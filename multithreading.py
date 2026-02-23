#multi threading

#dividing a program into to run subprogram
#using Thread we can run parallel
import threading
import time

def tables1(n):
    print(threading.current_thread().name)
    for r in range(1,11):
        time.sleep(2)
        print(n*r)
        
def tables2(n):
    for r in range(1,11):
        print(n*r)
def tables3(n):
    for r in range(1,11):
        print(n*r)

#tables1(5)
#tables2(6)

'''t1=threading.Thread(target=tables1, args=(5,))
t1.start()
t2=threading.Thread(target=tables1, args=(6,))
t3=threading.Thread(target=tables1, args=(10,))t2.start()
t3.start()'''
''''''
#join method(use to control the execution of the Thread)
'''t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
'''
'''t1=threading.Thread(target=tables1,args=(5,),name="my_5_table")
t1.start()
t2=threading.Thread(target=tables2,args=(6,),name="my_6_table")
t2.start()
t3=threading.Thread(target=tables3,args=(6,),name="my_7_table")
t3.start()'''

#daemon will exceute in the background 
def mydaemon():
    print("hello")
    for r in range(1,11):
        print(5*r)
t1=threading.Thread(target=mydaemon,daemon=True)
t1.start()
