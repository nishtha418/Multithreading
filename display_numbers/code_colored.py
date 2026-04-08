from colorama import Fore, Back, Style, init
init(autoreset=True)

import threading
import random
import time
import os

# Shared data
values = [0] * 6

# -------- TASK FUNCTION --------
def task(index, lb, ub, refresh_time, run_time):
    start = time.time()

    while time.time() - start < run_time:
        values[index] = random.randint(lb, ub)
        time.sleep(refresh_time)

# -------- DISPLAY FUNCTION --------
def display(run_time):
    start = time.time()

    while time.time() - start < run_time:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n")

        print(Back.LIGHTYELLOW_EX + Fore.BLACK + f"   {values[0]:^8}   " + Style.RESET_ALL + "    " +
              Back.LIGHTBLUE_EX + Fore.BLACK + f"   {values[1]:^8}   ")
        print("[10,20] rt=10      [-10,10] rt=20\n")

        print(Back.LIGHTGREEN_EX + Fore.BLACK + f"   {values[2]:^8}   " + Style.RESET_ALL + "    " +
              Back.YELLOW + Fore.BLACK + f"   {values[3]:^8}   ")
        print("[-100,0] rt=8      [0,20] rt=12\n")

        print(Back.LIGHTMAGENTA_EX + Fore.BLACK + f"   {values[4]:^8}   " + Style.RESET_ALL + "    " +
              Back.WHITE + Fore.BLACK + f"   {values[5]:^8}   ")
        print("[-40,40] rt=16     [100,200] rt=14\n")

        time.sleep(1)

    print("\nProgram finished after 60 seconds.")

# -------- MAIN --------
if __name__ == "__main__":

    run_time = 60

    threads = [
        threading.Thread(target=task, args=(0, 10, 20, 10, run_time)),
        threading.Thread(target=task, args=(1, -10, 10, 20, run_time)),
        threading.Thread(target=task, args=(2, -100, 0, 8, run_time)),
        threading.Thread(target=task, args=(3, 0, 20, 12, run_time)),
        threading.Thread(target=task, args=(4, -40, 40, 16, run_time)),
        threading.Thread(target=task, args=(5, 100, 200, 14, run_time)),
    ]

    for t in threads:
        t.start()

    display(run_time)

    for t in threads:
        t.join()