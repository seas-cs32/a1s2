"""CS 32 helper library for Act I, Scene II"""

from typing import Tuple
import socket
from check32 import check_arg

HostType = str
PortType = int
AddressType = Tuple[HostType, PortType]


BUFFER_SIZE = 1024


class Socket32:
    """Socket32 is the CS32 custom socket class that simplifies
    client/server scripts built on top of `socket.socket`

    Example usage:

    with create_new_socket() as s:
        s.connect(HOST, PORT)

        s.sendall("some message")
        response = s.recv()
    """

    def __init__(self, sock: socket.socket):
        self._sock = sock

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._sock.__exit__(*args)

    def bind(self, host: str, port: int):
        """Bind the socket to address. The socket must not already be bound.

        Args:
            host (str): host name, with four numbers separated by three periods (like '127.0.0.1'). Also called an IP address
            port (int): port number (> 1023) to connect to.
        """
        check_arg(host, str, "host")
        check_arg(port, int, "port")
        self._sock.bind((host, port))

    def listen(self):
        """Enable a server to accept connections."""
        self._sock.listen()

    def accept(self) -> Tuple["Socket32", AddressType]:
        """Accept a connection.

        The socket must be bound to an address and listening for connections.

        Returns:
            Tuple[Socket32, AddressType]: A pair (conn, address) where conn is a new socket object usable to send and receive data on the connection,
                and address is the address bound to the socket on the other end of the connection.
        """
        conn, addr = self._sock.accept()
        return (Socket32(conn), addr)

    def connect(self, host: str, port: int):
        """Connect to a remote socket at the provided address (determined by host and port).


        If the connection is interrupted by a signal, the method waits until the connection completes,
        or raise a TimeoutError on timeout, if the signal handler doesn’t raise an exception and the socket is blocking or has a timeout.

        Args:
            host (str): host name, with four numbers separated by three periods (like '127.0.0.1'). Also called an IP address
            port (int): port number (> 1023) to connect to.
        """
        check_arg(host, str, "host")
        check_arg(port, int, "port")
        self._sock.connect((host, port))

    def sendall(self, msg: str):
        """Send data to the socket. The socket must be connected to a remote socket.

        Args:
            msg (str): The message to send to the remote socket
        """
        check_arg(msg, str, "msg")
        msg_bytes = msg.encode()
        self._sock.sendall(msg_bytes)

    def recv(self) -> str:
        """Receive data from the socket.

        Returns:
            str: The return value is a string representing the data received.
        """
        msg_bytes = self._sock.recv(BUFFER_SIZE)
        return msg_bytes.decode()


def create_new_socket() -> Socket32:
    return Socket32(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
