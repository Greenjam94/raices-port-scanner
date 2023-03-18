# raices-port-scanner
A port scanner written in Python for RAICES NCR Chapter presentation.

*Warning: this is for learning purposes, do NOT use on unauthorized machines.*

### Introduction
* whoami
### Motivation (why a port scanner?)
* Automating security-related tasks
### Out-of-scope
* Software Engineering Best Practices
* Deployment of Python applications
### Install necessary dependencies
* git clone the repo and utilize the skeleton.py file (rename the file to port-scanner.py)
    * https://github.com/ccamac01/raices-port-scanner
* `pip3 install colorama`
* `pip3 install pyfiglet`
### Agenda
* Review Python Basics (that will be utilized)
    * Reading input
    * Writing to a file
    * For loops
    * If statements
    * Exceptions
* Writing a Basic Port Scanner
    * Sockets
        * Sockets are a way to enable inter-process communication between programs running on a server, or between programs running on separate servers. Communication between servers relies on network sockets, which use the Internet Protocol (IP) to encapsulate and handle sending and receiving data.
        * Network sockets on both clients and servers are referred to by their socket address. An address is a unique combination of a transport protocol like the Transmission Control Protocol (TCP) or User Datagram Protocol (UDP), an IP address, and a port number.
    * Reading input from files and writing output to files
    * Writing a Threaded Port Scanner (Advanced)
        * Threads
            * conceptualized as a methodology where we can tell the computer to do another task if the processor is experiencing idle time. In the case of port scanning, we are spending a lot of time just waiting on the response from the server. While we are waiting, we can do something else. That is what threading is used for. 
        * Locks 
### Q&A
### Bonus
* identify which services are running on your machine based on the open ports
### References
* https://www.geeksforgeeks.org/port-scanner-using-python/?ref=rp
* https://www.geeksforgeeks.org/threaded-port-scanner-using-sockets-in-python/?ref=rp
* https://www.thepythoncode.com/article/make-port-scanner-python
