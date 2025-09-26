#!/usr/bin/env python3
"""Setup script for the Alerting & Notification Platform"""

import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and print output"""
    print(f"Running: {command}")
    result = subprocess.run(command.split(), capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    else:
        print(f"Success: {result.stdout}")

def setup_project():
    """Setup the entire project"""
    print("🚀 Setting up Alerting & Notification Platform...")
    
    # Install dependencies
    print("\n📦 Installing dependencies...")
    run_command("pip install -r requirements.txt")
    
    # Create database directory if it doesn't exist
    if not os.path.exists('instance'):
        os.makedirs('instance')
        print("📁 Created instance directory for database")
    
    print("\n✅ Setup completed successfully!")
    print("\n🎯 Next steps:")
    print("1. Run: python app.py")
    print("2. Test API endpoints using the examples in README.md")
    print("3. Check health: curl http://127.0.0.1:5000/health")

if __name__ == "__main__":
    setup_project()
