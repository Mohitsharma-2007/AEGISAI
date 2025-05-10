#!/usr/bin/env python3
"""
Brute Force Demo
This script demonstrates brute force password attacks.
"""

import random
import time
from typing import Dict, List, Any, Optional

# Script metadata
NAME = "Brute Force Demo"
DESCRIPTION = "Demonstrates brute force password attacks"

def run(**kwargs):
    """Run the brute force demo"""
    # Generate a random IP address for the attacker
    ip_address = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
    
    # Generate a timestamp for the attack
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Attack-specific parameters
    target_services = ["ssh", "ftp", "rdp", "web-login", "database", "email"]
    attack_methods = ["dictionary", "hybrid", "mask", "incremental"]
    password_lists = ["rockyou.txt", "darkweb2017-top10000.txt", "common-passwords-win.txt", "probable-v2-top12000.txt"]
    attack_speeds = [10, 50, 100, 500, 1000]  # attempts per minute
    tools = ["hydra", "medusa", "ncrack", "hashcat", "john", "custom script"]
    
    # Sample usernames for demonstration
    sample_usernames = ["admin", "root", "user", "administrator", "system"]
    
    # Select random parameters for this run
    target_service = random.choice(target_services)
    attack_method = random.choice(attack_methods)
    password_list = random.choice(password_lists)
    attack_speed = random.choice(attack_speeds)
    tool = random.choice(tools)
    username = random.choice(sample_usernames)
    
    # Generate a list of attempted passwords
    num_attempts = random.randint(5, 15)
    password_attempts = []
    for i in range(num_attempts):
        password_attempts.append(f"password{i}")
    
    # Generate events
    events = [
        f"Starting brute force demo...",
        f"Target service: {target_service}",
        f"Username: {username}",
        f"Attack method: {attack_method}",
        f"Password list: {password_list}",
        f"Attack speed: {attack_speed} attempts per minute",
        f"Tool: {tool}",
        f"Attempting passwords...",
    ]
    
    # Add the blocked event with detection time
    detection_time = f"{random.uniform(0.8, 3.0):.1f}"
    events.append(f"AegisAI blocked brute force attack in {detection_time}ms: Multiple failed login attempts detected")
    
    # Generate block details
    block_details = {
        "attack_type": "Brute Force Password Attack",
        "detection_method": "Login Attempt Analysis",
        "confidence": round(random.uniform(95.0, 99.0), 1),
        "ip_address": ip_address,
        "timestamp": timestamp,
        "target_service": target_service,
        "username": username,
        "attack_method": attack_method,
        "password_list": password_list,
        "attack_speed": attack_speed,
        "tool": tool,
        "password_attempts": password_attempts,
        "failed_attempts": len(password_attempts),
        "account_lockout": True,
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
    # Simulate detection for brute force attack
    time.sleep(0.0018)  # 1.8ms
    
    # Return the result
    return {
        "success": True,
        "detection_time": 1.8,
        "script": NAME
    }
