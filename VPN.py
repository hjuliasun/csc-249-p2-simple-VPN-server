#!/usr/bin/env python3

import socket
import arguments
import argparse
from sim_attacks import ddos
import random
# import time

# from client import SERVER_IP, SERVER_PORT

# Run 'python3 VPN.py --help' to see what these lines do
parser = argparse.ArgumentParser('Send a message to a server at the given address and prints the response')
parser.add_argument('--VPN_IP', help='IP address at which to host the VPN', **arguments.ip_addr_arg)
parser.add_argument('--VPN_port', help='Port number at which to host the VPN', **arguments.vpn_port_arg)
args = parser.parse_args()

VPN_IP = args.VPN_IP  # Address to listen on
VPN_PORT = args.VPN_port  # Port to listen on (non-privileged ports are > 1023)

def parse_message(message):

    message = message.decode("utf-8")
    # print("message:",message)
    # try: 
    # imsotired = message.split(':',1)
    # print(imsotired)
    SERVER_IP, SERVER_PORT, packet = message.split(':',2)
    

        # Parse the application-layer header into the destination SERVER_IP, destination SERVER_PORT,
        # and message to forward to that destination
        # raise NotImplementedError("Your job is to fill this function in. Remove this line when you're done.")
    return SERVER_IP, int(SERVER_PORT), packet
    # except Exception as exc:
    #     raise ValueError('Malformed message from client. Expected input: --server_IP --server_port ... --message. Expected format: SERVER_IP:SERVER_PORT:MESSAGE') from exc

### INSTRUCTIONS ###
# The VPN, like the server, must listen for connections from the client on IP address
# VPN_IP and port VPN_port. Then, once a connection is established and a message recieved,
# the VPN must parse the message to obtain the server IP address and port, and, without
# disconnecting from the client, establish a connection with the server the same way the
# client does, send the message from the client to the server, and wait for a reply.
# Upon receiving a reply from the server, it must forward the reply along its connection
# to the client. Then the VPN is free to close both connections and exit.

# The VPN server must additionally print appropriate trace messages and send back to the
# client appropriate error messages.

# def vpn_server():

print(f"VPN starting - listening for connections at IP {VPN_IP} and port {VPN_PORT}")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as vpn_socket:
    # connect w client
    vpn_socket.bind((VPN_IP, VPN_PORT))
    vpn_socket.listen()

    conn, addr = vpn_socket.accept()
    # print("conn",conn)
    # print("addr",addr)
    with conn:
        print(f"Connection established with client {addr}")
        data = conn.recv(1024)
        # print(data)
 
        SERVER_IP, SERVER_PORT, message = parse_message(data)

        if message == 'tunnelvision':
            print("Starting simulated TunnelVision-esque attack")
            message = f"Hacked: {random.getrandbits(128)}"
            print("Eavesdropper detected. Message intercepted and tampered.")
                    #sever connect
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.connect((SERVER_IP, SERVER_PORT))
                print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")
                server_socket.sendall(bytes(message, 'utf-8'))  # Send message to server
                
                server_response = server_socket.recv(1024)
                print(f"Received response from server: '{server_response.decode('utf-8')}'")

                # send message back to client
                conn.sendall(server_response)
                print("server message to client")
            # tunnelvision(SERVER_IP,SERVER_PORT)
        elif message == 'ddos':
            print("Starting simulated DDOS attack. Please exit if you do not wish to continue")

            ddos(SERVER_IP,SERVER_PORT)
        #print("message", message)
        #print("SERVERIP", SERVER_IP)
        else:
        #sever connect
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.connect((SERVER_IP, SERVER_PORT))
                print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")
                server_socket.sendall(bytes(message, 'utf-8'))  # Send message to server
                
                server_response = server_socket.recv(1024)
                print(f"Received response from server: '{server_response.decode('utf-8')}'")

                # send message back to client
                conn.sendall(server_response)
                print("server message to client")
    


# print("VPN starting - connecting to server at IP", VPN_IP, "and port", VPN_PORT)
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as vpn_s:
#     vpn_s.bind((VPN_IP,VPN_PORT))
#     vpn_s.listen()
#     # while True: 
#     conn, addr = vpn_s.accept()

#     with conn: 
#         print(f"Connected established with {addr}")
#         # while True: 
#         data = conn.recv(1024)
#             # if not data: 
#             #     break
#         SERVER_IP, SERVER_PORT, MESSAGE = parse_message(data)

#         print(f"Received message: '{MESSAGE!r}' [{len(MESSAGE)} bytes]")

#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_s:
#             server_s.connect((SERVER_IP,SERVER_PORT))
#             print(f"connection established, sending message '{MESSAGE}'")
#             server_s.sendall(bytes(MESSAGE, 'utf-8'))
#             print("message sent, waiting for reply")
#             server_data = server_s.recv(1024).decode("utf-8")
#             print(f"Received response: '{server_data}' [{len(server_data)} bytes]")


#             conn.sendall(bytes(server_data, 'utf-8'))

#     print("vpn is done!")











