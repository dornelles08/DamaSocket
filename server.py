import socket
from queue import Queue
from threading import Thread


class Conexao(Thread):
    def __init__(self, cliente, con):
        Thread.__init__(self)
        self.cliente = cliente
        self.con = con
    
    def run(self):
        print('Concetado por', self.cliente)
        if q.empty():
            q.put(cliente[0])
            self.con.send(bytes("Esperando Adversario", 'utf-8'))
        else:
            self.con.send(bytes(str(q.get()), 'utf-8'))

q = Queue()
HOST = '127.0.0.1'
PORT = 5000            
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(5)
while True:
    # recebendo nome o arquivo
    con, cliente = tcp.accept()
    proximo = Conexao(cliente, con).start()