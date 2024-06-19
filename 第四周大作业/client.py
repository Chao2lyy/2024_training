import requests
import json

def query_image(image_name):
    '''根据图片名查询'''
    url = f"http://localhost:8000/query_by_image/{image_name}"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        print(json.dumps(result, indent=4))
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    while True:
        image_name = input("Enter image name (or 'exit' to quit): ")
        if image_name.lower() == 'exit':
            break
        query_image(image_name)