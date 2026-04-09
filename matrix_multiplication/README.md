# Matrix Multiplication using Multithreading

This project demonstrates the use of multithreading for performing matrix multiplication in Python and analyzes its performance.

## Objective
- Multiply multiple random matrices with a constant matrix
- Execute using different numbers of threads
- Measure execution time and CPU usage
- Analyze performance behavior

## Parameters
- Number of matrices: 200
- Matrix size: 700 × 700
- Threads tested: 1 to 2 × number of CPU cores

## Features
- Multithreaded matrix multiplication
- Execution time analysis
- CPU usage monitoring
- Graph visualization

## Results
- Initial increase in threads reduces execution time
- After a certain point, performance plateaus or degrades
- This is due to Python’s Global Interpreter Lock (GIL)

## Technologies Used
- Python
- NumPy
- Threading
- Matplotlib
- psutil

## Conclusion
Multithreading is not effective for CPU-bound tasks in Python due to GIL limitations. Optimal performance is achieved with a limited number of threads.
