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

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQ2FtZXJhLT4-Rmxhc2s6IEltYWdlIGNhcHR1cmluZyBhbmQgc2VuZGluZ1xuICAgIEZsYXNrLT4-UHl0aG9uIFNjcmlwdDogSW1hZ2UgaXMgZm9yd2FyZGVkIHRvIGJhY2tlbmRcbiAgICBQeXRob24gU2NyaXB0LT4-Rmxhc2s6IFJldHVybiBjb3VudGRvd24gdGltZXJcbiAgICBGbGFzayAtPj4gU2lnbmFsOiBTZW5kIHRoZSB0aW1lciB0byBzaWduYWxsaW5nIHN5c3RlbSAgICAiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGFyayJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/edit/#eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgQ2FtZXJhLT4-Rmxhc2s6IEltYWdlIGNhcHR1cmluZyBhbmQgc2VuZGluZ1xuICAgIEZsYXNrLT4-UHl0aG9uIFNjcmlwdDogSW1hZ2UgaXMgZm9yd2FyZGVkIHRvIGJhY2tlbmRcbiAgICBQeXRob24gU2NyaXB0LT4-Rmxhc2s6IFJldHVybiBjb3VudGRvd24gdGltZXJcbiAgICBGbGFzayAtPj4gU2lnbmFsOiBTZW5kIHRoZSB0aW1lciB0byBzaWduYWxsaW5nIHN5c3RlbSAgICAiLCJtZXJtYWlkIjoie1xuICBcInRoZW1lXCI6IFwiZGFya1wiXG59IiwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)

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