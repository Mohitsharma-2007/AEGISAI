# AEGIS-AI Project

## Overview

AEGIS-AI is a comprehensive AI detection and attack simulation platform designed to identify and mitigate AI/bot/LLM activities using advanced algorithms. The project includes both frontend and backend components, each serving specific functionalities.

## Features

- Simulates a wide range of attack types:
  - DDoS attacks (HTTP Flooder, Slowloris)
  - Web attacks (SQL Injection, XSS, CSRF)
  - Reconnaissance (Port Scanning, Directory Bruteforce)
  - AI/LLM attacks (GPT, Claude, Gemini)
  - Bot attacks (Login Bots, Form Submitters)
  - CAPTCHA bypass techniques

- Dual implementation:
  - JavaScript frontend for standalone operation
  - Python backend for more realistic attack simulations

- Interactive console interface
- Real-time attack visualization
- Detection speed testing
- Detailed attack forensics

## Directory Structure

```
AEGIS-AI/
├── frontend/              # Web frontend
│   ├── js/                # JavaScript files
│   │   ├── attack-scripts.js      # JS attack implementations
│   │   ├── console-functions.js   # Console functionality
│   │   └── console-ui.js          # UI interactions
│   ├── css/               # CSS stylesheets
│   ├── console.html       # Main console interface
│   └── index.html         # Landing page
│
├── backend/               # Python backend
│   ├── api_server.py      # Flask API server
│   ├── scripts/           # Attack simulation scripts
│   │   ├── ddos/          # DDoS attack scripts
│   │   ├── web/           # Web attack scripts
│   │   ├── recon/         # Reconnaissance scripts
│   │   ├── ai/            # AI/LLM attack scripts
│   │   ├── bot/           # Bot attack scripts
│   │   └── captcha/       # CAPTCHA attack scripts
│   └── requirements.txt   # Python dependencies
│
└── start_aegis.bat        # Startup script for Windows
```

## Backend

The backend consists of:
- Attack simulation scripts organized by category
- A Flask API server for handling requests from the frontend
- A script handler for loading and executing attack scripts
- Detection algorithms for identifying and blocking attacks

## Frontend

The frontend is built using HTML, CSS, and JavaScript, providing an interface for:
- Selecting and running attack simulations
- Viewing attack logs and block details
- Testing detection speed
- Downloading forensics reports

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Edge)

### Installation

1. Clone the repository
2. Install Python dependencies:
   ```
   pip install -r backend/requirements.txt
   ```

### Running AEGIS-AI

#### Windows

Simply run the `start_aegis.bat` script:

```
start_aegis.bat
```

This will:
1. Start the Python backend server on port 5050
2. Start a simple HTTP server for the frontend on port 8080
3. Open the AEGIS-AI console in your default browser

#### Manual Start

1. Start the backend server:
   ```
   cd backend
   python api_server.py
   ```

2. In a separate terminal, start a web server for the frontend:
   ```
   cd frontend
   python -m http.server 8080
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:8080/console.html
   ```

## Usage

1. Select an attack script from the dropdown menu
2. Read the description to understand what the attack does
3. Click "Run Attack Script" to simulate the attack
4. View the attack logs and block details in the console
5. Use "Test Detection Speed" to measure AEGIS-AI's response time

## Adding New Attack Scripts

### Python Backend

1. Create a new Python file in the appropriate category directory (e.g., `backend/scripts/web/new_attack.py`)
2. Implement the script using the `BaseScript` class as a parent
3. Define the required metadata (NAME, DESCRIPTION)
4. Implement the `run()` method
5. Optionally implement `test_detection()` and `simulate_detection()` methods
6. Export the script functions (`run`, `test_detection`, `simulate_detection`)

### JavaScript Frontend

1. Add a new attack script to `frontend/js/attack-scripts.js`
2. Implement the required methods: `execute()` and `testDetection()`
3. Add the script description to the `scriptDescriptions` object in `frontend/js/console-functions.js`

## License

This project is licensed under the MIT License.

## Disclaimer

AEGIS-AI is designed for educational purposes only. The attack simulations are not intended to be used for malicious purposes. Always obtain proper authorization before testing security measures on any system you do not own.