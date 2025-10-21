# PSO-Based Traffic Optimization System with V2X Communication

Optimize traffic signal timings using **Particle Swarm Optimization (PSO)** and **V2X (Vehicle-to-Everything)** communication.  
This project enhances urban mobility by dynamically adjusting signal durations based on real-time traffic flow data, contributing to **UN SDG Goal 9 — Industry, Innovation, and Infrastructure**.

---

## Project Structure

E:\ProjectPSO
├── yolodetection.py # Core PSO optimization algorithm
├── README.md # Project documentation
---

## Features

- Real-time traffic data acquisition via V2X-enabled sensors  
- Adaptive traffic signal control using PSO algorithm  
- Dynamic adjustment of green and red light durations

---

## Working Principle

1. **Data Collection**  
   - Gather live traffic data: vehicle count, density, and queue length.  
   - Preprocess and normalize the data for the PSO model.  

2. **PSO Optimization**  
   - Each particle represents a possible traffic light timing configuration.  
   - The fitness function minimizes average waiting time and queue length.  
   - PSO updates particles using:
     ```
     v[i] = w*v[i] + c1*r1*(pbest[i] - x[i]) + c2*r2*(gbest - x[i])
     x[i] = x[i] + v[i]
     ```
   - The best configuration (gbest) is selected and sent to the signal controller.  

---

## Technologies Used

- **Python 3.x**  
- [NumPy](https://numpy.org/) — PSO computation
- [Matplotlib](https://matplotlib.org/) — Visualization  

---

## Installation

Install required dependencies:

```bash
pip install numpy flask pymongo paho-mqtt matplotlib
Running the Project

Navigate to your project directory:

cd E:\ProjectPSO


Run the main optimization script:

python yolodetection.py
Observe optimized signal timings and performance metrics on the Console.

Evaluation Metrics

Average waiting time per vehicle

Average queue length per intersection

Total throughput improvement

Signal response efficiency