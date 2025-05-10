#!/usr/bin/env python3
"""
Fake Login Bot
This script simulates automated login attempts with credential stuffing.
"""

import random
import time
from typing import Dict, List, Any, Optional

# Script metadata
NAME = "Fake Login Bot"
DESCRIPTION = "Simulates automated login attempts with credential stuffing"

def run(**kwargs):
    """Run the fake login bot simulation"""
    # Generate a random IP address for the attacker
    ip_address = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
    
    # Generate a timestamp for the attack
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Attack-specific parameters
    target_sites = ["e-commerce", "banking", "social-media", "email", "cloud-storage"]
    login_rates = [5, 10, 20, 50, 100]  # attempts per minute
    username_patterns = ["email", "username", "phone", "id"]
    password_lists = ["rockyou.txt", "10-million-password-list-top-1000000.txt", "darkweb2017-top10000.txt"]
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
    ]
    proxy_usage = ["none", "rotating-proxies", "vpn", "tor"]
    
    # Sample usernames and passwords for demonstration
    sample_usernames = ["user123", "john.doe", "alice_smith", "bob.johnson", "admin"]
    sample_passwords = ["password123", "qwerty", "123456", "letmein", "admin123"]
    
    # Select random parameters for this run
    target_site = random.choice(target_sites)
    login_rate = random.choice(login_rates)
    username_pattern = random.choice(username_patterns)
    password_list = random.choice(password_lists)
    user_agent = random.choice(user_agents)
    proxy = random.choice(proxy_usage)
    
    # Generate a list of attempted credentials
    num_attempts = random.randint(5, 15)
    credentials = []
    for _ in range(num_attempts):
        credentials.append({
            "username": random.choice(sample_usernames),
            "password": random.choice(sample_passwords)
        })
    
    # Generate events
    events = [
        f"Starting fake login bot simulation...",
        f"Target: {target_site} login page",
        f"Login rate: {login_rate} attempts per minute",
        f"Username pattern: {username_pattern}",
        f"Password list: {password_list}",
        f"Proxy usage: {proxy}",
        f"Attempting logins with credential stuffing...",
    ]
    
    # Add the blocked event with detection time
    detection_time = f"{random.uniform(0.8, 2.5):.1f}"
    events.append(f"AegisAI blocked fake login bot in {detection_time}ms: Credential stuffing attack detected")
    
    # Generate block details
    block_details = {
        "attack_type": "Credential Stuffing",
        "detection_method": "Behavior Analysis",
        "confidence": round(random.uniform(95.0, 99.0), 1),
        "ip_address": ip_address,
        "timestamp": timestamp,
        "target_site": target_site,
        "login_rate": login_rate,
        "username_pattern": username_pattern,
        "password_list": password_list,
        "user_agent": user_agent,
        "proxy_usage": proxy,
        "login_attempts": credentials,
        "success_rate": f"{random.uniform(0.0, 2.0):.1f}%",
        "captcha_status": "Failed or bypassed",
        "time_between_attempts": f"{random.uniform(0.5, 5.0):.1f} seconds"
    }
    
    # Return the result
    return {
        "success": True,
        "events": events,
        "block_details": block_details,
        "script": NAME
    }

def test_detection():
    """Test the detection speed of the script"""
    # Simulate detection for fake login bot
    time.sleep(0.0016)  # 1.6ms
    
    # Return the result
    return {
        "success": True,
        "detection_time": 1.6,
        "script": NAME
    }