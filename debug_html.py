import requests
try:
    response = requests.get('http://127.0.0.1:8000/')
    print(f"Status: {response.status_code}")
    content = response.text
    head_end = content.find('</head>')
    with open('debug_head.txt', 'w', encoding='utf-8') as f:
        f.write(content[:head_end+7])
except Exception as e:
    print(e)
