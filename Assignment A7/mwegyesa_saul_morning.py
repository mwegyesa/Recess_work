                   #CONTEXT MANAGER
                   
"""Context managers are used to properly manage resources and ensure that they are 
properly initialized and released, even in the presence of exceptions.
They provide a convenient and reliable way to handle common programming patterns
such as opening and closing files, acquiring and releasing locks, 
connecting and disconnecting from databases, and more."""

              #Context manager implementation in file handling
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

# Usage:
with FileManager("comrade.txt", "w") as file:
    file.write("How are you!")
    
    
             #MULTI THREADING
"""Multi-threading in Python allows you to perform concurrent execution of multiple threads
within a single process.
It enables you to run multiple threads of execution simultaneously, leveraging
the capabilities of modern processors with multiple cores or executing
tasks concurrently while waiting for I/O operations."""
 
             #IMPLEMENTATION
import threading

def task(index):
    # Code to be executed by the thread
    print(f"Thread {index} started")

# Number of threads to create
num_threads = 5

# Create a list to hold the thread objects
threads = []

# Create and start the threads
for i in range(num_threads):
    thread = threading.Thread(target=task, args=(i,))
    thread.start()
    threads.append(thread)

#Wait for all the threads to complete
for thread in threads:
    thread.join()

print("All threads completed")
                        
                        
                        #MULTI PROCESSING
import multiprocessing

def process (name):
    print(f"Running {name}")
    
#Loop for the processes
pool=multiprocessing.Pool(processes=5)

#Sending tasks into the pool
for i in range(5):
    pool.apply_async(process,args=(f"Process {i}",))


#closing the pool and waiting for all processes to finish
pool.close()
pool.join()
                        
                        
                    
