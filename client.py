import socket
import string
import time
import random


class Client:
    def __init__(self):
        self.client_socket = socket.socket()

    def connect_to_server(self, host, port):
        try:
            self.client_socket.connect((host, port))
            return True
        except Exception as e:
            self.close()
            return False

    def string_to_binary(self, message):
        binary_message = ''.join(format(ord(ch), '08b') for ch in message)
        return binary_message

    def generate_random_string(self, n):
        return ''.join(random.choices(string.ascii_lowercase +
                                      string.digits, k=n))

    def close(self):
        self.client_socket.close()

    def send_message(self, message):
        binary_msg = self.string_to_binary(message)
        print(binary_msg)

        for bit in binary_msg:
            self.client_socket.send(self.generate_random_string(5).encode())
            if bit == '1':
                time.sleep(0.001)
            else:
                time.sleep(0.0005)

        self.client_socket.send("FIN".encode())


if __name__ == '__main__':
    server_host = socket.gethostname()
    server_port = 5400

    client = Client()
    client.connect_to_server(server_host, server_port)

    client.send_message(input('-> '))
    client.close()
