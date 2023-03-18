'''
Generate a hosts.txt file for testing file I/O handling in port-scanner
'''

f = open("hosts.txt", "a")

for port in range(1, 65535):
    f.write("localhost:" + str(port) + "\n")

f.close()
