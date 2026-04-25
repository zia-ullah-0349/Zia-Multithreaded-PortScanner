import socket
import threading
from queue import Queue

print("=== MULTITHREADED SCANNER ===")
target = input("Enter Target IP: ")
print("Lock & Load... ")
print("-" * 30)

q = Queue()            
open_ports = []
start = int(input("Start Port: "))
end = int(input("End Port: "))
print("-" * 30)

def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN! ")
            open_ports.append(port)
            try:                          # Banner Grabbing to send msg to open Port
                s.send(b"Hello\r\n")
                banner = s.recv(1024)
                print(f" ↪ BANNER: {banner.decode(errors='ignore').strip()}")
            except:
                print(f" ↪ BANNER: No reply... ")
            print("-" * 30)
        s.close()
    except:
        pass

def threader():                  # Creating Threads
    while True:
        worker = q.get()
        port_scan(worker)
        q.task_done()

for x in range(50):             # Start Threads
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(start, end + 1):       # Putting each port in Queue
    q.put(worker)

q.join()

print("Scan COMPLETED! ")
print(f"Total Open Ports Found:{len(open_ports)} -> {sorted(open_ports)}")