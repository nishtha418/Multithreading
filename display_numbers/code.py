import threading
import random
import time
import os

# Shared data (6 positions)
values = [0] * 6

# TASK FUNCTION 
def task(index, lb, ub, refresh_time):
    while True:
        values[index] = random.randint(lb, ub)
        time.sleep(refresh_time)

# DISPLAY FUNCTION 
def display():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # clear screen

        print("\n")

        print(f" {values[0]:^10}        {values[1]:^10}")
        print("[10,20] rt=10     [-10,10] rt=20\n")

        print(f" {values[2]:^10}        {values[3]:^10}")
        print("[-100,0] rt=8     [0,20] rt=12\n")

        print(f" {values[4]:^10}        {values[5]:^10}")
        print("[-40,40] rt=16    [100,200] rt=14\n")

        time.sleep(1)  # refresh screen every second

#  MAIN 
if __name__ == "__main__":

    # Create 6 threads
    threads = [
        threading.Thread(target=task, args=(0, 10, 20, 10)),
        threading.Thread(target=task, args=(1, -10, 10, 20)),
        threading.Thread(target=task, args=(2, -100, 0, 8)),
        threading.Thread(target=task, args=(3, 0, 20, 12)),
        threading.Thread(target=task, args=(4, -40, 40, 16)),
        threading.Thread(target=task, args=(5, 100, 200, 14)),
    ]

    # Start all threads
    for t in threads:
        t.daemon = True  # so program can exit
        t.start()

    # Start display
    display()