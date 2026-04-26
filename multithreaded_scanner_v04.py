import socket
import threading
from queue import Queue
import time
import queue

print("=== MULTITHREADED SCANNER ===")
target = input("Enter Target IP: ")
print("Lock & Load... ")
print("-" * 30)

q = Queue()            
open_ports = []
start = int(input("Start Port: "))
end = int(input("End Port: "))
print("-" * 30)

time.time()
port_queue = queue.Queue()
queue_queue.qsize()
print(..., end='\r')

for port in range(start_port, end_port + 1):
    port_queue.put(port)
total_ports = end_port - start_port + 1
ports_left = port_queue.qsize()
ports_done = total_ports - ports_left
print(f"Scanning... {ports_done}/{total_ports}", end='\r')

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

thread_count = int(input("Enter Thread Count [10-200]: "))      # Start Threads
for x in range(thread_count):             
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
print("-" * 30)

for worker in range(start, end + 1):       # Putting each port in Queue
    q.put(worker)

q.join()

print("Scan COMPLETED! ")
print(f"Total Open Ports Found:{len(open_ports)} -> {sorted(open_ports)}")