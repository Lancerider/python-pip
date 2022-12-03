import requests

def get_categories():
    data = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(data.status_code)
    print(data.text)
    categories = data.json()
    for category in categories:
        print(category['name'])