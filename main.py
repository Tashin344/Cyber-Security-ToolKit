import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_input = input("Enter the IP Address: ")
port_input = input("Enter the Port Number: ")

try:
    s.connect((ip_input, int(port_input)))
    print(f"{ip_input}:\n{port_input} OPEN")

except Exception as e:
    print(f"{ip_input}:{port_input}\nCLOSED.\nError: {e}")

finally:
    s.close()