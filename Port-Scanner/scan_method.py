import socket
import banner_grabbing

def scan_method(ip_input, start_port, end_port):
    
    for i in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((ip_input, i))
            banner = banner_grabbing.banner_send(s, ip_input)
            print(f"{ip_input}:\n{i} OPEN ✅")
            if banner:
                print(f"{banner}\n")
        except socket.timeout as TimedoutError:
            print(f"{ip_input}:{i}\nTIMED OUT ⏱️\n")
        except Exception as e:
            print(f"{ip_input}:{i}\nCLOSED ❌\n")
        finally:
            s.close()