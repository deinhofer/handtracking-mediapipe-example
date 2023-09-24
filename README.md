# Example for handtracking using mediapipe API

This repository contains an example of handtracking using the [mediapipe API in python](https://pypi.org/project/mediapipe/).
[Mediapipe](https://developers.google.com/mediapipe) is a simple API containing performant machine learning examples directly easily embeddable into your application.

## Install

Clone the project, create a virtual environment and install the following dependencies.

Create virtual environment:
```bash
pip -m venv venv
```

Activate virtual environment (Linux only)
```bash
. venv/bin/activate
```
Activate virtual environment (Windows only)
```bash
venv/Scripts/activate
```

Install dependencies ```mediapipe``` and ```opencv-python``` with requirements.txt

```bash
pip install -r requirements.txt
```

## Run

Run the code examples by using one of the given scripts:

```bash
python main-tracking.py
```