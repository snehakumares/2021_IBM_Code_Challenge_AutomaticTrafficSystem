# Automatic Traffic Signalling System

An automated traffic signalling system that provides a smart way of defining the flow of vehicles in traffic.

## The Problem We Face

We all have experienced long queues and waiting time in traffic, haven't us? Even though there may be a few vehicles (or none at all!), we need to wait for the timer to end to continue our journey. Isn't it a wastage of our valuable time and also resources?

## How can we solve this?

We came up with a solution for this. An automated, smart traffic signalling system, which is capable of analysing the traffic beforehand and providing signalling according to the congestion. Each traffic signals and/or junctions have cameras which captures images in a particular direction and sends to a backend server where the image is processed and an optimum time limit is returned.

## System Users and Usecase

This is as an embedded system. The software and required hardware are integrated together to perform the specific task. Hence maintainance and activation is only the key external activities that is needed to be performed in the system.

- Users who have access to the system:
    - System analysts
    - System maintainers
    - Traffic Control Authority

## Code Flow

![Flow Diagram](https://github.com/snehakumares/2021_IBM_Code_Challenge_AutomaticTrafficSystem/images/flow.png)

## How to use

### Pre-requisites
- Download Python from [here](https://www.python.org/downloads/)
- Code Editor of your choice. (Eg. VSCode, Sublime Text, Atom, etc.)

The repository is split into two segment:
- `bin` folder contains the core python scripts that can be embedded into a system for direct functioning.
- `src` folder contains a Flask application which can be used to demonstrate the interaction of camera and backend processing.

`Step 1` : Excute command ```pip install requirements.txt```. This will install all the libraries needed to run the program.

`Step 2` : Navigate into `src` folder and execute the command `py app.py`

`Step 3` : The application will now be running on local host. i.e. `https://127.0.0.5000/`