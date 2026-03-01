import requests
import binascii

# Check Headers
try:
    response = requests.get('http://127.0.0.1:8000/static/css/style.css')
    print(f"Status: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-Type')}")
except Exception as e:
    print(f"Request Error: {e}")

# Check File Encoding (first 10 bytes)
try:
    with open('static/css/style.css', 'rb') as f:
        content = f.read(10)
        print(f"First 10 bytes hex: {binascii.hexlify(content)}")
except Exception as e:
    print(f"File Error: {e}")
