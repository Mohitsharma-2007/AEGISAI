# AEGIS-AI Script Integration Changes

## Overview

We've implemented a comprehensive set of attack simulation scripts for the AEGIS-AI platform with both Python backend implementations and JavaScript fallback implementations.

## Changes Made

### 1. Created Python Scripts

We've created the following Python scripts in the backend/scripts directory:

#### DDoS Attacks
- `slowloris_attack.py`: Simulates a Slowloris attack that keeps connections open by sending partial HTTP requests

#### Web Attacks
- `xss_payload_demo.py`: Demonstrates Cross-Site Scripting (XSS) attacks with various payloads
- `csrf_attack_demo.py`: Demonstrates Cross-Site Request Forgery (CSRF) attacks against web forms
- `form_submitter.py`: Simulates automated form submission attacks
- `harmful_demo.py`: Demonstrates harmful Cross-Site Scripting (XSS) attacks

#### Reconnaissance
- `port_scanner.py`: Scans for open ports on a target system
- `directory_bruteforce.py`: Attempts to discover hidden directories on a web server

#### AI/LLM Attacks
- `ai_chatbot_demo.py`: Demonstrates attacks against AI chatbots
- `langchain_demo.py`: Demonstrates attacks against LangChain agents
- `openai_api_demo.py`: Demonstrates attacks against OpenAI APIs
- `anthropic_claude_demo.py`: Demonstrates attacks against Anthropic Claude
- `autogen_demo.py`: Demonstrates attacks against Microsoft AutoGen

#### Bot Attacks
- `fake_login_bot.py`: Simulates automated login attempts with credential stuffing
- `email_spam_demo.py`: Demonstrates email spam attacks
- `brute_force_demo.py`: Demonstrates brute force password attacks
- `scraper_demo.py`: Demonstrates web scraping attacks
- `selenium_bot_demo.py`: Demonstrates browser automation attacks

#### CAPTCHA Attacks
- `captcha_bypass_demo.py`: Shows techniques to bypass CAPTCHA using third-party services
- `captcha_solver_demo.py`: Demonstrates automated CAPTCHA solving

### 2. Created JavaScript Fallback Implementations

We've created a new file `frontend/js/local-scripts.js` that contains JavaScript implementations of all the scripts. These are used as fallbacks when the Python backend is not available.

### 3. Updated Script Bridge

Modified `frontend/js/script-bridge.js` to:
- Update the script paths to point to the new location in the backend/scripts directory
- Implement a categorization function based on script IDs
- Add fallback to local JavaScript implementations when the Python backend is not available
- Fix the script path handling in API calls

### 4. Updated Console HTML

Modified `frontend/console.html` to:
- Include the new local-scripts.js file
- Set useLocalScripts to true by default
- Define specific scripts with their metadata
- Update the script loading function to use these specific scripts

## Script Structure

Each script (both Python and JavaScript) follows a consistent structure:

1. **Metadata**: Name and description
2. **Run Function**: Simulates the attack and returns events and block details
3. **Test Detection Function**: Simulates the detection process with realistic timing

## Benefits

These changes provide several benefits:

1. **Simplified Structure**: All scripts are now in a single directory, making them easier to manage
2. **Consistent Implementation**: All scripts follow the same structure and API
3. **Realistic Simulation**: Each script simulates a realistic attack scenario with appropriate parameters
4. **Performance Measurement**: The test_detection function allows measuring the detection speed
5. **Fallback Mechanism**: The frontend can use the JavaScript implementations when the Python backend is not available

## How to Use

1. The system will first try to use the Python backend scripts
2. If the Python backend is not available, it will automatically fall back to the JavaScript implementations
3. You can force the use of local scripts by setting `window.useLocalScripts = true` (currently the default)

## Next Steps

To further improve the script implementation:

1. Add more sophisticated attack simulations
2. Implement more realistic detection algorithms
3. Add support for script parameters to customize the attack behavior
4. Create a script discovery mechanism to automatically find and load scripts