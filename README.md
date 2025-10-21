# PSO-Based Traffic Optimization System with V2X Communication

Optimize traffic signal timings using **Particle Swarm Optimization (PSO)** and **V2X (Vehicle-to-Everything)** communication.  
This project enhances urban mobility by dynamically adjusting signal durations based on real-time traffic flow data, contributing to **UN SDG Goal 9 — Industry, Innovation, and Infrastructure**.

---

## Project Structure

E:\ProjectPSO
├── main.py # Core PSO optimization algorithm
├── simulation.py # SUMO or traffic simulation interface
├── v2x_module.py # Handles V2X communication layer
├── requirements.txt # Required dependencies
├── README.md # Project documentation
---

## Features

- Real-time traffic data acquisition via V2X-enabled sensors  
- Adaptive traffic signal control using PSO algorithm  
- Dynamic adjustment of green and red light durations  
- Vehicle-to-Vehicle (V2V) and Vehicle-to-Infrastructure (V2I) data exchange  
- Improved average throughput and reduced waiting time  
- Visualization of optimized traffic flow using simulation tools  

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

3. **V2X Communication**  
   - Vehicles and infrastructure share data through **V2V**, **V2I**, and **V2N** channels.  
   - The controller updates signals based on real-time inputs from connected vehicles.  

---

## Technologies Used

- **Python 3.x**  
- [NumPy](https://numpy.org/) — PSO computation  
- [Flask / FastAPI](https://fastapi.tiangolo.com/) — Backend API  
- [MongoDB / Firebase](https://www.mongodb.com/) — Data storage  
- [SUMO](https://www.eclipse.org/sumo/) — Traffic simulation  
- [MQTT / VANET Protocols](https://mqtt.org/) — V2X communication layer  
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