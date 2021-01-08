import time
import threading

LIST_SIZE = 100000

class Counter():
    def __init__(self,lockEnabled):
        self.lockEnabled = lockEnabled
        self.lock = threading.Lock()
        self.count = 0
    def addValue(self,value):
        if self.lockEnabled:
            with self.lock:
                self.count += value
        else:
             self.count += value



addList = list(range(LIST_SIZE))
print("Actual value: {}".format(sum(addList)))

def worker():
    while len(addList) > 0:
        try:
            addAmount = addList.pop()                
            counter.addValue(addAmount)
            
            
        except:
            pass
        
    return
        

counter = Counter(False)
    
threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print("Counter No Lock value: {}".format(counter.count))

counter = Counter(True)
addList = list(range(LIST_SIZE))
    
threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print("Counter Lock value: {}".format(counter.count))

print("test")








