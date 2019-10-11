import peripheralControl as peri
import cloudModule as cloud
import Contact
import recog
import ultra

def start():
	try:
		l = recog.begin()
		if(l[1] == False):
			peri.rejectProtocol()
			Contact.sendInfo()
			# enABLE CLOUD OVERRIDE
		else:
			print(l)
			peri.acceptProtocol()
			hault()
		cloud.cloudProtocol()
		# Halt Exec
	except Exception:
		print("CHECK internet connection or loose wiring!!")
	finally:
		stop()
	
def stop():
	peri.rejectProtocol()
	cloud.putMutex(0)
	
def hault():
	while(cloud.getMutex() == 0):
		if(ultra.distance() > 50):
			reset()
		time.sleep(1)
	
'''Cloud functions'''

def cloudOverride():
	putExtMutex(0)
	for i in range(8):
		if(getMutex() == 0):
			time.sleep(2)
			continue
		elif(getMutex() == 1):
			acceptProtocol()
			break
		else: # Mutex == 3
			face_rec.reset()
	putExtMutex(1)
	
def getMutex():
	pass

def putExtMutex(val):
	pass
