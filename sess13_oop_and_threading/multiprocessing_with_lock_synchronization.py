# Python script to demonstrate how to safely increment a shared integer variable among multiple processes
# using multiprocessing and locking

# Import the required module(s)
import multiprocessing as mp

# Function to increment a shared value using a lock
def increment_shared_value_with_lock(shared_value, lock):
    for _ in range(1000000):
        with lock:
            shared_value.value += 1

if __name__ == '__main__':
    # Create a shared integer value and a lock
    shared_value = mp.Value('i', 0)
    lock = mp.Lock()

    # Create 5 processes (threads) each incrementing the shared value using the lock
    processes = [mp.Process(target=increment_shared_value_with_lock, args=(shared_value, lock)) for _ in range(5)]

    # Start all the processes
    for p in processes:
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    print(f"Final shared value (with lock): {shared_value.value}")