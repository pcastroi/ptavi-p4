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
            dline = line.decode('utf-8')
            if not line:
                continue
            elif dline.split(' ')[0] == 'REGISTER':
                self.resdic[dline.split(' ')[1][dline.find(':') + 1 : ]] = self.client_address[0]
                print("El cliente nos manda:", dline)
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
