#!/usr/bin/env python3
"""
Port Scanner
This script simulates scanning for open ports on a target system.
"""

import random
import time
from typing import Dict, List, Any, Optional

# Script metadata
NAME = "Port Scanner"
DESCRIPTION = "Scans for open ports on a target system"

def run(**kwargs):
    """Run the port scanner simulation"""
    # Generate a random IP address for the attacker
    ip_address = f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
    
    # Generate a timestamp for the attack
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Attack-specific parameters
    target_systems = ["web-server", "database-server", "mail-server", "file-server", "application-server"]
    scan_types = ["TCP SYN scan", "TCP connect scan", "UDP scan", "FIN scan", "XMAS scan", "NULL scan"]
    port_ranges = ["1-1024", "1-65535", "20-30,80,443,8080", "21-23,25,80,110,143,443,3306,5432"]
    scan_speeds = ["slow", "normal", "aggressive", "insane"]
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 1433, 3306, 3389, 5432, 8080, 8443]
    
    # Select random parameters for this run
    target_system = random.choice(target_systems)
    scan_type = random.choice(scan_types)
    port_range = random.choice(port_ranges)
    scan_speed = random.choice(scan_speeds)
    
    # Generate a list of "discovered" open ports
    open_ports = random.sample(common_ports, random.randint(3, 8))
    open_ports.sort()
    
    # Generate events
    events = [
        f"Starting port scan simulation...",
        f"Target: {target_system}",
        f"Scan type: {scan_type}",
        f"Port range: {port_range}",
        f"Scan speed: {scan_speed}",
        f"Scanning ports...",
    ]
    
    # Add the blocked event with detection time
    detection_time = f"{random.uniform(1.0, 4.0):.1f}"
    events.append(f"AegisAI blocked port scan in {detection_time}ms: Suspicious port scanning activity detected")
    
    # Generate block details
    block_details = {
        "attack_type": "Port Scanning",
        "detection_method": "Traffic Analysis",
        "confidence": round(random.uniform(93.0, 98.0), 1),
        "ip_address": ip_address,
        "timestamp": timestamp,
        "target_system": target_system,
        "scan_type": scan_type,
        "port_range": port_range,
        "scan_speed": scan_speed,
        "open_ports_found": open_ports,
        "packets_sent": random.randint(100, 5000),
        "scan_duration": f"{random.uniform(2.0, 30.0):.1f} seconds"
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
    # Simulate detection for port scanning
    time.sleep(0.0025)  # 2.5ms
    
    # Return the result
    return {
        "success": True,
        "detection_time": 2.5,
        "script": NAME
    }
