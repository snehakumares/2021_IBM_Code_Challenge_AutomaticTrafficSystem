# Automatic Traffic Signalling System :traffic_light:

An automated traffic signalling system that provides a smart way of defining the flow of vehicles in traffic.

## The Problem

We all have experienced long queues and waiting time in traffic, haven't us? Even though there may be a few vehicles (or none at all!), we need to wait for the timer to end to continue our journey. Isn't it a wastage of our valuable time and also resources?

## How can we solve this?

We came up with a solution for this. An automated, smart traffic signalling system, which is capable of analysing the traffic beforehand and providing signalling according to the congestion. Each traffic signals and/or junctions have cameras which captures images in a particular direction and sends to a backend server where the image is processed and an optimum time limit is returned.

## Code Flow and System Users

![Flow Diagram](https://github.com/snehakumares/2021_IBM_Code_Challenge_AutomaticTrafficSystem/blob/main/images/flow.png)

This is as an embedded system. The software and required hardware are integrated together to perform the specific task. Hence maintainance and activation is only the key external activities that is needed to be performed in the system.

- Users who have access to the system:
    - System analysts
    - System maintainers
    - Traffic Control Authority

## How to use

### Pre-requisites
- Download Python from [here](https://www.python.org/downloads/)
- Code Editor of your choice. (Eg. VSCode, Sublime Text, Atom, etc.)

The repository is split into two segment:
- `bin` folder contains the core python scripts that can be embedded into a system for direct functioning after slight modifications.
- `src` folder contains a Flask application which can be used to demonstrate the interaction of camera and backend processing.

`Step 1` : Excute command ```pip install requirements.txt```. This will install all the libraries needed to run the program.

`Step 2` : Navigate into `src` folder and execute the command `py app.py`

`Step 3` : The application will now be running on local host. i.e. `https://127.0.0.5000/`

`Step 4` : Provide image for respective side and submit the form. A suitable timer will be displayed on the screen.

## Problems faced
- Camera positions must be fixed for a particular direction. Vehicles in other side of the roads may come in the view of a camera which is facing a particular side that may affect the systems accuracy.
- Highly congested traffic is difficult to be analyzed and taken count of.
- Camera operation in different weather conditions and low-light.

## Future Plans
- Since the accuracy of the system is subjected to vehicle count, we could integrate training mechanism so that the system can learn from the experiences.
- Timer can be automatically adjusted according to the type of vechiles (two wheeler are comparitively faster than heavier vehicles). Hence training can be given to implement this functionality.
- Data about vehicle traffic and effectiveness can be stored in database which can be used for modelling the system updates and can be used by officials to know the traffic pattern in large cities.

## Contributors

- Abhilash Nair, *NSS College of Engineering, Palakkad*
- Abhishek T, *NSS College of Engineering, Palakkad*
- Amrutha V.P, *NSS College of Engineering, Palakkad*
- Divya K, *NSS College of Engineering, Palakkad*
- Sneha Kumaresan, *NSS College of Engineering, Palakkad*

## License

This repository is licensed under Apache License, v2.0. See [LICENSE](https://github.com/snehakumares/2021_IBM_Code_Challenge_AutomaticTrafficSystem/blob/main/LICENSE) for full licensing text.