# Autonomous-rover-with-visualslam-ros2-rpi5

<p align="center">
  <img src="IMG_20260505_151202006.jpg.jpeg" width="650"/>
</p>

## Overview
Autonomous rover platform built using ROS 2 and Raspberry Pi 5 featuring camera-based SLAM, real-time mapping, navigation, motor control, and computer vision for intelligent robotic exploration.

This project focuses on developing a low-cost intelligent robotic rover capable of:
- Visual depth estimation
- Pseudo 3D terrain mapping
- Camera-based environmental perception
- Autonomous robotic navigation
- Real-time obstacle understanding

---

# Features

- ROS2 based robotic architecture
- Raspberry Pi 5 integration
- Camera-based visual SLAM
- Real-time depth sensing
- Pseudo 3D contour mapping
- PWM motor control
- OpenCV computer vision pipeline
- Autonomous exploration framework

---

# Hardware Used

- Raspberry Pi 5
- Motor Driver Module
- DC Geared Motors
- USB Camera
- Rover Chassis
- Power Supply Module

---

# Software Stack

- ROS 2
- Python
- OpenCV
- NumPy
- SLAM Toolbox

---
# Visual Depth Estimation Result

<p align="center">
  <img src="Screenshot 2026-05-07 113224.png" width="700"/>
</p>

The depth sensing module estimates scene depth using monocular vision techniques and computer vision processing for environmental understanding and navigation assistance.

---

# Pseudo 3D Contour Mapping Result

<p align="center">
  <img src="Screenshot 2026-05-07 113314.png" width="700"/>
</p>

The pseudo 3D mapping system generates contour-based terrain visualization from camera input to simulate depth-aware environmental mapping for autonomous rover applications.

---
---

# Pseudo 3D Point Cloud Visualization

<p align="center">
  <img src="Screenshot 2026-05-07 124005.png" width="700"/>
</p>

A pseudo 3D point cloud was generated using a single USB webcam and AI-based monocular depth estimation on Raspberry Pi. The system captures an image, predicts relative depth using a lightweight depth estimation model, and converts image pixels into 3D coordinates to visualize a point cloud.

The generated visualization represents the spatial structure of the environment, including walls, floor surfaces, and nearby objects, without using any dedicated depth sensor or LiDAR. This demonstrates low-cost embedded 3D perception using monocular vision and lightweight AI techniques for autonomous robotic applications.

---

# Project Structure

```bash
motor_test.py                  # PWM motor testing
visionbaseddepthsence.py      # Real-time depth sensing
psudo3dmappingmonovision.py   # Pseudo 3D contour mapping
README.md

