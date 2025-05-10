#!/usr/bin/env python3
"""
CSRF Attack Demo
This script demonstrates Cross-Site Request Forgery (CSRF) attacks against web forms.
"""

import random
import time
from typing import Dict, List, Any, Optional

# Script metadata
NAME = "CSRF Attack Demo"
DESCRIPTION = "Demonstrates Cross-Site Request Forgery (CSRF) attacks against web forms"

def run(**kwargs):
    """Run the CSRF attack demo"""
    # Generate a random IP address for the attacker
    ip_address = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
    
    # Generate a timestamp for the attack
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Attack-specific parameters
    target_actions = ["change-password", "update-profile", "transfer-funds", "delete-account", "add-admin-user"]
    csrf_methods = ["GET", "POST", "PUT", "DELETE"]
    target_domains = ["bank.example.com", "admin.example.com", "account.example.com", "profile.example.com"]
    referrer_domains = ["malicious.example.com", "attacker.example.com", "evil.example.com", "phishing.example.com"]
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
    ]
    
    # Select random parameters for this run
    target_action = random.choice(target_actions)
    csrf_method = random.choice(csrf_methods)
    target_domain = random.choice(target_domains)
    referrer_domain = random.choice(referrer_domains)
    user_agent = random.choice(user_agents)
    
    # Generate events
    events = [
        f"Starting CSRF attack demo...",
        f"Target domain: {target_domain}",
        f"Target action: {target_action}",
        f"HTTP method: {csrf_method}",
        f"Creating hidden form on {referrer_domain}...",
        f"Submitting cross-domain request to {target_domain}/{target_action}...",
    ]
    
    # Add the blocked event with detection time
    detection_time = f"{random.uniform(0.8, 3.0):.1f}"
    events.append(f"AegisAI blocked CSRF attack in {detection_time}ms: Invalid CSRF token detected")
    
    # Generate block details
    block_details = {
        "attack_type": "Cross-Site Request Forgery (CSRF)",
        "detection_method": "Token Validation",
        "confidence": round(random.uniform(95.0, 99.0), 1),
        "ip_address": ip_address,
        "timestamp": timestamp,
        "target_domain": target_domain,
        "target_action": target_action,
        "http_method": csrf_method,
        "referrer_domain": referrer_domain,
        "user_agent": user_agent,
        "csrf_token": "Missing or invalid",
        "same_origin": False,
        "protection_mechanism": "Double-submit cookie pattern"
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
    # Simulate detection for CSRF attack
    time.sleep(0.002)  # 2ms
    
    # Return the result
    return {
        "success": True,
        "detection_time": 2.0,
        "script": NAME
    }
