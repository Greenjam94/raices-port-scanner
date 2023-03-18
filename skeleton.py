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

def run_step_one():
    # get host from the user

def run_step_two():
    # get filename to read host/port values from

NUM_THREADS = 200
'''
The built-in queue module allows you to exchange data safely between
multiple threads. The Queue class in the queue module implements all 
required locking semantics.
'''
q = Queue() 
# print while using Threads
print_lock = Lock()

def run_step_three():
    # ask user for host:port file and process with Threads

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
    # run_step_three()

    print("-" * 50)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n Exiting Program!")
        sys.exit()