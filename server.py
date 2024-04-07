import socket
import time


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.server_socket = socket.socket()
        self.server_socket.bind((host, port))
        self.connection = None

    def accept(self):
        self.server_socket.listen(2)
        self.connection, address = self.server_socket.accept()
        print("Connection from: " + str(address))

    def close(self):
        self.connection.close()
        self.server_socket.close()

    def binary_to_string(self, binary_massage):
        message = ''
        counter = 0
        character = ''

        for bit in binary_massage:
            counter += 1

            character += bit
            if counter % 8 == 0:
                message += chr(int(character, 2))
                character = ''

        return message

    def receive(self):
        received = ""

        start = time.time()

        while True:
            start_time = time.time()
            data = self.connection.recv(1024).decode()
            end_time = time.time()

            print('channel data: ' + data)
            if not data:
                break

            if (end_time - start_time) > 0.00075:
                received += "1"
            else:
                received += "0"

        end = time.time()

        print("important message: " + self.binary_to_string(received[1:]))
        print('time: ' + str(end - start))


if __name__ == '__main__':
    host = socket.gethostname()
    port = 5400
    server = Server(host, port)
    server.accept()

    server.receive()
    server.close()
