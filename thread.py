import threading

def fazSistemas():
	return conta != 0
def fazDistribuidos():
	return contb != 0
def fazMjoaojr():
	return contc != 0

def Sistemas():
	for i in (10):
		with cv:
			print("SISTEMAS ")
			conta+=1
			cv.wait_for(fazSistemas)
			cv.notify_all()
def Distribuidos():
	for i in (10):
		with cv:
			print("DISTRIBUIDOS_")	
			contb+=1
			cv.wait_for(fazDistribuidos)
			contc = 0
			cv.notify_all()

def Mjoaojr():
	for i in (10):
		with cv:
			print("MJOAOJR")
			contc+=1
			cv.wait_for(fazMjoaojr)
			conta = 0
			contb = 0
			c.notify_all()
global conta 
global contb 
global contc 

conta = 0
contb = 0
contc = 0			
cv = threading.Condition ()

threads = []
threads.append(threading.Thread(target=Sistemas))
threads.append(threading.Thread(target=Distribuidos))
threads.append(threading.Thread(target=Mjoaojr))

for t  in threads:
	t.start()

for t  in threads:
	t.join()
