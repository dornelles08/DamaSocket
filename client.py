import socket
from drawField import Dama

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#enviando nome do arquivo
dest = ('127.0.0.1', 5000)
tcp.connect(dest)


msg = tcp.recv(1024)
tcp.close()

msg = msg.decode("utf-8")

if msg == "Esperando Adversario":
    print(msg)
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('127.0.0.1', 5050))
    tcp.listen(1)
    con, adversario = tcp.accept()
    msg = con.recv(1024)
    print("Recebida: {}".format(msg.decode('utf-8')))
    a = Dama(1)
    a.main(con)
    con.close()

else:
    print("Adversario: "+msg)
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((msg, 5050))
    tcp.send(bytes("Olá", 'utf-8'))
    a = Dama(0)
    a.main(tcp)
    tcp.close()
    
