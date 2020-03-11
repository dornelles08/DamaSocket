from queue import Queue

q = Queue()

q.put([1,2,3])
q.put([4,5,6])
q.put(0)

print(q.get())
print(q.get())
print(q.empty())

print("Tamanho: {}".format(q.qsize()))