#!/usr/bin/env python3
"""
XSS Payload Demo
This script demonstrates Cross-Site Scripting (XSS) attacks with various payloads.
"""

import random
import time
from typing import Dict, List, Any, Optional

# Script metadata
NAME = "XSS Payload Demo"
DESCRIPTION = "Demonstrates Cross-Site Scripting (XSS) attacks with various payloads"

def run(**kwargs):
    """Run the XSS payload demo"""
    # Generate a random IP address for the attacker
    ip_address = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
    
    # Generate a timestamp for the attack
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Attack-specific parameters
    target_fields = ["comment", "search", "username", "bio", "message"]
    xss_payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<svg onload=alert('XSS')>",
        "<iframe src=\"javascript:alert('XSS')\"></iframe>",
        "<body onload=alert('XSS')>",
        "<a href=\"javascript:alert('XSS')\">Click me</a>",
        "<div onmouseover=\"alert('XSS')\">Hover me</div>"
    ]
    xss_types = ["Reflected", "Stored", "DOM-based"]
    encoding_types = ["None", "URL", "HTML", "Base64", "Double encoding"]
    target_browsers = ["Chrome", "Firefox", "Safari", "Edge"]
    target_pages = ["blog-post", "user-profile", "search-results", "product-review", "forum-thread"]
    
    # Select random parameters for this run
    target_field = random.choice(target_fields)
    xss_payload = random.choice(xss_payloads)
    xss_type = random.choice(xss_types)
    encoding_type = random.choice(encoding_types)
    target_browser = random.choice(target_browsers)
    target_page = random.choice(target_pages)
    
    # Generate events
    events = [
        f"Starting XSS payload demo...",
        f"Target page: {target_page}",
        f"Target field: {target_field}",
        f"XSS type: {xss_type}",
        f"Encoding: {encoding_type}",
        f"Injecting XSS payload: {xss_payload}",
    ]
    
    # Add the blocked event with detection time
    detection_time = f"{random.uniform(0.5, 2.0):.1f}"
    events.append(f"AegisAI blocked XSS attack in {detection_time}ms: Malicious script detected in {target_field}")
    
    # Generate block details
    block_details = {
        "attack_type": "Cross-Site Scripting (XSS)",
        "detection_method": "Pattern Matching",
        "confidence": round(random.uniform(95.0, 99.0), 1),
        "ip_address": ip_address,
        "timestamp": timestamp,
        "target_field": target_field,
        "xss_payload": xss_payload,
        "xss_type": xss_type,
        "encoding_type": encoding_type,
        "target_browser": target_browser,
        "target_page": target_page,
        "sanitization_applied": True,
        "csp_headers": "script-src 'self'; object-src 'none'"
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
    # Simulate detection for XSS attack
    time.sleep(0.0015)  # 1.5ms
    
    # Return the result
    return {
        "success": True,
        "detection_time": 1.5,
        "script": NAME
    }