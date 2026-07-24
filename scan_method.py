import socket

def scan_method(ip_input, start_port, end_port):
    
    for i in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((ip_input, i))
            print(f"{ip_input}:\n{i} OPEN")
        except Exception as e:
            print(f"{ip_input}:{i}\nCLOSED.\nError: {e}")
        finally:
            s.close()