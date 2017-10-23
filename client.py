#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
SERVER = sys.argv[1]
PORT = int(sys.argv[2])
LINE = sys.argv[3]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))

    if LINE == 'register':
        line = 'REGISTER sip:' + sys.argv[4] + ' SIP/2.0\r\n'
        my_socket.send(bytes(line, 'utf-8') + b'\r\n')
    else:
        sys.exit()
    
    print('Enviando:', line)
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))
    
print('Socket terminado.')
