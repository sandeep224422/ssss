#!/usr/bin/env python3
"""
Test script for API key authentication
This script tests the API key middleware functionality
"""

import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BASE_URL = "http://localhost:5011"
API_KEY = os.getenv('API_KEY', 'default_secret_key')

def test_api_key_authentication():
    """Test API key authentication with different scenarios"""
    
    print("Testing API Key Authentication...")
    print(f"Using API Key: {API_KEY}")
    print(f"Base URL: {BASE_URL}")
    print("-" * 50)
    
    # Test 1: Valid API key
    print("Test 1: Valid API key")
    try:
        response = requests.get(
            f"{BASE_URL}/info",
            headers={"x-api-key": API_KEY}
        )
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Valid API key works correctly")
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure the API is running.")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print()
    
    # Test 2: Missing API key
    print("Test 2: Missing API key")
    try:
        response = requests.get(f"{BASE_URL}/info")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 403:
            print("✅ Missing API key correctly rejected")
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure the API is running.")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print()
    
    # Test 3: Invalid API key
    print("Test 3: Invalid API key")
    try:
        response = requests.get(
            f"{BASE_URL}/info",
            headers={"x-api-key": "invalid_key"}
        )
        print(f"Status Code: {response.status_code}")
        if response.status_code == 403:
            print("✅ Invalid API key correctly rejected")
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure the API is running.")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print()
    
    # Test 4: Documentation endpoints (should be accessible without API key)
    print("Test 4: Documentation endpoints (should be accessible without API key)")
    try:
        response = requests.get(f"{BASE_URL}/docs")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Documentation endpoint accessible without API key")
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure the API is running.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_api_key_authentication()
