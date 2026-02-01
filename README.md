# Intelligent Identity Tracking System

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10+-red.svg)](https://mediapipe.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Advanced CPU-efficient multi-person identification and persistent tracking system utilizing 5-Point Facial Landmarks, ArcFace ONNX embeddings, and Behavioral Pattern Analysis

---

## System Overview

This project implements a sophisticated computer vision system that goes beyond simple face recognition to provide intelligent identity tracking and behavioral analysis. Built with performance in mind, it runs entirely on CPU while maintaining real-time capabilities.

### Key Features

- User Registration & Enrollment - Easy face capture and database creation
- Real-time Multi-face Identification - Simultaneous recognition of multiple people
- Intelligent Identity Tracking - Persistent monitoring of target individuals
- Behavioral Analysis - Detection of facial expressions and movements
- Activity Timeline Logging - Comprehensive behavioral pattern recording

---

## System Architecture

```
Camera Input → Haar Detection → FaceMesh 5-Point → ArcFace Embeddings → 
Similarity Matching → Identity Tracking → Behavior Analysis → Timeline Recording
```

---

## Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Face Detection | Haar Cascades | Fast multi-face detection |
| Landmark Detection | MediaPipe FaceMesh | 5-point facial landmarks |
| Feature Extraction | ArcFace ONNX | High-quality face embeddings |
| Similarity Matching | Cosine Distance | Identity verification |
| Behavior Analysis | Geometric Heuristics | Movement and expression detection |

---

## Requirements

- Python 3.12+
- OpenCV 4.x
- NumPy
- ONNX Runtime
- MediaPipe

### Quick Installation

```bash
pip install opencv-python numpy onnxruntime mediapipe
```

---

## Project Structure

```
FaceLocking/
│
├── data/
│   ├── enroll/          # Raw enrollment images
│   └── db/              # Face feature database (face_db.npz)
│
├── models/
│   └── embedder_arcface.onnx  # ArcFace ONNX model
│
├── src/
│   ├── camera.py
│   ├── detect.py
│   ├── landmarks.py
│   ├── align.py
│   ├── embed.py
│   ├── enroll.py
│   ├── recognize.py
│   ├── evaluate.py
│   ├── haar_5pt.py
│   │
│   ├── config.py
│   ├── identity_tracker.py
│   ├── behavior_analysis.py
│   └── event_recorder.py
│
├── identity_tracking_system.py
└── README.md
```

---

## Usage Guide

### Part 1 - Face Enrollment

```bash
py -3.12 -m src.enroll
```

**Controls:**
| Key | Action |
|-----|--------|
| SPACE | Capture current frame |
| A | Auto-capture multiple frames |
| S | Save captured embeddings |
| R | Reset current session |
| Q | Quit |

> Tip: More sample images = better recognition accuracy!

---

### Part 2 - Face Recognition

```bash
py -3.12 -m src.recognize
```

**Controls:**
| Key | Action |
|-----|--------|
| Q | Quit |
| R | Reload database |
| +/- | Adjust recognition threshold |
| D | Toggle debug overlay |

**Matching Algorithm:**
```python
distance = 1 - cosine_similarity(embedding, db_embedding)
```

---

### Part 3 - Identity Tracking & Behavioral Analysis

```bash
py -3.12 identity_tracking_system.py
```

#### How Identity Tracking Works

When the target user appears:

1. System identifies the person
2. Establishes persistent tracking on that identity
3. Monitors the same person across video frames
4. Disregards other detected individuals
5. Analyzes basic facial behaviors
6. Records comprehensive activity timeline

#### Tracking States

| State | Description |
|-------|-------------|
| Identification Mode | All faces are analyzed normally |
| Tracking Mode | Only the target user is monitored |

> Smart Tracking: The system maintains tracking even during brief recognition failures and only releases if the person disappears for multiple consecutive frames.

---

## Behavioral Detection

### Detected Behaviors

| Behavior | Detection Method |
|----------|-----------------|
| Move Left | Nose X coordinate decreases over time |
| Move Right | Nose X coordinate increases over time |
| Blink | Eye landmark vertical distance temporarily reduces |
| Smile | Mouth corner horizontal distance increases |

> Approach: Uses straightforward, interpretable heuristics rather than complex neural networks for transparency and reliability.

---

## Activity Timeline Recording

When tracking is active, the system automatically generates activity logs:

```
<username>_actions_<timestamp>.txt
```

**Each entry contains:**
- Timestamp
- Behavior type
- Description (if applicable)

**Example Output:**
```
14:32:15 | Head Moved Right | User turned to the right
14:32:18 | Smile Detected | User showed positive expression
14:32:22 | Eye Blink Detected | Natural eye movement
```

---

## System Performance

### Optimization Features

- CPU-only execution - No GPU required
- Real-time processing - Optimized for live video
- Selective tracking - Focus on target identity only
- Efficient algorithms - Minimal computational overhead

### Configuration

Key parameters in `src/config.py`:

```python
TARGET_USER = "User_01"              # Target identity
CONFIDENCE_THRESHOLD = 0.65         # Recognition confidence
MAX_MISSING_FRAMES = 25              # Tracking persistence
HEAD_MOVEMENT_SENSITIVITY = 10      # Motion detection
SMILE_DETECTION_THRESHOLD = 45      # Expression detection
BLINK_DETECTION_THRESHOLD = 2.8      # Eye closure detection
```

---

## Final Result

This project demonstrates the evolution from:

```
Person Identification → Intelligent Behavioral Monitoring System
```

The system not only identifies individuals but also continuously analyzes their behavioral patterns and maintains comprehensive activity logs for advanced monitoring applications.

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgments

- OpenCV - Computer vision framework
- MediaPipe - Face landmark detection
- ArcFace - Face recognition model
- ONNX Runtime - Model inference engine

---

## Contact

For questions or suggestions, please open an issue on this repository.

---

<div align="center">

**Built with passion for intelligent computer vision systems**

</div>
