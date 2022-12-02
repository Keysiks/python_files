import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(("localhost", 6569))
client.connect(("localhost", 6568))

file_name = input("Enter file name: ")
encoding = "utf-8"
while file_name != "break":
    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            data = file.read()
        file_name = "next_file" + file_name.split("/")[-1]
        client.sendall(file_name.encode(encoding))
        for i in range(0, len(data), 1024):
            client.sendall(data[i:i + 1024])
            client.recv(1)
    file_name = input('Enter file name: ')

client.close()