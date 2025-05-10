#!/usr/bin/env python3
"""
Form Submitter
This script simulates automated form submission attacks.
"""

import random
import time
from typing import Dict, List, Any, Optional

# Script metadata
NAME = "Form Submitter"
DESCRIPTION = "Simulates automated form submission attacks"

def run(**kwargs):
    """Run the form submitter attack"""
    # Generate a random IP address for the attacker
    ip_address = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
    
    # Generate a timestamp for the attack
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Attack-specific parameters
    form_types = ["contact", "registration", "login", "comment", "newsletter", "feedback"]
    submission_rates = [10, 20, 50, 100, 200]  # submissions per minute
    field_values = {
        "name": ["John Doe", "Jane Smith", "Bob Johnson", "Alice Brown", "Random User"],
        "email": ["user@example.com", "test@test.com", "random@mail.com", "fake@fake.com", "spam@spam.com"],
        "message": ["Test message", "Please contact me", "This is spam", "Automated submission", "Bot message"],
        "subject": ["Inquiry", "Help needed", "Contact request", "Information", "Support"]
    }
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
    ]
    
    # Select random parameters for this run
    form_type = random.choice(form_types)
    submission_rate = random.choice(submission_rates)
    user_agent = random.choice(user_agents)
    
    # Generate form data
    form_data = {}
    for field, values in field_values.items():
        if random.random() > 0.3:  # 70% chance to include each field
            form_data[field] = random.choice(values)
    
    # Generate events
    events = [
        f"Starting form submission attack...",
        f"Target form: {form_type} form",
        f"Submission rate: {submission_rate} per minute",
        f"Preparing form data...",
        f"Submitting form data: {form_data}",
    ]
    
    # Add the blocked event with detection time
    detection_time = f"{random.uniform(0.5, 2.5):.1f}"
    events.append(f"AegisAI blocked form submission attack in {detection_time}ms: Automated submission pattern detected")
    
    # Generate block details
    block_details = {
        "attack_type": "Automated Form Submission",
        "detection_method": "Behavior Analysis",
        "confidence": round(random.uniform(92.0, 98.0), 1),
        "ip_address": ip_address,
        "timestamp": timestamp,
        "form_type": form_type,
        "submission_rate": submission_rate,
        "form_data": form_data,
        "user_agent": user_agent,
        "captcha_status": "Failed or bypassed",
        "honeypot_triggered": random.choice([True, False]),
        "time_spent_on_form": f"{random.uniform(0.5, 3.0):.1f} seconds"
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
    # Simulate detection for form submission attack
    time.sleep(0.0018)  # 1.8ms
    
    # Return the result
    return {
        "success": True,
        "detection_time": 1.8,
        "script": NAME
    }