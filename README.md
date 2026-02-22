# API Monitoring & Debug Simulator (Python + REST API)

## Overview
A lightweight Python tool that monitors REST API endpoints, logs responses, detects repeated failures, and triggers simulated alerts — replicating real-world debugging workflows used in Product Support and Site Reliability Engineering (SRE).

## Features
- Sends GET requests to multiple APIs  
- Logs timestamps, endpoints, and status codes  
- Detects repeated failures (400/403/404/500)  
- Generates simulated ⚠️ alerts for anomalies  
- Handles errors gracefully with Python `try/except`

## Technologies Used
- Python 3.x  
- requests  
- time  
- collections.defaultdict  

## How to Run
1. Install dependencies  
   ```bash
   pip install requests

   Update Log: Improved logging format and added response time tracking.


