# 13A Sample modules: Request

## Request 

`requests` is a package to interact with web services.

Create a virtual env in the `request_tutorial` subfolder and activate it.

### Get call

```python
import requests

BASE_URL = 'https://fakestoreapi.com'

response = requests.get(f"{BASE_URL}/products")
print(response.json()) #print response json
print(response.status_code) #200


query_params = {
    "limit": 3
}

response = requests.get(f"{BASE_URL}/products", params=query_params)  #GET /products?limit=x
print(response.json())

response = requests.get(f"{BASE_URL}/products/2")
print(response.json())
```

### Post call

```python
import requests

BASE_URL = 'https://fakestoreapi.com'

new_product = {
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}

response = requests.post(f"{BASE_URL}/products", json=new_product)
print(response.json()) # {'id': 21, 'title': 'test product', 'price': 13.5, 'description': 'lorem ipsum set', 'image': 'https://i.pravatar.cc', 'category': 'electronic'}
```

If we don't use the json argument, we have to make the POST request like this:

```python
new_product_json_string = json.dumps(new_product) #converts the object (dictionary) to json formatted string

headers = {
    "Content-Type": "application/json"
}

response = requests.post(f"{BASE_URL}/products", data=json.dumps(new_product), headers=headers)
print(response.json())
```
