'''
- share the same data space with the main thread and can therefore share information or communicate with each other more easily
- light-weight processes and they do not require much memory overhead

Ref:    https://docs.python.org/3/library/threading.html
        https://docs.python.org/3/library/_thread.html#module-_thread

In CPython, due to the Global Interpreter Lock, only one thread can execute Python code at once 
(even though certain performance-oriented libraries might overcome this limitation). 
If you want your application to make better use of the computational resources of multi-core machines, 
you are advised to use multiprocessing or concurrent.futures.ProcessPoolExecutor. 
However, threading is still an appropriate model if you want to run multiple I/O-bound tasks simultaneously.
'''

#Method 1
import threading
import time

count1 = 0
count2 = 0
def even(thread_name):
    global count1
    local_data = threading.local()

    while count1 < 10:
        if count1 % 2 == 0:
            local_data.name = thread_name
            print(local_data.name + ": \t", count1, "\t", threading.get_native_id(), "\t",threading.get_ident())
            # time.sleep(.5)
        count1 = count1 + 1

def odd(thread_name):
    global count2
    local_data = threading.local()

    while count2 < 10:
        if count2 % 2 != 0:
            local_data.name = thread_name
            print(local_data.name + ": \t", count2, "\t", threading.get_native_id(), "\t",threading.get_ident())
            # time.sleep(.5)
        count2 = count2 + 1
        

'''
Basic Thread creation.
'''

'''
Ref Thread object:https://docs.python.org/3/library/threading.html#thread-objects
'''
thread1 = threading.Thread(target=even, args=("Even",), name="test1")
thread2 = threading.Thread(target=odd, args=("Odd",), name="test2")

'''
It must be called at most once per thread object. 
It arranges for the object’s run() method to be invoked in a separate thread of control.
'''
thread1.start() 
thread2.start()

# print(thread1.getName(),"\t", thread2.getName())

'''
This blocks the calling thread until the thread whose join() method is called terminates 
– either normally or through an unhandled exception – or until the optional timeout occurs.
A thread can be join()ed many times
'''
thread1.join()  
thread2.join()

print("Done.")

#*************************************************************
#Method 2
#import threading

count = 0
class MyThread():
    def even(self, thread_name):
        global count
        while count < 10:
            if count % 2 == 0:
                print(thread_name + ": \t", count)
            count = count + 1

obj = MyThread()
thread = threading.Thread(target=obj.even, args=("Even",), name="EvenThread")
thread.start()
thread.join()
print("Done.")

#*************************************************************
#Method 3
# import threading

count = 0
class MyThread1(threading.Thread):
    def __init__(self,thread_name):
        super(MyThread1, self).__init__(args=(thread_name,), name=thread_name)
        self.thread_name = thread_name

    def run(self):
        global count
        while count < 10:
            if count % 2 == 0:
                print(self.thread_name + ": \t", count)
            count = count + 1

thread = MyThread1("even")
thread.start()
thread.join()
print("Done.")



