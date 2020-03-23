import pygame
from pygame.locals import *
import os
import pickle
from threading import Thread
from queue import Queue

q = Queue()

class Enviar:
    def __init__(self, pretas, brancas, vez):
        self.pretas = pretas
        self.brancas = brancas
        self.vez = vez        
        self.CrirarObjeto()

    def CrirarObjeto(self):
        preta = []
        branca = []
        for p in self.pretas:
            preta.append([p[0], None, p[2]])
        for b in self.brancas:
            branca.append([b[0], None, b[2]])
        self.pretas = preta
        self.brancas = branca
    
    def AtualizarObjeto(self):
        PRETA  = pygame.image.load(os.path.join("imagens", "preta.png"))
        BRANCA = pygame.image.load(os.path.join("imagens", "branca.png"))
        DAMAPRETA = pygame.image.load(os.path.join("imagens", "pretaDama.png"))
        DAMABRANCA = pygame.image.load(os.path.join("imagens", "brancaDama.png"))
        for p in self.pretas:
            if p[2]:
                p[1] = DAMAPRETA
            else:
                p[1] = PRETA
        
        for b in self.brancas:
            if b[2]:
                b[1] = DAMABRANCA
            else:
                b[1] = BRANCA

        return self.pretas, self.brancas, self.vez

class Listener(Thread):
    def __init__(self, con):
        Thread.__init__(self)
        self.con = con

    def run(self):
        laco = True
        while laco:
            try:
                msg = self.con.recv(1024)
                receber = pickle.loads(msg)
                pretas, brancas, vez = receber.AtualizarObjeto()
                q.put(pretas)
                q.put(brancas)
                q.put(vez)
            except:
                laco = False
        
class Dama:
    def __init__(self, color):
        self.window = pygame.display.set_mode((500,500))
        pygame.display.set_caption("Dama")
        self.clock = pygame.time.Clock()
        self.loop = True
        self.PRETA  = pygame.image.load(os.path.join("imagens", "preta.png"))
        self.BRANCA = pygame.image.load(os.path.join("imagens", "branca.png"))
        self.DAMAPRETA = pygame.image.load(os.path.join("imagens", "pretaDama.png"))
        self.DAMABRANCA = pygame.image.load(os.path.join("imagens", "brancaDama.png"))
        self.YOURTURN = pygame.image.load(os.path.join("imagens", "suaVez.png"))
        self.WAIT = pygame.image.load(os.path.join("imagens", "aguardando.png"))

        self.campo = [
            [[(50,50,50,50),  (150,150,150)], [(100,50,50,50),  (255,255,255)], [(150,50,50,50),  (150,150,150)], [(200,50,50,50),  (255,255,255)], [(250,50,50,50),  (150,150,150)], [(300,50,50,50),  (255,255,255)], [(350,50,50,50),  (150,150,150)], [(400,50,50,50),  (255,255,255)]],
            [[(50,100,50,50), (255,255,255)], [(100,100,50,50), (150,150,150)], [(150,100,50,50), (255,255,255)], [(200,100,50,50), (150,150,150)], [(250,100,50,50), (255,255,255)], [(300,100,50,50), (150,150,150)], [(350,100,50,50), (255,255,255)], [(400,100,50,50), (150,150,150)]],
            [[(50,150,50,50), (150,150,150)], [(100,150,50,50), (255,255,255)], [(150,150,50,50), (150,150,150)], [(200,150,50,50), (255,255,255)], [(250,150,50,50), (150,150,150)], [(300,150,50,50), (255,255,255)], [(350,150,50,50), (150,150,150)], [(400,150,50,50), (255,255,255)]],
            [[(50,200,50,50), (255,255,255)], [(100,200,50,50), (150,150,150)], [(150,200,50,50), (255,255,255)], [(200,200,50,50), (150,150,150)], [(250,200,50,50), (255,255,255)], [(300,200,50,50), (150,150,150)], [(350,200,50,50), (255,255,255)], [(400,200,50,50), (150,150,150)]],
            [[(50,250,50,50), (150,150,150)], [(100,250,50,50), (255,255,255)], [(150,250,50,50), (150,150,150)], [(200,250,50,50), (255,255,255)], [(250,250,50,50), (150,150,150)], [(300,250,50,50), (255,255,255)], [(350,250,50,50), (150,150,150)], [(400,250,50,50), (255,255,255)]],
            [[(50,300,50,50), (255,255,255)], [(100,300,50,50), (150,150,150)], [(150,300,50,50), (255,255,255)], [(200,300,50,50), (150,150,150)], [(250,300,50,50), (255,255,255)], [(300,300,50,50), (150,150,150)], [(350,300,50,50), (255,255,255)], [(400,300,50,50), (150,150,150)]],
            [[(50,350,50,50), (150,150,150)], [(100,350,50,50), (255,255,255)], [(150,350,50,50), (150,150,150)], [(200,350,50,50), (255,255,255)], [(250,350,50,50), (150,150,150)], [(300,350,50,50), (255,255,255)], [(350,350,50,50), (150,150,150)], [(400,350,50,50), (255,255,255)]],
            [[(50,400,50,50), (255,255,255)], [(100,400,50,50), (150,150,150)], [(150,400,50,50), (255,255,255)], [(200,400,50,50), (150,150,150)], [(250,400,50,50), (255,255,255)], [(300,400,50,50), (150,150,150)], [(350,400,50,50), (255,255,255)], [(400,400,50,50), (150,150,150)]],
        ]
        '''self.pretas  = [
            [self.campo[0][0][0], self.PRETA, False],  [self.campo[0][2][0], self.PRETA, False], [self.campo[0][4][0], self.PRETA, False], [self.campo[0][6][0], self.PRETA, False],
            [self.campo[1][1][0], self.PRETA, False],  [self.campo[1][3][0], self.PRETA, False], [self.campo[1][5][0], self.PRETA, False], [self.campo[1][7][0], self.PRETA, False],
            [self.campo[2][0][0], self.PRETA, False],  [self.campo[2][2][0], self.PRETA, False], [self.campo[2][4][0], self.PRETA, False], [self.campo[2][6][0], self.PRETA, False]
        ]
        self.brancas = [
            [self.campo[7][1][0], self.BRANCA, False], [self.campo[7][3][0], self.BRANCA, False], [self.campo[7][5][0], self.BRANCA, False], [self.campo[7][7][0], self.BRANCA, False],
            [self.campo[6][0][0], self.BRANCA, False], [self.campo[6][2][0], self.BRANCA, False], [self.campo[6][4][0], self.BRANCA, False], [self.campo[6][6][0], self.BRANCA, False],
            [self.campo[5][1][0], self.BRANCA, False], [self.campo[5][3][0], self.BRANCA, False], [self.campo[5][5][0], self.BRANCA, False], [self.campo[5][7][0], self.BRANCA, False]
        ]'''
        self.pretas  = [
            [self.campo[0][0][0], self.PRETA, False]
        ]
        self.brancas = [
            [self.campo[1][1][0], self.BRANCA, False]
        ]

        self.peiceSelected = None
        self.posSelected = None
        self.posibilityMove = []
        self.vez = 1
        self.peiceColor = color
        self.vezText = None
        if self.peiceColor == 1:
            self.vezText = self.YOURTURN
        else:
            self.vezText = self.WAIT
   
    def UpdateParameter(self):
        self.pretas = q.get()
        self.brancas = q.get()        
        if self.vez == 0:
            if self.peiceColor == 1:
                self.vezText = self.YOURTURN
            elif self.peiceColor == 0:
                self.vezText = self.WAIT
        else:
            if self.peiceColor == 1:
                self.vezText = self.WAIT
            elif self.peiceColor == 0:
                self.vezText = self.YOURTURN
        self.vez = q.get()

    def Field(self):
        for linha in self.campo:        
            for coluna in linha:            
                    pygame.draw.rect(self.window, coluna[1], coluna[0])
        
    def Peices(self):
        for p in self.pretas:
            self.window.blit(p[1], (p[0][0], p[0][1]))
        for b in self.brancas:
            self.window.blit(b[1], (b[0][0], b[0][1]))

    def SelectPeice(self, pos):
        for i in range(len(self.pretas)):
            if pygame.Rect(self.pretas[i][0][0], self.pretas[i][0][1], self.pretas[i][0][2], self.pretas[i][0][3]).collidepoint(pos[0], pos[1]) and self.peiceColor == 0:
                return i, 0
        for i in range(len(self.brancas)):
            if pygame.Rect(self.brancas[i][0][0], self.brancas[i][0][1], self.brancas[i][0][2], self.brancas[i][0][3]).collidepoint(pos[0], pos[1]) and self.peiceColor == 1:
                return i, 1
        return None, None
        
    def SelectPos(self, pos):
        for i in range(len(self.campo)):
            for j in range(len(self.campo[i])):
                temp = self.campo[i][j][0]
                if pygame.Rect(temp[0], temp[1], temp[2], temp[3]).collidepoint(pos[0], pos[1]):
                    return temp, i, j

    def changeColorSelectedPeice(self, peice, selected):
        if peice == 0:
            for i in range(len(self.campo)):
                for j in range(len(self.campo[i])):
                    if self.campo[i][j][0] == self.pretas[selected][0]:
                        self.campo[i][j][1] = (0,255,0)
                        break
        else:
            for i in range(len(self.campo)):
                for j in range(len(self.campo[i])):
                    if self.campo[i][j][0] == self.brancas[selected][0]:
                        self.campo[i][j][1] = (0,255,0)
                        break
        
    def Colission(self, posPeice, posOpponent, cor, linha, coluna):
        if cor == 0:
            if posPeice[0] > posOpponent[0]:
                try:
                    return self.campo[linha+2][coluna-2][0]
                except:
                    return None
            elif posPeice[0] < posOpponent[0]:
                try:
                    return self.campo[linha+2][coluna+2][0]
                except:
                    return None
        elif cor == 1:
            if posPeice[0] > posOpponent[0]:
                try:
                    return self.campo[linha-2][coluna-2][0]
                except:
                    return None
            elif posPeice[0] < posOpponent[0]:
                try:
                    return self.campo[linha-2][coluna+2][0]
                except:
                    return None

    def MovePosibility(self, peiceSelected, peices, cor, adversario):
        _, i, j = self.SelectPos((peices[peiceSelected][0][0], peices[peiceSelected][0][1]))
        posPeice = peices[peiceSelected][0]
        self.posibilityMove = []
        collisonPosition = None
        removePosition = None
        if cor == 0:
            #preto
            if j == 0:
                for p in peices:                    
                    if p[0] == self.campo[i+1][j+1][0]:
                        self.posibilityMove = []
                    else:
                        self.posibilityMove = [self.campo[i+1][j+1][0]]
            elif j == 7: 
                for p in peices:
                    if p[0] == [self.campo[i+1][j-1][0]]:
                        self.posibilityMove = []
                    else:
                        self.posibilityMove = [self.campo[i+1][j-1][0]]
            else:
                tem1 = False
                tem2 = False
                for p in peices:
                    if p[0] == self.campo[i+1][j-1][0]:
                        tem1 = True

                    if p[0] == self.campo[i+1][j+1][0]:
                        tem2 = True
                    
                if not tem1:
                    self.posibilityMove.append(self.campo[i+1][j-1][0])
                if not tem2:
                    self.posibilityMove.append(self.campo[i+1][j+1][0])

        elif cor == 1:
            #branco
            if j == 0:
                for p in peices:
                    if p[0] == [self.campo[i-1][j+1][0]]:
                        self.posibilityMove = []
                    else:
                        self.posibilityMove = [self.campo[i-1][j+1][0]]
            elif j == 7:
                for p in peices:
                    if p[0] == [self.campo[i-1][j-1][0]]:
                        self.posibilityMove = []
                    else:
                        self.posibilityMove = [self.campo[i-1][j-1][0]]
            else:
                tem1 = False
                tem2 = False
                for p in peices:
                    if p[0] == self.campo[i-1][j-1][0]:
                        tem1 = True

                    if p[0] == self.campo[i-1][j+1][0]:
                        tem2 = True
                    
                if not tem1:
                    self.posibilityMove.append(self.campo[i-1][j-1][0])
                if not tem2:
                    self.posibilityMove.append(self.campo[i-1][j+1][0])   

        for x in range(len(adversario)):
            if adversario[x][0] in self.posibilityMove:
                self.posibilityMove.remove(adversario[x][0])
                removePosition = adversario[x][0]
                eatPeice = self.Colission(posPeice, adversario[x][0], cor, i, j)
                canEat = True
                for a in adversario:
                    if eatPeice != None and a[0] == eatPeice:
                        canEat = False
                if canEat:
                    self.posibilityMove.append(eatPeice)
                    collisonPosition = eatPeice

        return self.posibilityMove, collisonPosition, removePosition

    def Move(self, peiceSelected, peices, posSelected, collisonPosition, removePosition):
        if peices == 0:
            self.pretas[peiceSelected][0] = posSelected
            if posSelected == collisonPosition:                
                for i in range(len(self.brancas)):
                    if self.brancas[i][0] == removePosition:
                        self.brancas.pop(i)
                        break
            if posSelected[1] == 400:
                self.pretas[peiceSelected][1] = self.DAMAPRETA
                self.pretas[peiceSelected][2] = True
                
        elif peices == 1:
            self.brancas[peiceSelected][0] = posSelected
            if posSelected == collisonPosition:
                for i in range(len(self.pretas)):
                    if self.pretas[i][0] == removePosition:
                        self.pretas.pop(i)
                        break
            if posSelected[1] == 50:
                self.brancas[peiceSelected][1] = self.DAMABRANCA
                self.brancas[peiceSelected][2] = True

    def ColissionDama(self, posPeice, posOpponent, cor, linha, coluna):
        if cor == 0:
            if posPeice[0] > posOpponent[0] and posPeice[1] < posOpponent[1]:
                try:
                    return self.campo[linha+2][coluna-2][0]
                except:
                    return None
            elif posPeice[0] < posOpponent[0] and posPeice[1] < posOpponent[1]:
                try:
                    return self.campo[linha+2][coluna+2][0]
                except:
                    return None
            elif posPeice[0] < posOpponent[0] and posPeice[1] > posOpponent[1]:
                try:
                    return self.campo[linha-2][coluna+2][0]
                except:
                    return None
            elif posPeice[0] > posOpponent[0] and posPeice[1] > posOpponent[1]:
                try:
                    return self.campo[linha-2][coluna-2][0]
                except:
                    return None

        elif cor == 1:
            if posPeice[0] > posOpponent[0] and posPeice[1] < posOpponent[1]:
                try:
                    return self.campo[linha+2][coluna-2][0]
                except:
                    return None
            elif posPeice[0] < posOpponent[0] and posPeice[1] < posOpponent[1]:
                try:
                    return self.campo[linha+2][coluna+2][0]
                except:
                    return None
            elif posPeice[0] < posOpponent[0] and posPeice[1] > posOpponent[1]:
                try:
                    return self.campo[linha-2][coluna+2][0]
                except:
                    return None
            elif posPeice[0] > posOpponent[0] and posPeice[1] > posOpponent[1]:
                try:
                    return self.campo[linha-2][coluna-2][0]
                except:
                    return None

    def MovePosibilityDama(self, peiceSelected, peices, cor, adversario):
        _, i, j = self.SelectPos((peices[peiceSelected][0][0], peices[peiceSelected][0][1]))
        posPeice = peices[peiceSelected][0]
        self.posibilityMove = []
        collisonPosition = None
        removePosition = None

        if cor == 0:
            print(i)
            #preto
            if j == 0:
                for p in peices:
                    if p[0] != self.campo[i+1][j+1][0]:
                        self.posibilityMove.append(self.campo[i+1][j+1][0])
                    
                    if i > 0 and p[0] == self.campo[i-1][j+1][0]:
                        pass
                    else:
                        self.posibilityMove.append(self.campo[i-1][j+1][0])
                            
            elif j == 7: 
                for p in peices:
                    if p[0] != [self.campo[i+1][j-1][0]]:
                        self.posibilityMove.append(self.campo[i+1][j-1][0])
                    
                    if i < 7 and p[0] == [self.campo[i-1][j-1][0]]:
                        pass
                    else:
                        self.posibilityMove.append(self.campo[i-1][j-1][0])
                        
            else:
                tem1 = False
                tem2 = False
                tem3 = False
                tem4 = False
                for p in peices:
                    if i != 7:
                        if p[0] == self.campo[i+1][j-1][0]:
                            tem1 = True

                        if p[0] == self.campo[i+1][j+1][0]:
                            tem2 = True

                    if i!=0:
                        if p[0] == self.campo[i-1][j-1][0]:
                            tem3 = True

                        if p[0] == self.campo[i-1][j+1][0]:
                            tem4 = True
                if i != 7:
                    if not tem1:
                        self.posibilityMove.append(self.campo[i+1][j-1][0])
                    if not tem2:
                        self.posibilityMove.append(self.campo[i+1][j+1][0])
                if i!=0:       
                    if not tem3:
                        self.posibilityMove.append(self.campo[i-1][j-1][0])
                    if not tem4:
                        self.posibilityMove.append(self.campo[i-1][j+1][0])

        elif cor == 1:
            #branco
            if j == 0:
                for p in peices:
                    if p[0] != [self.campo[i-1][j+1][0]]:                    
                        self.posibilityMove.append(self.campo[i-1][j+1][0])

                    if i > 0 and p[0] == [self.campo[i+1][j+1][0]]:
                        pass
                    else:
                        self.posibilityMove.append(self.campo[i+1][j+1][0])
            elif j == 7:
                for p in peices:
                    if p[0] != [self.campo[i-1][j-1][0]]:
                        self.posibilityMove.append(self.campo[i-1][j-1][0])
                    
                    if i < 7 and p[0] == [self.campo[i+1][j-1][0]]:
                        pass
                    else:
                        self.posibilityMove.append(self.campo[i+1][j-1][0])
            else:
                tem1 = False
                tem2 = False
                tem3 = False
                tem4 = False
                for p in peices:
                    if i!=0:
                        if p[0] == self.campo[i-1][j-1][0]:
                            tem1 = True

                        if p[0] == self.campo[i-1][j+1][0]:
                            tem2 = True

                    if i!=7:    
                        if p[0] == self.campo[i+1][j-1][0]:
                            tem3 = True

                        if p[0] == self.campo[i+1][j+1][0]:
                            tem4 = True
                if i!=0: 
                    if not tem1:
                        self.posibilityMove.append(self.campo[i-1][j-1][0])
                    if not tem2:
                        self.posibilityMove.append(self.campo[i-1][j+1][0])
                
                if i!=7:
                    if not tem3:
                        self.posibilityMove.append(self.campo[i+1][j-1][0])
                    if not tem4:
                        self.posibilityMove.append(self.campo[i+1][j+1][0]) 

        for x in range(len(adversario)):
            if adversario[x][0] in self.posibilityMove:
                self.posibilityMove.remove(adversario[x][0])
                removePosition = adversario[x][0]
                eatPeice = self.ColissionDama(posPeice, adversario[x][0], cor, i, j)
                canEat = True
                for a in adversario:
                    if eatPeice != None and a[0] == eatPeice:
                        canEat = False
                for p in peices:
                    if eatPeice != None and p[0] == eatPeice:
                        canEat = False

                if canEat:
                    self.posibilityMove.append(eatPeice)
                    collisonPosition = eatPeice

        return self.posibilityMove, collisonPosition, removePosition

    def Winner(self):
        if self.pretas == []:
            return False, 1
        elif self.brancas == []:                                                       
            return False, 0
        return True, None
    
    def main(self, con):
        pygame.init()   
        l = Listener(con)
        l.start()    
        winner = None
        while self.loop:
            self.window.fill((192,217,217))
            self.Field()
            self.Peices()
            self.window.blit(self.vezText, (0,455))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    #Selecionar posição para mover peça                    
                    if self.peiceSelected != None and self.posibilityMove != []:
                        if self.SelectPos(pygame.mouse.get_pos()) != None:
                            self.posSelected, _, _ = self.SelectPos(pygame.mouse.get_pos())
                        
                        if self.posibilityMove != None and self.posSelected in self.posibilityMove:
                            self.Move(self.peiceSelected, peices, self.posSelected, collisonPosition, removePosition)
                            self.peiceSelected = None
                            self.posSelected = None
                            if self.vez == 0:
                                self.vez = 1
                                if self.peiceColor == 1:
                                    self.vezText = self.YOURTURN
                                elif self.peiceColor == 0:
                                    self.vezText = self.WAIT
                            else:
                                self.vez = 0
                                if self.peiceColor == 1:
                                    self.vezText = self.WAIT
                                elif self.peiceColor == 0:
                                    self.vezText = self.YOURTURN

                            self.campo = [
                                            [[(50,50,50,50),  (150,150,150)], [(100,50,50,50),  (255,255,255)], [(150,50,50,50),  (150,150,150)], [(200,50,50,50),  (255,255,255)], [(250,50,50,50),  (150,150,150)], [(300,50,50,50),  (255,255,255)], [(350,50,50,50),  (150,150,150)], [(400,50,50,50),  (255,255,255)]],
                                            [[(50,100,50,50), (255,255,255)], [(100,100,50,50), (150,150,150)], [(150,100,50,50), (255,255,255)], [(200,100,50,50), (150,150,150)], [(250,100,50,50), (255,255,255)], [(300,100,50,50), (150,150,150)], [(350,100,50,50), (255,255,255)], [(400,100,50,50), (150,150,150)]],
                                            [[(50,150,50,50), (150,150,150)], [(100,150,50,50), (255,255,255)], [(150,150,50,50), (150,150,150)], [(200,150,50,50), (255,255,255)], [(250,150,50,50), (150,150,150)], [(300,150,50,50), (255,255,255)], [(350,150,50,50), (150,150,150)], [(400,150,50,50), (255,255,255)]],
                                            [[(50,200,50,50), (255,255,255)], [(100,200,50,50), (150,150,150)], [(150,200,50,50), (255,255,255)], [(200,200,50,50), (150,150,150)], [(250,200,50,50), (255,255,255)], [(300,200,50,50), (150,150,150)], [(350,200,50,50), (255,255,255)], [(400,200,50,50), (150,150,150)]],
                                            [[(50,250,50,50), (150,150,150)], [(100,250,50,50), (255,255,255)], [(150,250,50,50), (150,150,150)], [(200,250,50,50), (255,255,255)], [(250,250,50,50), (150,150,150)], [(300,250,50,50), (255,255,255)], [(350,250,50,50), (150,150,150)], [(400,250,50,50), (255,255,255)]],
                                            [[(50,300,50,50), (255,255,255)], [(100,300,50,50), (150,150,150)], [(150,300,50,50), (255,255,255)], [(200,300,50,50), (150,150,150)], [(250,300,50,50), (255,255,255)], [(300,300,50,50), (150,150,150)], [(350,300,50,50), (255,255,255)], [(400,300,50,50), (150,150,150)]],
                                            [[(50,350,50,50), (150,150,150)], [(100,350,50,50), (255,255,255)], [(150,350,50,50), (150,150,150)], [(200,350,50,50), (255,255,255)], [(250,350,50,50), (150,150,150)], [(300,350,50,50), (255,255,255)], [(350,350,50,50), (150,150,150)], [(400,350,50,50), (255,255,255)]],
                                            [[(50,400,50,50), (255,255,255)], [(100,400,50,50), (150,150,150)], [(150,400,50,50), (255,255,255)], [(200,400,50,50), (150,150,150)], [(250,400,50,50), (255,255,255)], [(300,400,50,50), (150,150,150)], [(350,400,50,50), (255,255,255)], [(400,400,50,50), (150,150,150)]],
                            ]
                            enviar = Enviar(self.pretas, self.brancas, self.vez)
                            con.send(bytes(pickle.dumps(enviar)))                        
                        else:
                            self.peiceSelected = None
                            self.posSelected = None
                            self.campo = [
                                            [[(50,50,50,50),  (150,150,150)], [(100,50,50,50),  (255,255,255)], [(150,50,50,50),  (150,150,150)], [(200,50,50,50),  (255,255,255)], [(250,50,50,50),  (150,150,150)], [(300,50,50,50),  (255,255,255)], [(350,50,50,50),  (150,150,150)], [(400,50,50,50),  (255,255,255)]],
                                            [[(50,100,50,50), (255,255,255)], [(100,100,50,50), (150,150,150)], [(150,100,50,50), (255,255,255)], [(200,100,50,50), (150,150,150)], [(250,100,50,50), (255,255,255)], [(300,100,50,50), (150,150,150)], [(350,100,50,50), (255,255,255)], [(400,100,50,50), (150,150,150)]],
                                            [[(50,150,50,50), (150,150,150)], [(100,150,50,50), (255,255,255)], [(150,150,50,50), (150,150,150)], [(200,150,50,50), (255,255,255)], [(250,150,50,50), (150,150,150)], [(300,150,50,50), (255,255,255)], [(350,150,50,50), (150,150,150)], [(400,150,50,50), (255,255,255)]],
                                            [[(50,200,50,50), (255,255,255)], [(100,200,50,50), (150,150,150)], [(150,200,50,50), (255,255,255)], [(200,200,50,50), (150,150,150)], [(250,200,50,50), (255,255,255)], [(300,200,50,50), (150,150,150)], [(350,200,50,50), (255,255,255)], [(400,200,50,50), (150,150,150)]],
                                            [[(50,250,50,50), (150,150,150)], [(100,250,50,50), (255,255,255)], [(150,250,50,50), (150,150,150)], [(200,250,50,50), (255,255,255)], [(250,250,50,50), (150,150,150)], [(300,250,50,50), (255,255,255)], [(350,250,50,50), (150,150,150)], [(400,250,50,50), (255,255,255)]],
                                            [[(50,300,50,50), (255,255,255)], [(100,300,50,50), (150,150,150)], [(150,300,50,50), (255,255,255)], [(200,300,50,50), (150,150,150)], [(250,300,50,50), (255,255,255)], [(300,300,50,50), (150,150,150)], [(350,300,50,50), (255,255,255)], [(400,300,50,50), (150,150,150)]],
                                            [[(50,350,50,50), (150,150,150)], [(100,350,50,50), (255,255,255)], [(150,350,50,50), (150,150,150)], [(200,350,50,50), (255,255,255)], [(250,350,50,50), (150,150,150)], [(300,350,50,50), (255,255,255)], [(350,350,50,50), (150,150,150)], [(400,350,50,50), (255,255,255)]],
                                            [[(50,400,50,50), (255,255,255)], [(100,400,50,50), (150,150,150)], [(150,400,50,50), (255,255,255)], [(200,400,50,50), (150,150,150)], [(250,400,50,50), (255,255,255)], [(300,400,50,50), (150,150,150)], [(350,400,50,50), (255,255,255)], [(400,400,50,50), (150,150,150)]],
                            ]
                                            
                    #Selecionar peça
                    else:                
                        self.peiceSelected, peices = self.SelectPeice(pygame.mouse.get_pos())
                        if self.vez == 0 and peices != 0:
                            self.peiceSelected = None
                        if self.vez == 1 and peices != 1:
                            self.peiceSelected = None
                            
                        if self.peiceSelected != None:
                            self.changeColorSelectedPeice(peices, self.peiceSelected)
                            if peices == 0:
                                if self.pretas[self.peiceSelected][2]:
                                    self.posibilityMove, collisonPosition, removePosition = self.MovePosibilityDama(self.peiceSelected, self.pretas, peices, self.brancas)                    
                                else:
                                    self.posibilityMove, collisonPosition, removePosition = self.MovePosibility(self.peiceSelected, self.pretas, peices, self.brancas)                    
                            elif peices == 1:
                                if self.brancas[self.peiceSelected][2]:
                                    self.posibilityMove, collisonPosition, removePosition = self.MovePosibilityDama(self.peiceSelected, self.brancas, peices, self.pretas)
                                else:
                                    self.posibilityMove, collisonPosition, removePosition = self.MovePosibility(self.peiceSelected, self.brancas, peices, self.pretas)

            if not q.empty():
                self.UpdateParameter()

            self.loop, winner = self.Winner()
            pygame.display.update()
            self.clock.tick(30)
        return winner