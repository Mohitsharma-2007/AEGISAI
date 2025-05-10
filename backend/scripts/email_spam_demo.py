#!/usr/bin/env python3
"""
Email Spam Demo
This script demonstrates email spam attacks.
"""

import random
import time
from typing import Dict, List, Any, Optional

# Script metadata
NAME = "Email Spam Demo"
DESCRIPTION = "Demonstrates email spam attacks"

def run(**kwargs):
    """Run the email spam demo"""
    # Generate a random IP address for the attacker
    ip_address = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
    
    # Generate a timestamp for the attack
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Attack-specific parameters
    spam_types = ["phishing", "advertising", "malware", "scam", "bulk"]
    email_volumes = [100, 500, 1000, 5000, 10000]  # emails per hour
    sender_domains = ["spam-domain.com", "fake-news.org", "not-real-company.net", "special-offer.info", "free-stuff.xyz"]
    subject_lines = [
        "URGENT: Your account has been compromised",
        "You've won a free iPhone!",
        "Important security update required",
        "Your package is waiting for delivery",
        "Exclusive offer just for you"
    ]
    attachment_types = ["none", "pdf", "doc", "zip", "exe"]
    spam_techniques = ["open relay", "compromised accounts", "botnet", "snowshoe spamming", "direct sending"]
    
    # Select random parameters for this run
    spam_type = random.choice(spam_types)
    email_volume = random.choice(email_volumes)
    sender_domain = random.choice(sender_domains)
    subject_line = random.choice(subject_lines)
    attachment_type = random.choice(attachment_types)
    spam_technique = random.choice(spam_techniques)
    
    # Generate events
    events = [
        f"Starting email spam demo...",
        f"Spam type: {spam_type}",
        f"Email volume: {email_volume} emails per hour",
        f"Sender domain: {sender_domain}",
        f"Subject line: '{subject_line}'",
        f"Attachment type: {attachment_type}",
        f"Spam technique: {spam_technique}",
    ]
    
    # Add the blocked event with detection time
    detection_time = f"{random.uniform(0.5, 2.0):.1f}"
    events.append(f"AegisAI blocked email spam in {detection_time}ms: Spam content detected")
    
    # Generate block details
    block_details = {
        "attack_type": "Email Spam",
        "detection_method": "Content Analysis",
        "confidence": round(random.uniform(92.0, 98.0), 1),
        "ip_address": ip_address,
        "timestamp": timestamp,
        "spam_type": spam_type,
        "email_volume": email_volume,
        "sender_domain": sender_domain,
        "subject_line": subject_line,
        "attachment_type": attachment_type,
        "spam_technique": spam_technique,
        "spam_score": round(random.uniform(8.0, 10.0), 1),
        "spf_check": "fail",
        "dkim_check": "fail",
        "dmarc_check": "fail",
        "blacklist_status": "listed"
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
    # Simulate detection for email spam
    time.sleep(0.0014)  # 1.4ms
    
    # Return the result
    return {
        "success": True,
        "detection_time": 1.4,
        "script": NAME
    }