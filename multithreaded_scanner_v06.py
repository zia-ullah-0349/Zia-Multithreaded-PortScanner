import socket
import threading
from queue import Queue
import time
from datetime import datetime

print("=== MULTITHREADED SCANNER ===")
target = input("Enter Target IP: ")
start = int(input("Start Port: "))
end = int(input("End Port: "))
thread_count = int(input("Enter Thread Count [10-200]: "))  
print("Lock & Load... ")
print("-" * 30)

filename = f"scan_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

with open(filename, 'w') as f:
    f.write(f"=== SCAN REPORTS ===\n")
    f.write(f"Target: {target}\n")
    f.write(f"ports: {start}-{end}\n")
    f.write(f"Threads: {thread_count}\n")
    f.write(f"Started: {datetime.now()}\n")
    f.write("-" * 30)

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 3306: "MySQL",
    3389: "RDP", 8080: "HTTP-Proxy"
}
port_queue = Queue()
open_ports = []
total_ports = end - start + 1
start_time = time.time()
print_lock = threading.Lock()         # We create a LOCK here

for port in range(start, end + 1):
    port_queue.put(port)

def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            with print_lock:            # Put LOCK
                open_ports.append(port)
                service_name = COMMON_PORTS.get(port, "Unknown")    # Service Name
                try:                          # Banner Grabbing to send msg to open Port
                   s.send(b"Hello\r\n")
                   banner = s.recv(1024).decode(errors='ignore').strip()
                   result_line = f"\nPort {port} is OPEN! ↪ Service: {service_name} | BANNER: {banner}"  
                   print(" " * 60, end='\r')  # FIX 1: r ki jagah \r aur 60 spaces
                   print(f"{result_line}")    # FIX: \n hata diya result_line mein already hai
                   print("-" * 30)
                   with open(filename, 'a') as f:
                    f.write(result_line + "\n")
                except:
                    # FIX 2: result_line yahan bhi banaya
                    result_line = f"\nPort {port} is OPEN! ↪ Service: {service_name} | BANNER: No Reply... "
                    print(" " * 60, end='\r')  # FIX 1: r ki jagah \r
                    print(f"{result_line}")
                    print("-" * 30)
                    with open(filename, 'a') as f:
                      f.write(result_line + "\n")
                # FIX 4: Ye extra line thi, hata di -> print("-" * 30)
            s.close()
    except:
        pass

def threader():                  # Creating Threads
    while True:
        if port_queue.empty():
            break
        worker = port_queue.get()

        with print_lock:        # To LOCK the progress bar
            port_done = total_ports - port_queue.qsize()
            elapsed = time.time() - start_time
            print(f"Scanning... {port_done}/{total_ports} | Time: {elapsed:.1f}s | Found: {len(open_ports)}", end='\r')
        port_scan(worker)
        port_queue.task_done()

threads = []                  # Start Threads
for x in range(thread_count):             
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()

total_time = time.time() - start_time
with print_lock:       # For final print   
    print(" " * 60, end='\r')  # FIX 1: r ki jagah \r
    # FIX 3: print = hata kar sirf print kar diya
    print(f"\nScan COMPLETED in {total_time:.2f} seconds! ")
    print(f"Total Open Ports Found:{len(open_ports)} -> {sorted(open_ports)}")
    print("-" * 30)

with open(filename, 'a') as f:
    f.write("-" * 30 + "\n")
    f.write(f"Scan COMPLETED in {total_time:.2f} seconds!\n")
    f.write(f"Total Open Ports Found:{len(open_ports)} -> {sorted(open_ports)}\n")
    f.write("-" * 30 + "\n")
print(f"\n[+] Results saved to {filename}")