# each program in an os is a separate process. Each process has one or more threads
# If a process has several threads, they appear to run simultaneously

# processes can't communicate with each other
# threads can (have access to the same memory)

import subprocess
# subprocess.call

# The threading module
# complexity arises when we want to separate threads. Since they share data, we need to be careful with a policy for locks
# to create multiple threads using threading.thread() method passes a callable object

import threading
def worker(num):
	'''thread worker function'''
	print('Worker: {}'.format(num))
	return 

threads = []
for i in range(5):
	t = threading.Thread(target=worker, args=(i,))
	threads.append(t)
	t.start()

# we can also use the queue.queue() class to handle all the locking internally. 
# this will serialize access, meaning that only one thread at a time has access to the data (this is the FIFO model)
# Since the program will not terminate while there are running threads, the one ones that are finished will appear to still be running.
# in this case, the program terminates as soon as there are no daemon threads running

#Mutexes
	# a mutex is like a lock. Mutexes are used in parallel programming to ensure that only one thread can access a shared resource at a time
	# for example, say one thread is modifying an array:
		# When it has gotten halfway through the array, the processor switches to another thread. 
		# if we were not using mutexes, the thread could try to modify the array as well, at the same time
	# conceptually, a mutex is an integer that starts at 1. Whenever a thread needs to alter the array, it 'locks' the mutex
	# This causes the thread to wait until the number is positive and then decreases it by one
	# When the thread is done modifying the array, it 'unlocks' the mutex, causing the number to increase by 1

	#Semaphores
	# more general than mutexes. 
	# A semaphore's integer may start at a number greater than 1. 
	# the number at which the semaphore starts is the number of threads that may access the resource at once. 
	# semaphores support 'wait' and 'signal' operations. which are analogous to the 'lock' and 'unlock' operations of mutexes

	# Deadlock
		# a problem that sometimes arises in parallel programming, when two threads are stuck indefinitely.
		# We can prevent deadlock if we assign an order to our locks and require that locks will always be acquired in order (this is a very general and a not precise approach)

	# Spinlock
		# a form of 'busy waiting', that can be useful for high-performance computing (HPC - when the entire system is dedicated to a single application and exactly one thread per core). 
		# It takes less time than a semaphore.
		
