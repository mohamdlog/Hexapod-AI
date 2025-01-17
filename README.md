# Hexapod-AI

<img src='assets/Hexapod.png' width='50%'/>

## Welcome
This project is designed to provide the following features and capabilities:

1. **Operate Entirely in Headless Mode**  
The system is built to function without requiring a graphical user interface, including the server.

2. **Develop a Custom CLI-Friendly Client**  
A custom command-line interface (CLI) client. Key functionalities include:
   - Controlling the spider’s behavior.
   - Monitoring system status and logs.
   - Retrieving or managing scene recording data.

3. **ROS2 for Communication and Control**  
ROS2 (Robot Operating System 2) is the backbone of the system’s communication. It provides support for:
   - **Node-Based Architecture:** The spider, obstacle detection, and data recording each run as independent ROS2 nodes.
   - **Inter-Node Communication:** Nodes use ROS2 topics and services to share data, such as movement commands, obstacle sensor readings, and scene recording updates.

4. **Simulate Spider Movements with Obstacle Avoidance and Scene Recording**  
The focus is to simulate a spider capable of dynamic movement and environment interaction:
   - **Random Walk:** A pseudo-random algorithm guides the spider’s movements.
   - **Obstacle Avoidance:** The spider identifies and navigate around obstacles.
   - **Scene Recording:** The system captures and stores environmental data, movement paths, and interaction details using ROS2’s data management tools. This information is used for machine learning.

5. **Expand Compatibility to Other Hexapod Robots**  
While initially focused on the Freenove Hexapod, the goal is to build an adaptable framework that can work with other hexapod robots as well.

## Prerequisites
- [Freenove Hexapod](https://www.amazon.com/Freenove-Big-Hexapod-Robot-Kit-Raspberry-Pi-Balancing-Recognition-Ultrasonic/dp/B08M5DXS2P?crid=3KV2K72VN8OIK&dib=eyJ2IjoiMSJ9.hyUjFCpcxtDvB6cSLdESXZvB2Vyu2BZE702Opav_4pw362Y-leX2nhRihGUpyvatdfUFLYhrkhYVxXUzxyAaLYfVc6g1PVaMHt4uJv-dwMYlmFLEGvaQ66BU7SMynz0brOpnYqBRpgNcHqetpvmbAYEbJFhWCXfYBug0f2YO52OM-B7dpcoSzVk0aRrdsl8ctKsNe2Z-5jhl1crJfvMoAoC_Rb0cIi2KP_QZGddGFhQDT2tlPQ7p6cW_mbHIsw2SRd_kYq8g11BzwAtgp8MguQXNNt87BzRrXcaZ3WkcEdLDOFxf6ls9B6-_Yfo1_SkcWOprh6HFUTzrcMW271oe0_Pxq7GHw0h3ORTjLPz_pTlnpLJPJwS5Xsgi3Srrqcr_.Z9MeEfegRmxxC1aoamTnySzmuAeN6PyndgJWAVI4-uA&dib_tag=se&keywords=freenove+hexapod&qid=1737096509&s=electronics&sprefix=freenove+hexapod%2Celectronics%2C87&sr=1-1_)
- [Ubuntu for Raspberry Pi](https://ubuntu.com/download/raspberry-pi/thank-you?version=24.04.1&architecture=server-arm64+raspi)


## Setup
1. In the root of the project, run the setup script: 
    ```bash
    python setup.py
    ```
2. Create a virtual envirnment:
    ```bash
    python -m venv venv
    ```
3. Activate the virtual enviornment:
    ```bash
    source venv/bin/activate
    ```
4. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Tips
- If sudo elevation is needed, run:
    ```bash
    sudo /path/to/Hexapod-AI/venv/bin/python script.py
    ```
    This will use the virtual environment's Python interpreter.

- Follow this [tutorial](assets/Tutorial.pdf) for setup and testing.

- To calibrate the spider, download the appropriate client from the original repository. It is compatible with the server.