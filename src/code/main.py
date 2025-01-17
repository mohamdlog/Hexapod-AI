# -*- coding: utf-8 -*-
from Server import *
from Control import *
import os

class Service():
    def __init__(self):
        self.active = False
        self.server = Server()
                
    def server_on(self):
        if self.active:
             print("\nServer is already activated. Enter '0' to de-activate the server, or 'exit' to exit: ")
        else:
            self.server.turn_on_server()
            self.instruction = threading.Thread(target = self.server.receive_instruction)
            self.instruction.start()
            self.active = True
            print("\nServer activated. Enter '0' to de-activate the server, or 'exit' to exit: ")

    def server_off(self):
        if not self.active :
             print("\nServer is already deactivated. Enter '1' to activate the server, or 'exit' to exit: ")
        else:
            try:
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
            print("\nServer de-activated. Enter '1' to activate the server, or 'exit' to exit: ")


if __name__ == '__main__':
    server = Service()

    print("NOTE: Do not exit without de-activating the server.\n")
    print("Enter '1' to activate the server, '0' to de-activate the server, or 'exit' to exit: ")
    
    while True:
        try:
            status=input()
            if status == '1':
                server.server_on()
            elif status == '0':
                server.server_off()
            elif status == 'exit':
                if server.active:
                    print("Deactivating server before exiting...")
                    server.server_off()
                print("\nExiting program.")
                os._exit(0)
            else:
                print("\nInvalid input. Please enter '1', '0', or 'exit'.")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Exiting program.")
            if server.active:
                server.server_off()
            os._exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")