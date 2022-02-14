# Guessing game -- server

import random

from socket32 import create_new_socket


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


def main():
    secret = random.randint(1, 100)
    # print(f'The secret number is {the_secret}')

    with create_new_socket() as s:
        s.bind(HOST, PORT)
        s.listen()
        print(
            f"GUESS-THE-NUMBER server started. Listening on host {HOST} at port {PORT} ({HOST}:{POST})",
            (HOST, PORT),
        )

        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            while True:
                guess = conn.recv()
                if not guess:
                    break
                guess = int(guess)

                # Check guess against secret and respond
                if guess < secret:
                    conn.sendall('Too small!')
                elif guess == secret:
                    conn.sendall('Exactly! You win!')
                    break
                else:
                    conn.sendall('Too big!')

            print('Disconnected')


if __name__ == '__main__':
    main()
