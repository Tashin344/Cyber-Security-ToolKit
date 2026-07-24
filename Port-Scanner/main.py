import scan_method



ip_input = input("Enter the IP Address: ")
start_port = int(input("Enter start Port: "))
end_port = int(input("Enter end Port: "))

scan_method.scan_method(ip_input, start_port, end_port)
