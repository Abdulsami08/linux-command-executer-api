# Linux Command Executor API

## Project Overview
This project is a simple FastAPI-based system that executes predefined Linux commands and returns output in JSON format.

## Features
- System uptime
- Disk usage
- Memory usage
- Current user
- Health check API

## API Endpoints
- GET /system/uptime
- GET /system/disk
- GET /system/memory
- GET /system/user
- GET /health

## Run Project
pip install -r requirements.txt  
uvicorn main:app --reload

## Technologies Used
- Python
- FastAPI
- Linux Commands
- Uvicorn