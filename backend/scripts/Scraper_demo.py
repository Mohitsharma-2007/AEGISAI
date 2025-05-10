#!/usr/bin/env python3
"""
Web Scraper Demo
This script demonstrates web scraping attacks.
"""

import random
import time
from typing import Dict, List, Any, Optional

# Script metadata
NAME = "Web Scraper Demo"
DESCRIPTION = "Demonstrates web scraping attacks"

def run(**kwargs):
    """Run the web scraper demo"""
    # Generate a random IP address for the attacker
    ip_address = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
    
    # Generate a timestamp for the attack
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Attack-specific parameters
    target_sites = ["e-commerce", "content-site", "social-media", "job-board", "real-estate", "directory"]
    scraping_tools = ["BeautifulSoup", "Scrapy", "Selenium", "Puppeteer", "Playwright", "Custom script"]
    data_targets = ["product-info", "user-profiles", "contact-details", "pricing-data", "images", "reviews"]
    request_rates = [10, 50, 100, 200, 500]  # requests per minute
    proxy_usage = ["none", "rotating-proxies", "vpn", "tor", "residential-proxies"]
    
    # Select random parameters for this run
    target_site = random.choice(target_sites)
    scraping_tool = random.choice(scraping_tools)
    data_target = random.choice(data_targets)
    request_rate = random.choice(request_rates)
    proxy = random.choice(proxy_usage)
    
    # Generate events
    events = [
        f"Starting web scraper demo...",
        f"Target site type: {target_site}",
        f"Scraping tool: {scraping_tool}",
        f"Data target: {data_target}",
        f"Request rate: {request_rate} requests per minute",
        f"Proxy usage: {proxy}",
        f"Initiating scraping sequence...",
    ]
    
    # Add the blocked event with detection time
    detection_time = f"{random.uniform(0.8, 3.0):.1f}"
    events.append(f"AegisAI blocked web scraper in {detection_time}ms: Automated scraping pattern detected")
    
    # Generate block details
    block_details = {
        "attack_type": "Web Scraping",
        "detection_method": "Behavior Analysis",
        "confidence": round(random.uniform(92.0, 97.0), 1),
        "ip_address": ip_address,
        "timestamp": timestamp,
        "target_site": target_site,
        "scraping_tool": scraping_tool,
        "data_target": data_target,
        "request_rate": request_rate,
        "proxy_usage": proxy,
        "user_agent": "Mozilla/5.0 (compatible; ScraperBot/1.0; +http://example.com/bot)",
        "request_pattern": "sequential",
        "pages_accessed": random.randint(20, 500),
        "data_extracted": f"{random.randint(1, 100)} MB",
        "captcha_encounters": random.randint(0, 10)
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
    # Simulate detection for web scraper
    time.sleep(0.0021)  # 2.1ms
    
    # Return the result
    return {
        "success": True,
        "detection_time": 2.1,
        "script": NAME
    }