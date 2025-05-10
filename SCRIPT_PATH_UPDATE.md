# AEGIS-AI Script Path Update

## Overview

We've updated the script paths in the AEGIS-AI platform to point to the new location of the scripts. The system was trying to find scripts in the old directory structure (`D:\bkp\AEGIS-AI\backend\AI-SCRIPT\Web\xss_attack.py`) but we've moved the scripts to a new location (`D:\bkp\AEGIS-AI\backend\scripts\`).

## Changes Made

### 1. Updated BOT_SCRIPTS Dictionary in app.py

We've updated the BOT_SCRIPTS dictionary in app.py to point to the new location of the scripts. For each script, we've:
- Updated the 'filename' field to point to the scripts directory
- Updated the 'args' field to use the new path
- Added 'local': True to indicate that these are local scripts

### 2. Updated Script Paths for All Scripts

We've updated the paths for the following scripts:

#### Web Attack Scripts
- xss_payload_demo.py
- csrf_attack_demo.py
- form_submitter.py
- harmful_demo.py

#### DDoS Attack Scripts
- slowloris_attack.py

#### Reconnaissance Scripts
- port_scanner.py
- directory_bruteforce.py

#### AI/LLM Attack Scripts
- ai_chatbot_demo.py
- langchain_demo.py
- openai_api_demo.py
- anthropic_claude_demo.py
- autogen_demo.py

#### Bot Attack Scripts
- fake_login_bot.py
- email_spam_demo.py
- brute_force_demo.py
- scraper_demo.py
- selenium_bot_demo.py

#### CAPTCHA Attack Scripts
- captcha_bypass_demo.py
- captcha_solver_demo.py

### 3. Fixed Script Path Handling in console-functions.js

We've updated the script path handling in console-functions.js to use the correct format for API calls: `scripts.${scriptKey}`. This ensures that the backend looks for scripts in the correct location.

## How It Works Now

1. When a script is run, the system will look for it in the correct location: `D:\bkp\AEGIS-AI\backend\scripts\`
2. The scripts are now properly categorized and organized in a single directory
3. The system will use the local JavaScript implementations as a fallback if the Python backend is not available

## Benefits

1. **Simplified Structure**: All scripts are now in a single directory, making them easier to manage
2. **Consistent Implementation**: All scripts follow the same structure and API
3. **Correct Path Handling**: The system now uses the correct path format for API calls
4. **Fallback Mechanism**: The frontend can use the JavaScript implementations when the Python backend is not available

## Next Steps

1. Test the system to ensure that all scripts are working correctly
2. Consider adding more scripts to the system
3. Improve the error handling to provide more detailed information when a script fails to run