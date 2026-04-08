import threading
import random
import time
import tkinter as tk

# Shared values
values = [0] * 6

# -------- TASK FUNCTION --------
def task(index, lb, ub, refresh_time, run_time):
    start = time.time()

    while time.time() - start < run_time:
        values[index] = random.randint(lb, ub)
        time.sleep(refresh_time)

# -------- GUI UPDATE FUNCTION --------
def update_labels():
    for i in range(6):
        labels[i].config(text=str(values[i]))
    root.after(500, update_labels)  # refresh every 0.5 sec

# -------- MAIN --------
if __name__ == "__main__":

    run_time = 60

    # Start threads
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

    # -------- CREATE GUI --------
    root = tk.Tk()
    root.title("Multithreading Random Numbers")

    labels = []

    colors = ["yellow", "lightblue", "lightgreen", "orange", "pink", "white"]

    for i in range(6):
        label = tk.Label(root, text="0", font=("Arial", 20), width=10, height=3, bg=colors[i])
        label.grid(row=i//2, column=i%2, padx=20, pady=20)
        labels.append(label)

    # Start updating GUI
    update_labels()

    root.mainloop()