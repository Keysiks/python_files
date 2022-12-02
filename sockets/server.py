import socketserver


class Server(socketserver.BaseRequestHandler):
    def handle(self):
        encoding = "utf-8"
        #получение файла
        data = self.request.recv(1024)
        while data:
            # обработка названия файла для сохранения в локальную папку
            data = data.split(b' ', 1)[-1]
            file = open(data.decode(encoding), "wb")
            while True:
                data = self.request.recv(1024)
                print(data)
                if data.startswith(b'next_file') or not data:
                    break
                file.write(data)
                self.request.sendall(b'1')


server = socketserver.TCPServer(("localhost", 6568), Server)
#запуск сервера
server.serve_forever()


