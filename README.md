# ⚡ Electricity Meter API

> A Flask-powered API for managing and analyzing electricity meter readings 🌟

## 🎯 Features

- 📊 Get all meter readings by meter ID
- 📈 Calculate monthly averages for specific meters
- 🔍 Easy-to-use test interface with clickable buttons
- 🎨 Pretty JSON responses for better readability

## Assumptions
- Server maintenance will only happen during 0000-0100.
- Meter will only be installed more than 1 hour before the start of server maintenance.
- When server crash, server recovery will start to run.
- When meter reading comes into the server is cumulative and positive number.
- The last line of csv in daily and monthly csv will be the latest reading.

## Installation Guide for Backend
- Step 1: Run this code in the terminal

```
python3 -m pip install --upgrade pip
```
- Step 2: Run this in the terminal
```
pip install -r requirements.txt
```
- Step 3: Run this in terminal
```
python app.py
```
