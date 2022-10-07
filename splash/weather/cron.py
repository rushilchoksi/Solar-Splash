import sys
import requests

apiResponse = requests.get(f'http://localhost:8000/ask_sprinkle?clientID={sys.argv[1]}')
print(apiResponse.status_code)
print(apiResponse.text)
