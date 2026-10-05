"""Simulateur de l'objet : une fenêtre qui reçoit et envoie les mêmes trames que la carte (ADR 007).

Lancer `python simulator.py`, puis le compagnon avec `python main.py`.
Touches 1 à 4 du clavier, rangée du haut ou pavé numérique (ou clic) = les 4 touches ; roulette de la souris = molette ;
Entrée (ou clic sur la molette) = clic de la molette.
"""

import queue
import socket
import threading
import tkinter as tk

from PIL import Image, ImageTk

from src import image, link, pages, protocol

FIRMWARE = 0  # 0 = simulateur
MARGIN = 32
BAND = 150  # bande des commandes sous l'écran (pas à l'échelle)
KNOB_X, KNOB_RADIUS = 90, 52
KEY_SIZE = 84

BODY = "#2b2b2b"  # Charcoal Black
KNOB = "#8a2e2a"  # Army Red
KEY_OUTLINE = "#444444"
SYMBOL = "#5a5a5a"

# Délais imitant l'e-paper : rafraîchissement complet = flash noir, flash blanc, puis l'image.
FLASH_MS = 150
FULL_MS = 1000
FAST_MS = 300


def main():
    root = tk.Tk()
    root.title("Simulateur desktop-tool : en attente du compagnon")
    root.configure(bg=BODY)
    canvas = tk.Canvas(
        root, width=pages.WIDTH + 2 * MARGIN, height=pages.HEIGHT + MARGIN + BAND, bg=BODY, highlightthickness=0
    )
    canvas.pack()

    state = {"stream": None, "screen": Image.new("L", (pages.WIDTH, pages.HEIGHT), pages.WHITE), "held": set()}
    ui = {"root": root, "canvas": canvas, "photo": None}
    ui["screen"] = canvas.create_image(MARGIN, MARGIN, anchor="nw")
    draw_controls(ui, state)
    show(ui, state["screen"])

    root.bind("<KeyPress>", lambda event: on_key(state, event, pressed=True))
    root.bind("<KeyRelease>", lambda event: on_key(state, event, pressed=False))
    root.bind("<MouseWheel>", lambda event: on_wheel(state, event))

    inbox = queue.Queue()
    threading.Thread(target=serve, args=(inbox, state), daemon=True).start()
    poll(ui, state, inbox)
    root.mainloop()


def draw_controls(ui, state):
    """Molette en bas à gauche, 4 touches en bas à droite, alignées sur leurs étiquettes."""
    canvas = ui["canvas"]
    y = MARGIN + pages.HEIGHT + BAND // 2
    ui["knob"] = canvas.create_oval(
        MARGIN + KNOB_X - KNOB_RADIUS, y - KNOB_RADIUS, MARGIN + KNOB_X + KNOB_RADIUS, y + KNOB_RADIUS,
        fill=KNOB, outline=KEY_OUTLINE, width=4,
    )
    bind_press(canvas, ui["knob"], state, 4)
    ui["keys"] = []
    for index, key_x in enumerate(pages.KEY_X):
        x = MARGIN + key_x
        half = KEY_SIZE // 2
        key = canvas.create_rectangle(x - half, y - half, x + half, y + half, fill=BODY, outline=KEY_OUTLINE, width=4)
        ui["keys"].append(key)
        bind_press(canvas, key, state, index)
        for item in draw_symbol(canvas, index, x, y):
            bind_press(canvas, item, state, index)


def draw_symbol(canvas, index, x, y):
    """1, 2 ou 3 barres verticales, ou une maison (ADR 004)."""
    if index == 3:
        return [canvas.create_polygon(x - 12, y + 12, x - 12, y - 2, x, y - 13, x + 12, y - 2, x + 12, y + 12, fill=SYMBOL)]
    count = index + 1
    first = x - (count - 1) * 5
    return [canvas.create_rectangle(first + n * 10 - 2, y - 11, first + n * 10 + 2, y + 11, fill=SYMBOL, outline="") for n in range(count)]


def bind_press(canvas, item, state, key):
    canvas.tag_bind(item, "<ButtonPress-1>", lambda event: send_key(state, key, 1))
    canvas.tag_bind(item, "<ButtonRelease-1>", lambda event: send_key(state, key, 0))


def on_key(state, event, pressed):
    # Code de touche Windows plutôt que caractère : en AZERTY, la touche « 1 » donne « & ».
    # Rangée du haut, pavé numérique, puis Entrée.
    key = {0x31: 0, 0x32: 1, 0x33: 2, 0x34: 3, 0x61: 0, 0x62: 1, 0x63: 2, 0x64: 3, 0x0D: 4}.get(event.keycode)
    if key is None:
        return
    # Windows répète l'appui tant que la touche est enfoncée : n'envoyer que le premier.
    if pressed and key in state["held"]:
        return
    (state["held"].add if pressed else state["held"].discard)(key)
    send_key(state, key, int(pressed))


def send_key(state, key, pressed):
    send(state, protocol.encode(protocol.KEY, key=key, pressed=pressed))


def on_wheel(state, event):
    # Roulette vers soi = sens horaire = +1 ; un cran vaut 120 sous Windows.
    steps = max(-128, min(127, -event.delta // 120))
    if steps:
        send(state, protocol.encode(protocol.WHEEL, steps=steps))


def send(state, frame):
    if state["stream"] is None:
        return
    try:
        link.send(state["stream"], frame)
    except OSError:
        pass


def serve(inbox, state):
    """Fil d'attente des trames : accepte le compagnon, lit ses trames, recommence s'il se déconnecte."""
    server = socket.create_server((link.SIM_HOST, link.SIM_PORT))
    while True:
        connection, _ = server.accept()
        state["stream"] = connection.makefile("rwb")
        inbox.put(("connected", None))
        while True:
            try:
                frame = protocol.read_frame(state["stream"])
            except ValueError:
                inbox.put(("bad_frame", None))
                continue
            except OSError:
                break
            if frame is None:
                break
            inbox.put(("frame", frame))
        state["stream"] = None
        connection.close()
        inbox.put(("disconnected", None))


def poll(ui, state, inbox):
    """Traite dans la fenêtre (seul fil autorisé à la modifier) ce que le fil réseau a reçu."""
    while not inbox.empty():
        kind, frame = inbox.get()
        if kind == "connected":
            ui["root"].title("Simulateur desktop-tool : compagnon connecté")
        elif kind == "disconnected":
            ui["root"].title("Simulateur desktop-tool : en attente du compagnon")
        elif kind == "bad_frame":
            send(state, protocol.encode(protocol.ERROR, code=protocol.ERROR_FRAME))
        else:
            handle(ui, state, *frame)
    ui["root"].after(15, poll, ui, state, inbox)


def handle(ui, state, msg_type, payload):
    try:
        message = protocol.decode(msg_type, payload)
    except ValueError:
        code = protocol.ERROR_TYPE if msg_type not in protocol.FORMATS else protocol.ERROR_SIZE
        send(state, protocol.encode(protocol.ERROR, code=code))
        return
    if msg_type == protocol.HELLO_REQ:
        send(state, protocol.encode(
            protocol.HELLO, protocol=protocol.PROTOCOL_VERSION, firmware=FIRMWARE,
            width=pages.WIDTH, height=pages.HEIGHT, bpp=4, keys=4,
        ))
    elif msg_type == protocol.LED:
        set_led(ui, message)
    elif msg_type == protocol.DRAW:
        start_draw(ui, state, message)


def set_led(ui, message):
    if message["target"] > 4:
        return
    color = (message["red"], message["green"], message["blue"])
    outline = KEY_OUTLINE if color == (0, 0, 0) else "#%02x%02x%02x" % color
    item = ui["knob"] if message["target"] == 4 else ui["keys"][message["target"]]
    ui["canvas"].itemconfig(item, outline=outline)


def start_draw(ui, state, message):
    error = protocol.check_draw(message, pages.WIDTH, pages.HEIGHT)
    if error:
        send(state, protocol.encode(protocol.ERROR, code=error))
        return
    zone = image.from_4bpp(message["pixels"], message["width"], message["height"])
    box = (message["x"], message["y"], message["x"] + message["width"], message["y"] + message["height"])

    def finish():
        state["screen"].paste(zone, box)
        show(ui, state["screen"])
        send(state, protocol.encode(protocol.DONE, handled=protocol.DRAW))

    after = ui["root"].after
    if message["mode"] == protocol.MODE_FULL:
        after(0, flash, ui, state, box, pages.BLACK)
        after(FLASH_MS, flash, ui, state, box, pages.WHITE)
        after(FULL_MS, finish)
    else:
        after(FAST_MS, finish)


def flash(ui, state, box, level):
    screen = state["screen"].copy()
    screen.paste(level, box)
    show(ui, screen)


def show(ui, screen):
    ui["photo"] = ImageTk.PhotoImage(screen)  # garder la référence, sinon tkinter efface l'image
    ui["canvas"].itemconfig(ui["screen"], image=ui["photo"])


if __name__ == "__main__":
    main()
