# -*- coding: utf-8 -*-
from Server import *
from Control import *

class Service():
    def __init__(self):
        self.active = False
        self.server = Server()
                
    def server_on(self):
        if self.active == True:
             print("Server is already activated. Enter 'n' to deactivate the server.")
        else:
            self.server.turn_on_server()
            self.video = threading.Thread(target = self.server.transmission_video)
            self.video.start()
            self.instruction = threading.Thread(target = self.server.receive_instruction)
            self.instruction.start()
            self.active = True
            print("\nServer activated. Enter 'n' to de-activate the server.")

    def server_off(self):
        if self.active == False:
             print("Server is already deactivated. Enter 'y' to activate the server.")
        else:
            try:
                stop_thread(self.video)
                stop_thread(self.instruction)
            except Exception as e:
                    print(e)
            try:
                self.server.server_socket.shutdown(2)
                self.server.server_socket1.shutdown(2)
                self.server.turn_off_server()
            except Exception as e:
                    print(e)
            self.active = False
            print("\nServer de-activated. Enter 'y' to activate the server.")

if __name__ == '__main__':
    server = Service()
    print("NOTE: Do not exit without de-activating the server\n")

    start = input("Enter 'y' to activate the server, or 'n' to de-activate the server: ").lower()

    if start == 'y':
         server.server_on()
    elif start == 'n':
         server.server_off()
    
    while True:
        status = input().lower()
        if status == 'y':
             server.server_on()
        elif status == 'n':
             server.server_off()