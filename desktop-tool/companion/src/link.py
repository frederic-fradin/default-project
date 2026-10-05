"""Connexion à l'objet : simulateur (TCP local) ou carte (port série USB).

Les deux se lisent et s'écrivent comme un fichier : le reste du code ne voit pas la différence.
"""

import socket

SIM_HOST = "127.0.0.1"
SIM_PORT = 8765


def open_link(target):
    """target : "sim" pour le simulateur, sinon le port série de la carte (ex. "COM5")."""
    if target == "sim":
        return socket.create_connection((SIM_HOST, SIM_PORT)).makefile("rwb")
    import serial

    return serial.Serial(target)


def send(stream, frame):
    stream.write(frame)
    stream.flush()
