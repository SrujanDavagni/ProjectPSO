# ProjectPSO
This project proposes a Particle Swarm Optimization (PSO)-based intelligent traffic management system aimed at minimizing traffic congestion and optimizing signal timings. By integrating V2X (Vehicle-to-Everything) communication, the system ensures real-time data exchange between vehicles, roadside units, and the control center.

Project Structure
    |
    |--yolodetection.ipynb
    |--README.md

Features
    Collects live traffic statistics via sensors and V2X inputs. 
    Computes optimal green light durations for each junction.
    Updates signal timings dynamically based on PSO results.

Technologies Used
    Python 3.x
    pyswarm
    ultralytics
    cv2
    matplotlib

Installation
    pip install pyswarm
    Or inside Jupyter Notebook:
    !pip install pyswarm

    #Running
    1.Launch Jupyter Notebook: cd E:\ProjectPSO(Your Specific folder) jupyter notebook 
    2.Open yolodetection.ipynb. 
    3.Run each cell step by step.