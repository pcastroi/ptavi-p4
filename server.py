#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socketserver
import sys

class SIPRegisterHandler(socketserver.DatagramRequestHandler):

    resdic = {}
    def handle(self):

        print('IP cliente: ' + self.client_address[0] + '\t'
         + 'Puerto cliente: ' + str(self.client_address[1]))
        for line in self.rfile:
            dcline = line.decode('utf-8')
            if not line:
                continue
            elif dcline.split(' ')[0] == 'REGISTER':
                self.resdic[dcline.split(' ')[1]
                [dcline.split(' ')[1].find(':') + 1 : ]] = self.client_address[0]
                print("El cliente nos manda:", dcline)
                print(self.resdic)
                self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
            else:
                pass

if __name__ == "__main__":

    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler) 

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
