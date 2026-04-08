import threading
import random
import time
import tkinter as tk
import psutil

# Shared values
values = [0] * 6
cpu_usage = 0

# -------- TASK FUNCTION --------
def task(index, lb, ub, refresh_time, run_time):
    start = time.time()

    while time.time() - start < run_time:
        values[index] = random.randint(lb, ub)
        time.sleep(refresh_time)

# -------- CPU MONITOR --------
def monitor_cpu(run_time):
    global cpu_usage
    start = time.time()

    while time.time() - start < run_time:
        cpu_usage = psutil.cpu_percent(interval=1)

# -------- GUI UPDATE FUNCTION --------
def update_labels():
    for i in range(6):
        labels[i].config(text=str(values[i]))

    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")

    root.after(500, update_labels)

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
        threading.Thread(target=monitor_cpu, args=(run_time,))
    ]

    for t in threads:
        t.start()

    # -------- GUI --------
    root = tk.Tk()
    root.title("Multithreading Dashboard")

    labels = []
    colors = ["yellow", "lightblue", "lightgreen", "orange", "pink", "white"]

    for i in range(6):
        label = tk.Label(root, text="0", font=("Arial", 20),
                         width=10, height=3, bg=colors[i])
        label.grid(row=i//2, column=i%2, padx=20, pady=20)
        labels.append(label)

    # CPU Label
    cpu_label = tk.Label(root, text="CPU Usage: 0%", font=("Arial", 14))
    cpu_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Start GUI updates
    update_labels()

    root.mainloop()