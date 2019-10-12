import listTransfer as lt
import peripheralControl as pc

def overrideESG():
    lt.putMutexExt(0)
    if(lt.getMutex() == 1):
        pc.acceptProtocol()
    lt.putMutexExt(1)


def putMutexExt(a):
    ref.update({'MutexExt' : a})
