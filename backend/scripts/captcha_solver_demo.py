#!/usr/bin/env python3
"""
CAPTCHA Solver Demo
This script demonstrates automated CAPTCHA solving.
"""

import random
import time
from typing import Dict, List, Any, Optional

# Script metadata
NAME = "CAPTCHA Solver Demo"
DESCRIPTION = "Demonstrates automated CAPTCHA solving"

def run(**kwargs):
    """Run the CAPTCHA solver demo"""
    # Generate a random IP address for the attacker
    ip_address = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
    
    # Generate a timestamp for the attack
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Attack-specific parameters
    captcha_types = ["text-based", "image-based", "audio-based", "puzzle", "behavioral", "invisible"]
    solving_techniques = ["OCR", "computer-vision", "deep-learning", "audio-processing", "browser-automation"]
    model_types = ["CNN", "RNN", "LSTM", "Transformer", "ResNet", "Custom neural network"]
    target_sites = ["e-commerce", "banking", "social-media", "email", "government", "ticketing"]
    accuracy_rates = [75, 80, 85, 90, 95]  # percentage
    
    # Select random parameters for this run
    captcha_type = random.choice(captcha_types)
    solving_technique = random.choice(solving_techniques)
    model_type = random.choice(model_types)
    target_site = random.choice(target_sites)
    accuracy_rate = random.choice(accuracy_rates)
    
    # Generate events
    events = [
        f"Starting CAPTCHA solver demo...",
        f"CAPTCHA type: {captcha_type}",
        f"Solving technique: {solving_technique}",
        f"Model type: {model_type}",
        f"Target site type: {target_site}",
        f"Attempting to solve CAPTCHA...",
    ]
    
    # Add the blocked event with detection time
    detection_time = f"{random.uniform(0.7, 2.2):.1f}"
    events.append(f"AegisAI blocked CAPTCHA solver in {detection_time}ms: ML-based solving attempt detected")
    
    # Generate block details
    block_details = {
        "attack_type": "Automated CAPTCHA Solving",
        "detection_method": "ML Detection",
        "confidence": round(random.uniform(93.0, 98.0), 1),
        "ip_address": ip_address,
        "timestamp": timestamp,
        "captcha_type": captcha_type,
        "solving_technique": solving_technique,
        "model_type": model_type,
        "target_site": target_site,
        "accuracy_rate": f"{accuracy_rate}%",
        "processing_time": f"{random.uniform(0.2, 3.0):.1f} seconds",
        "dataset_size": f"{random.randint(10000, 1000000)} samples",
        "model_parameters": f"{random.randint(1, 100)} million",
        "training_time": f"{random.randint(1, 48)} hours",
        "challenge_difficulty": random.choice(["easy", "medium", "hard", "very hard"])
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
    # Simulate detection for CAPTCHA solver
    time.sleep(0.0015)  # 1.5ms
    
    # Return the result
    return {
        "success": True,
        "detection_time": 1.5,
        "script": NAME
    }