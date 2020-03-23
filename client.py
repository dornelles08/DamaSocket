import socket
from drawField import Dama
import pygame
from pygame.locals import *
import os

pygame.init()
def menuGame():
    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Dama")
    time = pygame.time.Clock()
    inicio = True
    win.blit(pygame.image.load(os.path.join("imagens", "inicio.png")),(0,0))
    while inicio:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pygame.Rect(256,87,234,56).collidepoint(pos[0], pos[1]):                        
                    inicio = False
                if pygame.Rect(299,162,114,56).collidepoint(pos[0], pos[1]):                        
                    win.blit(pygame.image.load(os.path.join("imagens", "sobre.png")),(0,0))
                if pygame.Rect(183,427,134,63).collidepoint(pos[0], pos[1]):                        
                    win.blit(pygame.image.load(os.path.join("imagens", "inicio.png")),(0,0))

        pygame.display.update()
        time.tick(30)
    pygame.quit()

#conexão com o servidor
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = ('127.0.0.1', 5000)
tcp.connect(dest)

#recebendo reposta do servidor
msg = tcp.recv(1024)
tcp.close()

msg = msg.decode("utf-8")

if msg == "Esperando Adversario": 

    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Dama")
    win.blit(pygame.image.load(os.path.join("imagens", "aguardandoAdversario.png")),(0,0))
    pygame.display.update()

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('127.0.0.1', 5050))
    tcp.listen(1)
    con, adversario = tcp.accept()    

    msg = con.recv(1024)
    print("Recebida: {}".format(msg.decode('utf-8')))
    pygame.quit()

    menuGame()
    a = Dama(1)
    a.main(con)
    con.close()

else:

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((msg, 5050))
    tcp.send(bytes("Olá", 'utf-8'))

    menuGame()
    a = Dama(0)
    a.main(tcp)
    tcp.close()

