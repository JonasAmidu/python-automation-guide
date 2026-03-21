import urllib.request
import urllib.parse

# Read the file
with open(r'C:\Users\alish\Desktop\python-automation-guide\index.html', 'rb') as f:
    data = f.read()

# Create request to 0x0.st
req = urllib.request.Request(
    'https://0x0.st',
    data=data,
    method='POST'
)
req.add_header('Content-Type', 'application/octet-stream')
req.add_header('Content-Disposition', 'attachment; filename=index.html')

try:
    response = urllib.request.urlopen(req, timeout=30)
    print(response.read().decode())
except Exception as e:
    print(f'Error: {e}')
