
# Overview of Application
This project facilitates message communication between a **malicious** and **friendly** client and VPN server to a destination server. The malicious client performs two types of cyber attacks on the VPN server: DDoS (Distributed Denial-of-Service) and TunnelVision. TunnelVision attacks bypass the VPN encapsulation and redirects traffic outside of the VPN encrypted tunnel, permitting snooping, tampering or eavesdropping of sensitive information. DDoS attacks hijack the accesibility of server or network by flooding the server with traffic. The communication protocol permits standard exchange and specific command line arguments for simulated cyber attacks.

## Layer Interaction
* Client: Application sends messages to VPN server
* VPN server: Interprets client application messages and executes accordingly. Either performs an attack (using sim_attack.py if DDoS) or sends message to server.
* sim_attack: Executes DDoS attack on destination server.
* Server: Receives message from VPN server and echoes back to client. 

## Steps
* First, run the echo-server.py from the command line.
* Then the VPN.py server
* Last, run your message through client.py

# Client->VPN Server Message Format, VPN Server->Client Message Format & Example Output
Everything is run through client.py through the message function. If the client types 'tunnelvision' or 'ddos' in the message terminal input, then the VPN server will execute one of these attacks. If the client input message is anything but those two strings, then the message will be echoed back to the client. Client, VPN and server provide messages in the terminal to illustrate the connection process and communicate when connections have been established and whether messages have been received or not (an error message will appear.)

## No Attack

### client.py output with Command Line Trace
```
The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) garf:csc-249-p2-simple-VPN-server hannahsun$ python client.py --message 'whats lookin good cookin'
client starting - connecting to VPN at IP 127.0.0.1 and port 55554 whats lookin good cookin
connection established, sending message '127.0.0.1:65432:whats lookin good cookin'
message sent, waiting for reply
Received response: 'whats lookin good cookin' [24 bytes]
client is done!
```
### VPN.py output
```
The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) garf:csc-249-p2-simple-VPN-server hannahsun$ python VPN.py
VPN starting - listening for connections at IP 127.0.0.1 and port 55554
Connection established with client ('127.0.0.1', 56452)
Connected to server at 127.0.0.1:65432
Received response from server: 'whats lookin good cookin'
server message to client
```
## TunnelVision-Inspired Attack

### client.py output with Command Line Trace
A hacked message is sent back to the client instead of being echoed.
```
For more details, please visit https://support.apple.com/kb/HT208050.
(base) garf:csc-249-p2-simple-VPN-server hannahsun$ python client.py --message 'tunnelvision'
client starting - connecting to VPN at IP 127.0.0.1 and port 55554 tunnelvision
connection established, sending message '127.0.0.1:65432:tunnelvision'
message sent, waiting for reply
Received response: 'Hacked: 329304333442340700460594260782212301851' [47 bytes]
client is done!
```
### VPN.py output
This tells the client that the VPN encrypted tunnel has vulnerabilities and traffic has been diverted to a rouge network for snooping or eavesdropping.
```
The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) garf:csc-249-p2-simple-VPN-server hannahsun$ python VPN.py
VPN starting - listening for connections at IP 127.0.0.1 and port 55554
Connection established with client ('127.0.0.1', 56116)
Starting simulated TunnelVision-esque attack
Eavesdropper detected. Message intercepted and tampered.
Connected to server at 127.0.0.1:65432
Received response from server: 'Hacked: 282199385818148038304171235776974967102'
server message to client
```

## DDoS Attack 
I know DDoS Attacks are considered 'illegal' to execute (according to NeuralNine). However, I reduced the thread count to 5 instead of 500 to avoid completely flooding the server. Additionally, I created a fake IP address using a random number generator. 

### client.py output with Command Line Trace
```
The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) garf:csc-249-p2-simple-VPN-server hannahsun$ python client.py --message 'ddos'
client starting - connecting to VPN at IP 127.0.0.1 and port 55554 ddos
connection established, sending message '127.0.0.1:65432:ddos'
message sent, waiting for reply
Received response: '' [0 bytes]
client is done!
```

### echo-server.py output
```
For more details, please visit https://support.apple.com/kb/HT208050.
(base) garf:csc-249-p2-simple-VPN-server hannahsun$ python echo-server.py
server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 55413)
Received client message: 'b'GET /127.0.0.1 HTTP/1.1\r\nHost: 228.97.100.33\r\n\r\n'' [48 bytes]
echoing 'b'GET /127.0.0.1 HTTP/1.1\r\nHost: 228.97.100.33\r\n\r\n'' back to client
server is done!
(base) garf:csc-249-p2-simple-VPN-server hannahsun$ 
```

### VPN.py output
```
The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) garf:csc-249-p2-simple-VPN-server hannahsun$ python VPN.py
VPN starting - listening for connections at IP 127.0.0.1 and port 55554
Connection established with client ('127.0.0.1', 55534)
Starting simulated DOS attack. Please exit if you do not wish to continue
Attack Number:  1
Attack Number:  2
Attack Number:  3
Attack Number:  4
Exception in thread Thread-1 (attack):
Traceback (most recent call last):
  File "/Users/hannahsun/anaconda3/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
Exception in thread Thread-2 (attack):
Traceback (most recent call last):
  File "/Users/hannahsun/anaconda3/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
Exception in thread Thread-3 (attack):
Traceback (most recent call last):
  File "/Users/hannahsun/anaconda3/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
Exception in thread Thread-4 (attack):
Traceback (most recent call last):
  File "/Users/hannahsun/anaconda3/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/Users/hannahsun/anaconda3/lib/python3.11/threading.py", line 975, in run
    self.run()
  File "/Users/hannahsun/anaconda3/lib/python3.11/threading.py", line 975, in run
    self.run()
    self.run()
    self._target(*self._args, **self._kwargs)
  File "/Users/hannahsun/anaconda3/lib/python3.11/threading.py", line 975, in run
  File "/Users/hannahsun/anaconda3/lib/python3.11/threading.py", line 975, in run
  File "/Users/hannahsun/Desktop/work/2024_Fall/cs249/csc-249-p2-simple-VPN-server/sim_attacks.py", line 36, in attack
    self._target(*self._args, **self._kwargs)
    self._target(*self._args, **self._kwargs)
  File "/Users/hannahsun/Desktop/work/2024_Fall/cs249/csc-249-p2-simple-VPN-server/sim_attacks.py", line 36, in attack
  File "/Users/hannahsun/Desktop/work/2024_Fall/cs249/csc-249-p2-simple-VPN-server/sim_attacks.py", line 36, in attack
    s.connect((VPN_IP, VPN_PORT))
    self._target(*self._args, **self._kwargs)
ConnectionRefusedError: [Errno 61] Connection refused
  File "/Users/hannahsun/Desktop/work/2024_Fall/cs249/csc-249-p2-simple-VPN-server/sim_attacks.py", line 36, in attack
    s.connect((VPN_IP, VPN_PORT))
    s.connect((VPN_IP, VPN_PORT))
ConnectionRefusedError: [Errno 61] Connection refused
ConnectionRefusedError: [Errno 61] Connection refused
    s.connect((VPN_IP, VPN_PORT))
ConnectionRefusedError: [Errno 61] Connection refused
Exception in thread Thread-5 (attack):
Traceback (most recent call last):
  File "/Users/hannahsun/anaconda3/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/Users/hannahsun/anaconda3/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/hannahsun/Desktop/work/2024_Fall/cs249/csc-249-p2-simple-VPN-server/sim_attacks.py", line 36, in attack
    s.connect((VPN_IP, VPN_PORT))
ConnectionRefusedError: [Errno 61] Connection refused
```
# References
https://stackoverflow.com/questions/10012534/how-to-generate-a-big-random-number-in-python
https://pypi.org/project/eavesdropper/
https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_split4
https://www.techtarget.com/searchnetworking/definition/port-number
https://docs.python.org/3/library/argparse.html
https://www.linkedin.com/pulse/automating-network-traffic-using-data-generated-from-access-divine/
https://www.infosecinstitute.com/resources/general-security/python-for-network-penetration-testing-an-overview/
https://tools.keycdn.com/traceroute
https://www.imperva.com/learn/ddos/ping-icmp-flood/
https://allaboutcookies.org/does-vpn-prevent-ddos#:~:text=Although%20there's%20no%20guaranteed%20prevention,it%20well%20worth%20the%20investment.
https://www.security.org/vpn/ddos/
https://medium.com/@tommasobona04/how-to-code-a-dos-attack-in-python-by-tommaso-bona-b5387fc9c573
https://www.neuralnine.com/code-a-ddos-script-in-python/
https://www.guidepointsecurity.com/blog/tunnel-vision-cloudflared-abused-in-the-wild/
https://securityaffairs.com/162894/hacking/tunnelvision-attack-vpn.html
https://stackoverflow.com/questions/21014618/python-randomly-generated-ip-address-as-string
https://usa.kaspersky.com/resource-center/preemptive-safety/how-to-hide-ip
https://www.security.org/vpn/ddos/

