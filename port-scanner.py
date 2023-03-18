import socket
import sys
import pyfiglet
from threading import Thread, Lock
from queue import Queue
from colorama import init, Fore

# CLI output colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

'''
Step 1: Basic Port Scanner
Breakdown:
1) ask the user for a host (i.e., localhost)
2) iterate over ports 1-65534 to check if host:port is open
3) if open, print in GREEN; else, print in-place GRAY statement
'''

# port_open() determines whether `host` has the `port` open
def port_open(host, port):
    # Step 1: create a new socket
    s = socket.socket()

    # Step 2: try connecting to host on specified port
    try:
        # connect socket to remote address
        s.connect((host, port))
        # Optional: set a timeout value with s.settimeout()
    except:
        # if port is closed (can't connect)
        return False
    else:
        # port is open and connection established
        return True

def scan(host):
    # iterate over ports (1-65534)
    for port in range(1, 65535):
        if port_open(host, port):
            print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
        else:
            print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")

def run_step_one():
    # get host from the user
    host = input("Enter the host:")
    scan(host)

'''
Step 2: Port Scanner from File Input
Breakdown:
0) setup a hosts.txt file with `host:port` values (write-input-file.py)
1) ask user for a file containing `host:port` values (hosts.txt)
2) read_file() reads file, and processes line-by-line, storing (host, port) tuples
3) scan_tuples() calls port_open() on each tuple, and writes results to open_ports.txt
'''

def read_file(filename):
    f = open(filename, "r")
    lines = f.readlines()
    host_port_tuples = []
    for line in lines:
        line = line.strip() # remove newline character
        line = line.split(":") # split string into list on `:` character
        host = line[0]
        port = int(line[1]) # port must be an int in order for socket to connect
        # store host & port as tuple
        host_port_tuples.append((host, port))
    return host_port_tuples

# Writes new file containing result of scan
def scan_tuples(host_port_tuples):

    f = open("open_ports.txt", "a")
    
    # iterate over hosts/ports
    for host, port in host_port_tuples:
        if port_open(host, port):
            f.write(f"{host}:{port}" + "\n")
    f.close()
    print("Output written to open_ports.txt")

def run_step_two():
    # get filename to read host/port values from
    filename = input("Enter the filename containing `host:port` values: ")
    tuples = read_file(filename)
    scan_tuples(tuples)


'''
Step 3: Threaded Port Scanner
Note: took ~13s to complete multi-threaded, compared to ~3m for single-threaded
Breakdown:
0) Set number of threads, create Queue, create Lock for print statements
1) setup_threads() creates Threads and kicks them off to run scan_thread() function (consume work)
2) ask user for a file containing `host:port` values (hosts.txt)
3) read_file() reads file, and processes line-by-line, storing (host, port) tuples
4) for each tuple, add it to the Queue to be processed by workers
5) if port is open, use print_lock() to safely print results to screen
6) wait for all of the work on the Queue to be consumed by Threads before ending (q.join())
'''

NUM_THREADS = 200
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
            print(f"{GREEN}[+] {host}:{port} is open      {RESET}")

# Consumer: pulls work from the queue and processes it
def scan_thread():
    while True:
        # get the (host,port) tuple from the queue
        worker = q.get()
        # scan (host,port)
        scan_host_port(worker[0], worker[1])
        # notify queue of complete work
        q.task_done()

# create Threads and start them (tells them how to consume work)
def setup_threads(): 
    for t in range(NUM_THREADS):
        # for each thread, tell it to run the scan_thread() function
        t = Thread(target=scan_thread)
        # when daemon set to true, thread will end when the main thread ends
        # daemon is a process that runs in the background
        '''
        If a program is running Threads that are not daemons, then the program
        will wait for those threads to complete before it terminates. 
        Threads that are daemons, however, are just killed wherever they are when
        the program is exiting.
        '''
        t.daemon = True
        # start daemon thread
        t.start()

def run_step_three():
    setup_threads()

    filename = input("Enter the filename containing `host:port` values: ")
    tuples = read_file(filename)

    # for each host:port tuple, add tuple to queue to start scanning
    # Producer: add tasks to the queue
    for host_port in tuples:
        q.put(host_port)

    # waiting for all tasks on the queue to be completed
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