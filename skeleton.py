import socket
import pyfiglet
import sys
from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue

# CLI output colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def port_open(host, port):
    """ Return true if connect succeeds. Else return False """
    s = socket.socket()

    try:
        s.connect([host, port])
        #ToDo: timout optimization
    except:
        return False
    return True

def scan(host):
    """ Iterate through prots 1-65535 """
    for port in range(1, 65535):
        if port_open(host, port):
            #Cool tip: reset output
            print(f"{GREEN}[*] {host}:{port} OPEN {RESET}")
        else:
            print(f"{GRAY}[*] {host}:{port} CLOSED {RESET}", end="\r")

def run_step_one():
    # get host from the user
    host = input("Enter host: ")
    scan(host)

def read_file(file):
    """ Read in a file, parse line by line, return a tuple of host and port combos"""
    f = open(file, "r")
    lines = f.readlines()
    host_port_tuples = []

    for line in lines:
        line = line.strip()
        line = line.split(":")
        host = line[0]
        port = int(line[1])
        host_port_tuples.append([host, port])
    
    return host_port_tuples

def scan_tuples(tuples):
    f = open("open_port.txt", "a")

    # iterate over tuples
    for host,port in tuples:
        if port_open(host, port):
            f.write(f"{host}:{port}"+"\n")
    
    f.close()
    print("Wrote to open_port.txt")

def run_step_two():
    # get filename to read host/port values from
    file = input("enter filename containing host port values")
    tuples = read_file(file)
    scan_tuples(tuples)

NUM_THREADS = 200
# ToDo: Performance tuning via thread counts
'''
The built-in queue module allows you to exchange data safely between
multiple threads. The Queue class in the queue module implements all 
required locking semantics.
'''
q = Queue() 
# print while using Threads
print_lock = Lock()

def scan_host_port(host, port):
    if port_open(host, port):
        with print_lock:
            print(f"{GREEN}[*] {host}:{port} OPEN {RESET}")

def scan_thread():
    """ Define how a single thread consumes from Queue """
    while True:
        worker = q.get()
        scan_host_port(worker[0], worker[1])
        q.task_done()

def setup_threads():
    for t in range(NUM_THREADS):
        t = Thread(target=scan_thread)
        t.daemon = True
        t.start()

def run_step_three():
    # ask user for host:port file and process with Threads
    setup_threads()

    filename = input("Enter filename containing host port values: ")
    tuples = read_file(filename)

    for host_port in tuples:
        q.put(host_port)
    
    # wait for all tasks before ending
    q.join()

def main():
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(ascii_banner)
    print("-" * 50)

    '''
    STEP 1
    '''
    # run_step_one()


    '''
    STEP 2
    '''
    # run_step_two()

    '''
    STEP 3
    '''
    run_step_three()

    print("-" * 50)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n Exiting Program!")
        sys.exit()