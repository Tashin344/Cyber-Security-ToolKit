import socket

def banner_send(sock, ip_input):

    
    request = (f"GET / HTTP/1.1\r\nHost: {ip_input}\r\n\r\n")
    sock.send(request.encode())
    response = sock.recv(1024).decode()
    response_header = response.split('\r\n\r\n') [0]

    return response_header
    