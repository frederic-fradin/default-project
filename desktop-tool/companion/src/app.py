"""Boucle principale du compagnon : événement de l'objet → état → page à redessiner."""

from src import image, link, pages, protocol

LED_COLOR = (255, 60, 0)


def run(stream):
    link.send(stream, protocol.encode(protocol.HELLO_REQ))
    hello = wait_for(stream, protocol.HELLO)
    print(f"Objet connecté : écran {hello['width']} × {hello['height']}, firmware {hello['firmware']}")

    state = {"last_key": None, "wheel": 0, "led": False, "busy": False, "dirty": False}
    redraw(stream, state, protocol.MODE_FULL)
    while (frame := protocol.read_frame(stream)) is not None:
        handle(stream, state, protocol.decode(*frame))
        # Une seule image à la fois chez l'objet : les événements reçus pendant un
        # rafraîchissement sont regroupés dans le dessin suivant.
        if state["dirty"] and not state["busy"]:
            redraw(stream, state, protocol.MODE_FAST)
    print("Objet déconnecté")


def wait_for(stream, msg_type):
    while (frame := protocol.read_frame(stream)) is not None:
        if frame[0] == msg_type:
            return protocol.decode(*frame)
    raise ConnectionError("connexion fermée avant la réponse de l'objet")


def handle(stream, state, message):
    if message["type"] == protocol.KEY and message["pressed"]:
        state["last_key"] = message["key"]
        if message["key"] == 0:
            state["led"] = not state["led"]
            color = LED_COLOR if state["led"] else (0, 0, 0)
            link.send(stream, protocol.encode(protocol.LED, target=0, red=color[0], green=color[1], blue=color[2]))
        state["dirty"] = True
    elif message["type"] == protocol.WHEEL:
        state["wheel"] += message["steps"]
        state["dirty"] = True
    elif message["type"] == protocol.DONE:
        state["busy"] = False
    elif message["type"] == protocol.ERROR:
        print(f"Erreur signalée par l'objet : code {message['code']}")


def redraw(stream, state, mode):
    pixels = image.to_4bpp(pages.hello(state))
    frame = protocol.encode(protocol.DRAW, x=0, y=0, width=pages.WIDTH, height=pages.HEIGHT, mode=mode, pixels=pixels)
    link.send(stream, frame)
    state["busy"] = True
    state["dirty"] = False
