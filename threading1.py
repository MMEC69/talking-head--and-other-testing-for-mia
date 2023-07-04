import args as args
from Demos.win32cred_demo import target

import threading1

t1 = threading.Thread(target, args)
t2 = threading.Thread(target, args)

t1.start()
t2.start()

t1.join()
t2.join()

