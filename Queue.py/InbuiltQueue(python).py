#q.size()= Number of elements in queue
#empty() = it's check whether queue is empty or not
#full() = It's check whether queue is full or not
#get() = Dequeue the front element
# or
# Number of element in queue it wait's for someone to enter  the elements in enqueue then it's dequeue
#get_nowait() = ever empty exception
# put() = enqueue the elements until we get the max size
# or
# It wait to someone to enqueue the element
#put_nowait = Full exception
from queue import Queue
from queue import LifoQueue
q = Queue(maxsize=10)
q.put(20)
q.put(2)
q.put(3)
q.put(7)
q.put(9)
q.put(11)
q.put(6)
q.put(8)
q.put(3)
q.put(1)
print(q.empty())
print(q.full())
print(q.qsize())
while(q.empty() is False):
    print(q.get())

print("--------------------------------------------------")
q1 = LifoQueue()

q1.put(20)
q1.put(3)
q1.put(4)
q1.put(55)
q1.put(67)
while(q1.empty() is False):
    print(q1.get())