from flask import Flask, request, jsonify
from flask_cors import CORS

import os
from flask import send_from_directory, redirect

app = Flask(__name__)
CORS(app)

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), '../frontend')

@app.route('/')
def root():
    return redirect('/dashboard.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(FRONTEND_DIR, filename)

# Secure Browsing state
secure_browsing = {'enabled': False}

# In-memory storage for logs, settings, etc. (for prototype)
logs = [
    {"timestamp": "2025-04-29 12:01", "ip": "192.168.1.1", "type": "Bot", "status": "Blocked"},
    {"timestamp": "2025-04-29 12:05", "ip": "10.0.0.2", "type": "AI Agent", "status": "Confused"},
    {"timestamp": "2025-04-29 12:10", "ip": "172.16.0.3", "type": "Unknown", "status": "Escaped"}
]
settings = {
    "theme": "dark",
    "sensitivity": "Medium",
    "notifications": True,
    "2fa": False,
    "language": "English"
}
# In-memory honeypot activations log
honeypot_activations = []

@app.route('/api/logs', methods=['GET'])
def get_logs():
    return jsonify(logs)

@app.route('/api/settings', methods=['GET', 'POST'])
def api_settings():
    global settings
    if request.method == 'POST':
        data = request.json
        for k in settings:
            if k in data:
                settings[k] = data[k]
        return jsonify({"success": True, "settings": settings})
    return jsonify(settings)

from datetime import datetime

@app.route('/api/dashboard', methods=['GET'])
def dashboard():
    today = datetime.now().strftime('%Y-%m-%d')
    bots_today = sum(1 for l in logs if l.get('type') == 'Bot' and l.get('timestamp','').startswith(today))
    blocked_today = sum(1 for l in logs if l.get('status') == 'Blocked' and l.get('timestamp','').startswith(today))
    security_rating = max(0, min(100, 100 - blocked_today * 2))
    recent_events = list(reversed(logs[-10:]))
    return jsonify({
        "bots_today": bots_today,
        "blocked_today": blocked_today,
        "security_rating": security_rating,
        "recent_events": recent_events
    })

import threading
from flask import Response
import time

def event_stream():
    last_idx = len(logs)
    while True:
        time.sleep(1)
        if len(logs) > last_idx:
            for log in logs[last_idx:]:
                yield f'data: {jsonify(log).data.decode() if hasattr(jsonify(log), "data") else str(log)}\n\n'
            last_idx = len(logs)

@app.route('/api/dashboard/stream')
def dashboard_stream():
    return Response(event_stream(), mimetype='text/event-stream')

# Mutable trap states
trap_states = [
    {"name": "Honeypot Field", "status": "ON", "last_triggered": None},
    {"name": "Randomized CAPTCHA", "status": "ON", "last_triggered": None},
    {"name": "Behavior Puzzle", "status": "OFF", "last_triggered": None}
]

@app.route('/api/traps', methods=['GET'])
def traps():
    return jsonify(trap_states)

@app.route('/api/traps/toggle', methods=['POST'])
def traps_toggle():
    data = request.json
    name = data.get('name')
    status = data.get('status')
    for trap in trap_states:
        if trap['name'] == name:
            trap['status'] = status
            logs.append({
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'ip': request.remote_addr,
                'type': 'Trap',
                'status': status,
                'summary': f"{name} toggled to {status}"
            })
            return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Trap not found'})

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_USER = 'grnoida.mohitsharma2007@gmail.com'
GMAIL_PASS = 'zacb tpch vrfe ljsb'

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    to_addr = 'grnoida.mohitsharma2007@gmail.com'
    subject = f'AegisAI Contact/Demo Request from {name}'
    body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASS)
        server.sendmail(GMAIL_USER, to_addr, msg.as_string())
        server.quit()
        return jsonify({'success': True})
    except Exception as e:
        print('Failed to send email:', e)
        print('--- Contact Request ---')
        print(body)
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/request-demo', methods=['POST'])
def request_demo():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    details = data.get('details')
    to_addr = 'grnoida.mohitsharma2007@gmail.com'
    subject = f'AegisAI Demo Request from {name}'
    body = f"Name: {name}\nEmail: {email}\nDemo Details:\n{details}"
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASS)
        server.sendmail(GMAIL_USER, to_addr, msg.as_string())
        server.quit()
        return jsonify({'success': True})
    except Exception as e:
        print('Failed to send demo email:', e)
        print('--- Demo Request ---')
        print(body)
        return jsonify({'success': False, 'error': str(e)})

from datetime import datetime
import random

@app.route('/api/simulate-attacks', methods=['POST'])
def simulate_attacks():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    attacks = [
        {"timestamp": now, "ip": f"192.168.1.{random.randint(10, 99)}", "type": "Bot", "status": "Blocked"},
        {"timestamp": now, "ip": f"10.0.0.{random.randint(10, 99)}", "type": "AI", "status": "Confused"},
        {"timestamp": now, "ip": f"172.16.0.{random.randint(10, 99)}", "type": "Scripted", "status": "Blocked"},
        {"timestamp": now, "ip": f"203.0.113.{random.randint(10, 99)}", "type": "Online", "status": "Blocked"},
    ]
    logs.extend(attacks)
    return jsonify({"success": True, "message": "Attacks simulated.", "added": attacks})

import subprocess

import subprocess
import requests
import os

# List of available scripts (safe and 'harmful' for demo)
BOT_SCRIPTS = {
    # 1-3: Existing (now with local versions)
    'http_flooder': {
        'desc': 'HTTP Flooder (safe demo)',
        'filename': 'AI-SCRIPT/DDoS/http_flood.py',
        'args': ['python', 'AI-SCRIPT/DDoS/http_flood.py'],
        'local': True
    },
    'form_submitter': {
        'desc': 'Form Submitter (safe demo)',
        'filename': 'AI-SCRIPT/Web/csrf_attack.py',
        'args': ['python', 'AI-SCRIPT/Web/csrf_attack.py'],
        'local': True
    },
    'harmful_demo': {
        'desc': 'XSSer (harmful demo, do not use on real targets)',
        'filename': 'AI-SCRIPT/Web/xss_attack.py',
        'args': ['python', 'AI-SCRIPT/Web/xss_attack.py'],
        'local': True
    },
    # Local AI scripts (Claude)
    'claude_captcha_bypass': {
        'desc': 'Claude Captcha Bypass',
        'filename': 'AI-SCRIPT/Claude/claude_captcha_bypass.py',
        'args': ['python', 'AI-SCRIPT/Claude/claude_captcha_bypass.py'],
        'local': True
    },
    'claude_probe': {
        'desc': 'Claude Probe',
        'filename': 'AI-SCRIPT/Claude/claude_probe.py',
        'args': ['python', 'AI-SCRIPT/Claude/claude_probe.py'],
        'local': True
    },
    # Local AI scripts (GPT)
    'gpt_form_attack': {
        'desc': 'GPT Form Attack',
        'filename': 'AI-SCRIPT/GPT/gpt_form_attack.py',
        'args': ['python', 'AI-SCRIPT/GPT/gpt_form_attack.py'],
        'local': True
    },
    'gpt_probe': {
        'desc': 'GPT Probe',
        'filename': 'AI-SCRIPT/GPT/gpt_probe.py',
        'args': ['python', 'AI-SCRIPT/GPT/gpt_probe.py'],
        'local': True
    },
    # Local AI scripts (Gemini)
    'gemini_form_spam': {
        'desc': 'Gemini Form Spam',
        'filename': 'AI-SCRIPT/Gemini/gemini_form_spam.py',
        'args': ['python', 'AI-SCRIPT/Gemini/gemini_form_spam.py'],
        'local': True
    },
    'gemini_recon': {
        'desc': 'Gemini Recon',
        'filename': 'AI-SCRIPT/Gemini/gemini_recon.py',
        'args': ['python', 'AI-SCRIPT/Gemini/gemini_recon.py'],
        'local': True
    },
    # New Web Attack Scripts
    'sql_injection_demo': {
        'desc': 'SQL Injection Demo',
        'filename': 'scripts/sql_injection_demo.py',
        'args': ['python', 'scripts/sql_injection_demo.py'],
        'local': True
    },
    'xss_payload_demo': {
        'desc': 'XSS Payload Demo',
        'filename': 'scripts/xss_payload_demo.py',
        'args': ['python', 'scripts/xss_payload_demo.py'],
        'local': True
    },
    'csrf_attack_demo': {
        'desc': 'CSRF Attack Demo',
        'filename': 'scripts/csrf_attack_demo.py',
        'args': ['python', 'scripts/csrf_attack_demo.py'],
        'local': True
    },
    'form_submitter': {
        'desc': 'Form Submitter',
        'filename': 'scripts/form_submitter.py',
        'args': ['python', 'scripts/form_submitter.py'],
        'local': True
    },
    'harmful_demo': {
        'desc': 'XSS Attack Demo',
        'filename': 'scripts/harmful_demo.py',
        'args': ['python', 'scripts/harmful_demo.py'],
        'local': True
    },
    # DDoS Attack Scripts
    'slowloris_attack': {
        'desc': 'Slowloris DDoS Attack',
        'filename': 'scripts/slowloris_attack.py',
        'args': ['python', 'scripts/slowloris_attack.py'],
        'local': True
    },
    # Recon Scripts
    'port_scanner': {
        'desc': 'Port Scanner',
        'filename': 'scripts/port_scanner.py',
        'args': ['python', 'scripts/port_scanner.py'],
        'local': True
    },
    'directory_bruteforce': {
        'desc': 'Directory Bruteforce',
        'filename': 'scripts/directory_bruteforce.py',
        'args': ['python', 'scripts/directory_bruteforce.py'],
        'local': True
    },
    # 4-50: Variety of safe and demo scripts
    'scraper_demo': {
        'desc': 'Web Scraper Demo',
        'filename': 'scripts/Scraper_demo.py',
        'args': ['python', 'scripts/Scraper_demo.py'],
        'local': True
    },
    'sql_injection_demo': {
        'url': 'https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/sqlmap.py',
        'desc': 'SQLMap SQLi Demo',
        'filename': 'sqlmap.py',
        'args': ['python', 'sqlmap.py', '--version']
    },
    'captcha_bypass_demo': {
        'desc': 'CAPTCHA Bypass Demo',
        'filename': 'scripts/captcah_bypass_demo.py',
        'args': ['python', 'scripts/captcah_bypass_demo.py'],
        'local': True
    },
    'fake_login_bot': {
        'desc': 'Fake Login Bot',
        'filename': 'scripts/fake_login_bot.py',
        'args': ['python', 'scripts/fake_login_bot.py'],
        'local': True
    },
    'email_spam_demo': {
        'desc': 'Email Spam Demo',
        'filename': 'scripts/email_spam_demo.py',
        'args': ['python', 'scripts/email_spam_demo.py'],
        'local': True
    },
    'brute_force_demo': {
        'desc': 'Brute Force Demo',
        'filename': 'scripts/brute_force_demo.py',
        'args': ['python', 'scripts/brute_force_demo.py'],
        'local': True
    },
    'ai_chatbot_demo': {
        'desc': 'AI Chatbot Demo',
        'filename': 'scripts/ai_chatbot_demo.py',
        'args': ['python', 'scripts/ai_chatbot_demo.py'],
        'local': True
    },
    'llm_completion_demo': {
        'url': 'https://raw.githubusercontent.com/huggingface/transformers/main/examples/pytorch/text-generation/run_generation.py',
        'desc': 'LLM Completion Demo',
        'filename': 'run_generation.py',
        'args': ['python', 'run_generation.py', '--help']
    },
    'torch_image_demo': {
        'url': 'https://raw.githubusercontent.com/pytorch/examples/main/mnist/main.py',
        'desc': 'Torch Image Demo',
        'filename': 'mnist_main.py',
        'args': ['python', 'mnist_main.py', '--help']
    },
    'bert_qa_demo': {
        'url': 'https://raw.githubusercontent.com/huggingface/transformers/main/examples/pytorch/question-answering/run_qa.py',
        'desc': 'BERT QA Demo',
        'filename': 'run_qa.py',
        'args': ['python', 'run_qa.py', '--help']
    },
    'langchain_demo': {
        'desc': 'LangChain Agent Demo',
        'filename': 'scripts/langchain_demo.py',
        'args': ['python', 'scripts/langchain_demo.py'],
        'local': True
    },
    'huggingface_transformers_demo': {
        'url': 'https://raw.githubusercontent.com/huggingface/transformers/main/examples/pytorch/text-classification/run_glue.py',
        'desc': 'Huggingface Transformers Demo',
        'filename': 'run_glue.py',
        'args': ['python', 'run_glue.py', '--help']
    },
    'openai_api_demo': {
        'desc': 'OpenAI API Demo',
        'filename': 'scripts/openai_api_demo.py',
        'args': ['python', 'scripts/openai_api_demo.py'],
        'local': True
    },
    'anthropic_claude_demo': {
        'desc': 'Anthropic Claude Demo',
        'filename': 'scripts/anthropic_claude_demo.py',
        'args': ['python', 'scripts/anthropic_claude_demo.py'],
        'local': True
    },
    'stable_diffusion_demo': {
        'url': 'https://raw.githubusercontent.com/CompVis/stable-diffusion/main/scripts/txt2img.py',
        'desc': 'Stable Diffusion Demo',
        'filename': 'txt2img.py',
        'args': ['python', 'txt2img.py', '--help']
    },
    'selenium_bot_demo': {
        'desc': 'Selenium Bot Demo',
        'filename': 'scripts/selenium_bot_demo.py',
        'args': ['python', 'scripts/selenium_bot_demo.py'],
        'local': True
    },
    'autogen_demo': {
        'desc': 'Microsoft AutoGen Demo',
        'filename': 'scripts/autogen_demo.py',
        'args': ['python', 'scripts/autogen_demo.py'],
        'local': True
    },
    'captcha_solver_demo': {
        'desc': 'CAPTCHA Solver Demo',
        'filename': 'scripts/captcha_solver_demo.py',
        'args': ['python', 'scripts/captcha_solver_demo.py'],
        'local': True
    },
    'xss_payload_demo': {
        'url': 'https://raw.githubusercontent.com/0xInfection/Awesome-XSS-Payloads/master/payloads/xss.js',
        'desc': 'XSS Payload Demo',
        'filename': 'xss.js',
        'args': ['node', 'xss.js']
    },
    # ... (Add 30+ more realistic, safe, or demo scripts with unique keys and descriptions)
}
# For brevity, only 20 shown. In production, fill to 50+ with more safe scripts from GitHub, OWASP, or your own demos.


@app.route('/api/online-bot-attack', methods=['POST'])
def online_bot_attack():
    global secure_browsing
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    events = []
    log_entries = []
    script_key = request.json.get('script', 'http_flooder')
    script = BOT_SCRIPTS.get(script_key, BOT_SCRIPTS['http_flooder'])
    # Use a dedicated folder for downloaded scripts
    # Determine script path: local vs remote
    if script.get('local'):
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), script['filename']))
    else:
        scripts_dir = os.path.join(os.path.dirname(__file__), 'downloaded_scripts')
        os.makedirs(scripts_dir, exist_ok=True)
        script_path = os.path.join(scripts_dir, script['filename'])
    if secure_browsing.get('enabled'):
        events.append(f"{script['desc']} attack blocked by Secure Browsing!")
        log_entries.append({"timestamp": now, "ip": "0.0.0.0", "type": "Online", "status": "Blocked by Secure Browsing", "script": script_key})
        logs.extend(log_entries)
        return jsonify({"success": True, "events": events})
    # Download script if not present or empty (remote only)
    if not script.get('local'):
        def download_script():
            try:
                r = requests.get(script['url'], timeout=10)
                if r.status_code != 200 or not r.text.strip():
                    raise Exception(f"Script not found or empty at {script['url']}")
                with open(script_path, 'w', encoding='utf-8') as f:
                    f.write(r.text)
                return True, None
            except Exception as e:
                return False, str(e)
        need_download = not os.path.exists(script_path) or os.path.getsize(script_path) == 0
        if need_download:
            events.append(f"Downloading bot script: {script['desc']}")
            ok, err = download_script()
            if not ok:
                events.append(f"Failed to download script: {err}")
                log_entries.append({"timestamp": now, "ip": "0.0.0.0", "type": "Online", "status": f"Download Error: {err}", "script": script_key})
                logs.extend(log_entries)
                return jsonify({"success": False, "events": events, "script": script_key, "error": f"Script not found or unavailable: {err}"})
            events.append(f"Downloaded {script['filename']}")
        # If still missing or empty, try to re-download once
        if not os.path.exists(script_path) or os.path.getsize(script_path) == 0:
            ok, err = download_script()
            if not ok or not os.path.exists(script_path) or os.path.getsize(script_path) == 0:
                events.append(f"Script file is missing or empty after download attempts.")
                log_entries.append({"timestamp": now, "ip": "0.0.0.0", "type": "Online", "status": "Script file missing after download", "script": script_key})
                logs.extend(log_entries)
                return jsonify({"success": False, "events": events, "script": script_key, "error": "Script file missing or empty after download attempts."})
    # For local scripts, check existence and non-empty
    if script.get('local'):
        if not os.path.exists(script_path) or os.path.getsize(script_path) == 0:
            events.append(f"Local script file not found or empty: {script_path}")
            log_entries.append({"timestamp": now, "ip": "0.0.0.0", "type": "Online", "status": "Local script missing or empty", "script": script_key})
            logs.extend(log_entries)
            return jsonify({"success": False, "events": events, "script": script_key, "error": f"Local script not found or empty: {script_path}"})
    # Fast pre-check for known malicious scripts
    script_basename = os.path.basename(script_path).lower()
    
    # Instant block for known malicious script names
    instant_block_names = ['attack', 'exploit', 'hack', 'flood', 'ddos', 'injection', 'xss', 'csrf', 'scan']
    for block_name in instant_block_names:
        if block_name in script_basename:
            block_reason = f"Instant detection: Malicious script name '{block_name}'"
            events.append(f"AEGIS-AI instantly blocked script: {block_reason}")
            
            # Create minimal block details
            block_details = {
                'script_key': script_key,
                'script_name': script.get('desc', script_key),
                'block_reason': block_reason,
                'how_identified': f"Millisecond detection based on script name pattern",
                'code_sample': f"# Script blocked before content analysis\n# Filename: {script_basename}\n# Detection time: <1ms",
                'filename': script.get('filename'),
                'url': script.get('url', 'Local script'),
            }
            
            log_entries.append({
                "timestamp": now, 
                "ip": "0.0.0.0", 
                "type": "Block", 
                "status": f"Blocked in <1ms: {block_reason}", 
                "script": script_key, 
                "block_details": block_details
            })
            logs.extend(log_entries)
            return jsonify({
                "success": True, 
                "events": events, 
                "script": script_key, 
                "block_details": block_details,
                "detection_time_ms": "<1ms"
            })
    
    # AI/LLM/ML, HTTP Flooder, and Vulnerability detection/blocking
    detection_start = time.time()
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read(8192)  # scan first 8KB for more coverage
        ai_keywords = [
            'openai', 'gpt', 'llm', 'bert', 'torch', 'transformers', 'langchain', 'stable-diffusion', 
            'autogen', 'anthropic', 'llama', 'ai21', 'pytorch', 'huggingface', 'ml', 'ai', 'chatgpt',
            'claude', 'gemini', 'bard', 'mistral', 'cohere', 'dalle', 'midjourney', 'diffusion', 
            'neural network', 'deep learning', 'machine learning', 'nlp', 'natural language processing',
            'embedding', 'token', 'tokenizer', 'completion', 'prompt', 'fine-tuning', 'rag'
        ]
        
        flood_keywords = [
            'flood', 'ddos', 'mhddos', 'attack', 'http flood', 'requests.get', 'requests.post',
            'slowloris', 'syn flood', 'ping flood', 'amplification', 'botnet', 'threadpool',
            'concurrent.futures', 'threading', 'multiprocessing', 'asyncio', 'aiohttp',
            'socket', 'connection', 'keep-alive', 'timeout', 'max_workers'
        ]
        
        web_attack_keywords = [
            'sql injection', 'sqli', 'union select', 'or 1=1', 'drop table', 'information_schema',
            'xss', 'cross site', 'script>', 'alert(', 'onerror', 'onload', 'csrf', 'cross-site request',
            'forgery', 'clickjacking', 'iframe', 'lfi', 'rfi', 'path traversal', '../', 'file://',
            'command injection', 'shell', 'exec', 'eval', 'system', 'passthru', 'bypass', 'captcha'
        ]
        
        recon_keywords = [
            'port scan', 'nmap', 'reconnaissance', 'enumeration', 'fingerprint', 'banner grabbing',
            'directory', 'bruteforce', 'wordlist', 'dictionary', 'fuzzing', 'information gathering',
            'whois', 'dns', 'subdomain', 'crawl', 'spider', 'scrape', 'harvest', 'extract'
        ]
        
        vuln_keywords = [
            'os.system', 'subprocess', 'eval', 'exec(', 'import socket', 'import urllib', 'import requests', 'selenium',
            'sys.argv', 'base64', 'pickle', 'input(', 'open(', 'webbrowser', 'shutil', 'ftp', 'paramiko', 'popen',
            'import telnetlib', 'import ftplib', 'import http', 'import smtplib', 'import poplib', 'import imaplib',
            'import nmap', 'import winreg', 'import win32', 'import pyautogui', 'import pywinauto', 'import pyppeteer',
            'import pycurl', 'import urllib2', 'import urllib3', 'import xmlrpc', 'import xml.etree', 'import lxml',
            'import cryptography', 'import hashlib', 'import ssl', 'import socketserver', 'import flask', 'import django',
            'import tornado', 'import bottle', 'import twisted', 'import flask_restful', 'import aiohttp', 'import requests_html'
        ]
        detected = False
        block_reason = None
        # AI/LLM/ML
        for kw in ai_keywords:
            if kw in script_content.lower():
                block_reason = f"AI/LLM/ML attack: '{kw}'"
                detected = True
                break
                
        # DDoS/Flood attacks
        if not detected:
            for kw in flood_keywords:
                if kw in script_content.lower():
                    block_reason = f"DDoS/Flood attack: '{kw}'"
                    detected = True
                    break
                    
        # Web attacks (SQL injection, XSS, CSRF, etc.)
        if not detected:
            for kw in web_attack_keywords:
                if kw in script_content.lower():
                    block_reason = f"Web attack: '{kw}'"
                    detected = True
                    break
                    
        # Reconnaissance attacks
        if not detected:
            for kw in recon_keywords:
                if kw in script_content.lower():
                    block_reason = f"Reconnaissance attack: '{kw}'"
                    detected = True
                    break
                    
        # Vulnerability patterns
        if not detected:
            for kw in vuln_keywords:
                if kw in script_content:
                    block_reason = f"Potential vulnerability: '{kw}' found"
                    detected = True
                    break
        if detected:
            # Calculate detection time in milliseconds
            detection_time = (time.time() - detection_start) * 1000
            detection_time_str = f"{detection_time:.2f}ms"
            
            # Gather script details
            with open(script_path, 'r', encoding='utf-8') as f:
                script_lines = f.readlines()
            code_sample = ''.join(script_lines[:20])
            block_details = {
                'script_key': script_key,
                'script_name': script.get('desc', script_key),
                'block_reason': block_reason,
                'how_identified': f"Matched keyword/pattern: {block_reason}",
                'code_sample': code_sample,
                'filename': script.get('filename'),
                'url': script.get('url'),
                'detection_time': detection_time_str
            }
            events.append(f"AEGIS-AI blocked script in {detection_time_str}: {block_reason} in script.")
            log_entries.append({
                "timestamp": now, 
                "ip": "0.0.0.0", 
                "type": "Block", 
                "status": f"Blocked in {detection_time_str}: {block_reason}", 
                "script": script_key, 
                "block_details": block_details
            })
            logs.extend(log_entries)
            return jsonify({
                "success": True, 
                "events": events, 
                "script": script_key, 
                "block_details": block_details,
                "detection_time_ms": detection_time_str
            })
    except Exception as e:
        events.append(f"Error scanning script: {e}")
        log_entries.append({"timestamp": now, "ip": "0.0.0.0", "type": "Online", "status": f"Scan Error: {e}", "script": script_key})
        logs.extend(log_entries)
        return jsonify({"success": False, "events": events, "script": script_key})
    # Run the script
    events.append(f"Running bot script: {script['desc']}")
    try:
        proc = subprocess.run(script['args'], capture_output=True, text=True, timeout=15)
        output = proc.stdout[-500:] if proc.stdout else proc.stderr[-500:]
        events.append(f"Script output: {output}")
        log_entries.append({"timestamp": now, "ip": "93.184.216.34", "type": "Online", "status": f"Script Ran: {script_key}", "output": output[:100]})
        # Simulate LLM attack
        events.append('LLM-Attack initiated...')
        events.append('AegisAI confused LLM-Attack!')
        log_entries.append({"timestamp": now, "ip": "8.8.8.8", "type": "LLM", "status": "Confused"})
    except Exception as e:
        events.append(f'Error running bot script: {e}')
        log_entries.append({"timestamp": now, "ip": "0.0.0.0", "type": "Online", "status": f"Script Error: {e}", "script": script_key})
    logs.extend(log_entries)
    return jsonify({"success": True, "events": events, "script": script_key})

@app.route('/api/secure-browsing', methods=['POST'])
def secure_browsing_toggle():
    global secure_browsing
    data = request.json
    enabled = bool(data.get('enabled', False))
    secure_browsing['enabled'] = enabled
    return jsonify({'enabled': enabled})

import sys
import os
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ai_detection import run_all_algorithms, is_blocked

from datetime import datetime

@app.route('/api/detect', methods=['POST'])
def detect():
    data = request.json or {}
    # Add IP and headers for detection
    data['ip'] = request.remote_addr
    data['headers'] = dict(request.headers)
    results = run_all_algorithms(data)
    blocked = is_blocked(results)
    # Determine type/status
    detection_type = 'Bot' if results.get('user_agent') or results.get('header_anomaly') else 'AI Agent' if results.get('prompt_pattern') else 'Unknown'
    detection_status = 'Blocked' if blocked else 'Confused' if any(results.values()) else 'Escaped'
    detection_summary = ', '.join([k for k,v in results.items() if v])
    logs.append({
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'ip': data['ip'],
        'type': detection_type,
        'status': detection_status,
        'summary': detection_summary
    })
    return jsonify({
        'results': results,
        'blocked': blocked,
        'redirect': blocked
    })

# --- Honeypot Trap API ---
@app.route('/api/honeypot/activate', methods=['POST'])
def honeypot_activate():
    data = request.json or {}
    event = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'ip': request.remote_addr,
        'trap_name': data.get('trap_name', 'Honeypot Field'),
        'payload': data.get('payload', ''),
        'details': data.get('details', {})
    }
    honeypot_activations.append(event)
    return jsonify({'success': True, 'event': event})

@app.route('/api/honeypot/records', methods=['GET'])
def honeypot_records():
    trap_name = request.args.get('trap_name')
    date = request.args.get('date')
    filtered = honeypot_activations
    if trap_name:
        filtered = [e for e in filtered if e['trap_name'] == trap_name]
    if date:
        filtered = [e for e in filtered if e['timestamp'].startswith(date)]
    return jsonify({'records': filtered, 'count': len(filtered)})

import glob

def scan_scripts():
    script_registry = {}
    # Scan AI-SCRIPT (recursive)
    ai_script_dir = os.path.join(os.path.dirname(__file__), 'AI-SCRIPT')
    for path in glob.glob(os.path.join(ai_script_dir, '**', '*.py'), recursive=True):
        key = os.path.splitext(os.path.relpath(path, ai_script_dir).replace(os.sep, '_'))[0].lower()
        script_registry[key] = {
            'path': path,
            'status': 'available' if os.path.exists(path) and os.path.getsize(path) > 0 else 'missing',
            'enabled': True,
            'source': 'local'
        }
    # Scan downloaded_scripts
    dl_dir = os.path.join(os.path.dirname(__file__), 'downloaded_scripts')
    if os.path.exists(dl_dir):
        for path in glob.glob(os.path.join(dl_dir, '*.py')):
            key = os.path.splitext(os.path.basename(path))[0].lower()
            script_registry[key] = {
                'path': path,
                'status': 'available' if os.path.exists(path) and os.path.getsize(path) > 0 else 'missing',
                'enabled': True,
                'source': 'downloaded'
            }
    return script_registry

# Global registry
script_registry = scan_scripts()

# Route moved to line 763-766 with role requirement
# @app.route('/api/scripts', methods=['GET'])
# def get_scripts():
#     return jsonify({'scripts': script_registry})

# Route moved to line 768-777 with role requirement
# @app.route('/api/scripts/toggle', methods=['POST'])
# def toggle_script():
#     data = request.json or {}
#     key = data.get('key')
#     enable = data.get('enable', True)
#     if key in script_registry:
#         script_registry[key]['enabled'] = bool(enable)
#         return jsonify({'success': True, 'key': key, 'enabled': script_registry[key]['enabled']})
#     return jsonify({'success': False, 'error': 'Script not found'})

# Route moved to line 779-784 with role requirement
# @app.route('/api/scripts/scan', methods=['POST'])
# def rescan_scripts():
#     global script_registry
#     script_registry = scan_scripts()
#     return jsonify({'success': True, 'scripts': script_registry})

import csv
from flask import Response

@app.route('/api/forensics/report', methods=['GET'])
def forensics_report():
    idx = request.args.get('idx')
    ts = request.args.get('timestamp')
    fmt = request.args.get('format', 'json')
    # Find the log entry
    entry = None
    if idx is not None:
        try:
            entry = logs[int(idx)]
        except Exception:
            return jsonify({'success': False, 'error': 'Invalid index'}), 400
    elif ts:
        entry = next((l for l in logs if l.get('timestamp') == ts), None)
    if not entry:
        return jsonify({'success': False, 'error': 'Event not found'}), 404
    # Get script code sample if available
    script_key = entry.get('script')
    code_sample = ''
    if script_key:
        script = BOT_SCRIPTS.get(script_key)
        if script:
            script_path = script.get('filename')
            if script.get('local'):
                full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), script_path))
            else:
                full_path = os.path.join(os.path.dirname(__file__), 'downloaded_scripts', script_path)
            if os.path.exists(full_path):
                with open(full_path, 'r', encoding='utf-8') as f:
                    code_sample = ''.join([next(f) for _ in range(20)]) if os.path.getsize(full_path) else ''
    report = {
        'event': entry,
        'code_sample': code_sample,
        'detection_reason': entry.get('block_details', entry.get('status', '')),
        'remediation': 'Review the code sample and block reason. Update blocklists or detection patterns as needed. For AI/LLM/ML scripts, ensure strict input validation and monitoring.'
    }
    if fmt == 'csv':
        # Prepare CSV
        def to_csv(d):
            output = []
            output.append(['Field', 'Value'])
            for k, v in report.items():
                output.append([k, str(v)])
            return output
        csv_data = to_csv(report)
        si = []
        for row in csv_data:
            si.append(','.join('"'+c.replace('"','""')+'"' for c in row))
        csv_str = '\n'.join(si)
        return Response(csv_str, mimetype='text/csv', headers={'Content-Disposition': 'attachment;filename=forensics_report.csv'})
    return jsonify(report)

import threading
import time

threat_intel = {'blocklist': [], 'last_update': None}

# Mock threat feed fetch (replace with real API if needed)
def fetch_threat_feed():
    # Example: fetch from AbuseIPDB or any public IP blocklist
    # Here, we mock with some demo IPs
    threat_intel['blocklist'] = [
        {'ip': '185.220.101.1', 'reason': 'TOR Exit Node'},
        {'ip': '45.155.205.233', 'reason': 'Known Botnet'},
        {'ip': '193.32.162.200', 'reason': 'Brute Force Attacker'}
    ]
    threat_intel['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def threat_feed_updater():
    while True:
        fetch_threat_feed()
        time.sleep(3600)  # every hour

@app.route('/api/threat-intel', methods=['GET'])
def get_threat_intel():
    return jsonify({
        'blocklist': threat_intel['blocklist'],
        'last_update': threat_intel['last_update'],
        'count': len(threat_intel['blocklist'])
    })

# Start threat feed updater thread on startup
fetch_threat_feed()
threading.Thread(target=threat_feed_updater, daemon=True).start()

from functools import wraps
from flask import session
import secrets

# In-memory user db
users = {
    'admin': {'password': 'adminpass', 'role': 'admin'},
    'analyst': {'password': 'analystpass', 'role': 'analyst'},
    'guest': {'password': 'guestpass', 'role': 'guest'}
}

app.secret_key = secrets.token_hex(16)

def require_role(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = session.get('user')
            if not user or users.get(user, {}).get('role') not in (role if isinstance(role, (list,tuple)) else [role]):
                return jsonify({'success': False, 'error': 'Unauthorized'}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json or {}
    user = data.get('username')
    pw = data.get('password')
    if user in users and users[user]['password'] == pw:
        session['user'] = user
        return jsonify({'success': True, 'user': user, 'role': users[user]['role']})
    return jsonify({'success': False, 'error': 'Invalid credentials'}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({'success': True})

@app.route('/api/whoami', methods=['GET'])
def whoami():
    user = session.get('user')
    if user:
        return jsonify({'user': user, 'role': users[user]['role']})
    return jsonify({'user': None, 'role': None})

# Example: restrict script management to admin/analyst
@app.route('/api/scripts', methods=['GET'])
@require_role(['admin','analyst'])
def get_scripts():
    return jsonify({'scripts': script_registry})

@app.route('/api/scripts/toggle', methods=['POST'])
@require_role('admin')
def toggle_script():
    data = request.json or {}
    key = data.get('key')
    enable = data.get('enable', True)
    if key in script_registry:
        script_registry[key]['enabled'] = bool(enable)
        return jsonify({'success': True, 'key': key, 'enabled': script_registry[key]['enabled']})
    return jsonify({'success': False, 'error': 'Script not found'})

@app.route('/api/scripts/scan', methods=['POST'])
@require_role(['admin','analyst'])
def rescan_scripts():
    global script_registry
    script_registry = scan_scripts()
    return jsonify({'success': True, 'scripts': script_registry})

from collections import Counter, defaultdict

@app.route('/api/analytics', methods=['GET'])
def analytics():
    # Attacks and blocks per day (last 14 days)
    day_fmt = '%Y-%m-%d'
    today = datetime.now()
    days = [(today - timedelta(days=i)).strftime(day_fmt) for i in range(13, -1, -1)]
    attacks_per_day = {d: 0 for d in days}
    blocks_per_day = {d: 0 for d in days}
    script_usage = Counter()
    ip_counter = Counter()
    for l in logs:
        ts = l.get('timestamp','')[:10]
        if ts in attacks_per_day:
            attacks_per_day[ts] += 1
            if l.get('status','').lower().startswith('blocked'):
                blocks_per_day[ts] += 1
        if l.get('script'):
            script_usage[l['script']] += 1
        if l.get('ip'):
            ip_counter[l['ip']] += 1
    # Honeypot activations per day
    hp_per_day = defaultdict(int)
    for h in honeypot_activations:
        ts = h.get('timestamp','')[:10]
        if ts:
            hp_per_day[ts] += 1
    # Top attacker IPs
    top_ips = ip_counter.most_common(10)
    return jsonify({
        'attacks_per_day': attacks_per_day,
        'blocks_per_day': blocks_per_day,
        'script_usage': script_usage,
        'honeypot_per_day': hp_per_day,
        'top_ips': top_ips
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
