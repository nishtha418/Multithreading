import numpy as np
import threading
import time
import psutil
import matplotlib.pyplot as plt
import multiprocessing

# PARAMETERS 
NUM_MATRICES = 200
SIZE = 700

# Generate matrices
matrices = [np.random.rand(SIZE, SIZE) for _ in range(NUM_MATRICES)]
constant_matrix = np.random.rand(SIZE, SIZE)

#  WORKER FUNCTION 
def multiply_chunk(start, end):
    for i in range(start, end):
        _ = np.dot(matrices[i], constant_matrix)  # store result to avoid optimization

#  THREAD RUNNER 
def run_threads(num_threads):
    threads = []
    chunk_size = NUM_MATRICES // num_threads

    start_time = time.time()

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else NUM_MATRICES

        t = threading.Thread(target=multiply_chunk, args=(start, end))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return time.time() - start_time

#  MAIN 
if __name__ == "__main__":

    max_threads = multiprocessing.cpu_count() * 2

    thread_counts = []
    times = []
    cpu_usages = []

    print(f"CPU Cores: {multiprocessing.cpu_count()}\n")

    for t in range(1, max_threads + 1):
        print(f"Running with {t} threads...")

        cpu_before = psutil.cpu_percent(interval=None)

        time_taken = run_threads(t)

        cpu_after = psutil.cpu_percent(interval=None)

        avg_cpu = (cpu_before + cpu_after) / 2

        thread_counts.append(t)
        times.append(time_taken)
        cpu_usages.append(avg_cpu)

        print(f"Time: {round(time_taken, 2)} sec | CPU: {avg_cpu}%\n")

    #  PRINT TABLE
    print("\nThread vs Time Table:")
    for t, time_val in zip(thread_counts, times):
        print(f"T={t} -> {round(time_val, 2)} sec")

    # PLOT TIME GRAPH
    plt.figure()
    plt.plot(thread_counts, times, marker='o')
    plt.xlabel("Number of Threads")
    plt.ylabel("Time (seconds)")
    plt.title("Thread vs Execution Time")

    #PLOT CPU GRAPH 
    plt.figure()
    plt.plot(thread_counts, cpu_usages, marker='o')
    plt.xlabel("Number of Threads")
    plt.ylabel("CPU Usage (%)")
    plt.title("Thread vs CPU Usage")

    plt.show()     