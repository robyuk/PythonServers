This repository contains web servers written in Python
1. basic_server.py - This uses the internal python libraries to make a basic web server.  The example contains a class to override the default behaviour of the python web server.
2. flask_server.py - This uses the Flask library to make a basic web server.  The example contains a class to override the default behaviour of the Flask web server.
3. rest-api.py - This uses the Flask library to make a basic REST API.  The example contains enpoints to retrieve, add, update and delete data.

## How to run the servers
1. Clone the repository
2. Open a terminal and navigate to the repository
3. Run the server you want to use
    - For the basic server run `python basic_server.py`
    - For the Flask server run `python flask_server.py`
    - For the REST API run `python rest-api.py`
4. Open a web browser and navigate to `http://localhost:8080` for the basic server or `http://localhost:5000` for the Flask server or REST API
5. To stop the server press `Ctrl+C` in the terminal


## To test the REST API using bash

Here are some `curl` commands to test the endpoints of your REST API:

1. **GET** all products:
    ```sh
    curl -X GET http://localhost:5000/products
    ```

2. **GET** a specific product by ID:
    ```sh
    curl -X GET http://localhost:5000/products/1
    ```

3. **POST** a new product:
    ```sh
    curl -X POST http://localhost:5000/products -H "Content-Type: application/json" -d '{"id": 6, "name": "Monitor", "price": 199.99}'
    ```

4. **PUT** to update an existing product by ID:
    ```sh
    curl -X PUT http://localhost:5000/products/1 -H "Content-Type: application/json" -d '{"name": "Gaming Laptop", "price": 1299.99}'
    ```

5. **DELETE** a product by ID:
    ```sh
    curl -X DELETE http://localhost:5000/products/1
    ```

6. **PATCH** to partially update a product by ID:
    ```sh
    curl -X PATCH http://localhost:5000/products/1 -H "Content-Type: application/json" -d '{"price": 1099.99}'
    ```

## To test the REST API using Windows Powershell

Here are commands using `Invoke-WebRequest` in PowerShell:

1. **GET** all products:
    ```powershell
    Invoke-WebRequest -Uri http://localhost:5000/products -Method GET
    ```

2. **GET** a specific product by ID:
    ```powershell
    Invoke-WebRequest -Uri http://localhost:5000/products/1 -Method GET
    ```

3. **POST** a new product:
    ```powershell
    $body = '{"id": 6, "name": "Monitor", "price": 199.99}'
    Invoke-WebRequest -Uri http://localhost:5000/products -Method POST -ContentType "application/json" -Body $body
    ```

4. **PUT** to update an existing product by ID:
    ```powershell
    $body = '{"name": "Gaming Laptop", "price": 1299.99}'
    Invoke-WebRequest -Uri http://localhost:5000/products/1 -Method PUT -ContentType "application/json" -Body $body
    ```

5. **DELETE** a product by ID:
    ```powershell
    Invoke-WebRequest -Uri http://localhost:5000/products/1 -Method DELETE
    ```

6. **PATCH** to partially update a product by ID:
    ```powershell
    $body = '{"price": 1099.99}'
    Invoke-WebRequest -Uri http://localhost:5000/products/1 -Method PATCH -ContentType "application/json" -Body $body
    ```
   
## To test the blog server

### Install required packages
pip install Flask Flask-HTTPAuth werkzeug

### Run the Flask server
python blog_server.py

Open a new PowerShell window to run the following test commands

### Test GET all blogs (should return an empty list initially)
Invoke-RestMethod -Uri http://127.0.0.1:5000/blogs -Method Get -Headers @{Authorization="Basic $( [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes('admin:secret')) )"}

### Test POST create a new blog
Invoke-RestMethod -Uri http://127.0.0.1:5000/blogs -Method Post -Headers @{Authorization="Basic $( [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes('admin:secret')) )"} -Body (@{title="First Blog"; content="This is the first blog post."} | ConvertTo-Json) -ContentType "application/json"

### Test GET specific blog by ID
Invoke-RestMethod -Uri http://127.0.0.1:5000/blogs/1 -Method Get -Headers @{Authorization="Basic $( [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes('admin:secret')) )"}

### Test PUT update a blog
Invoke-RestMethod -Uri http://127.0.0.1:5000/blogs/1 -Method Put -Headers @{Authorization="Basic $( [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes('admin:secret')) )"} -Body (@{title="Updated Blog"; content="This is the updated blog post."} | ConvertTo-Json) -ContentType "application/json"

### Test DELETE a blog
Invoke-RestMethod -Uri http://127.0.0.1:5000/blogs/1 -Method Delete -Headers @{Authorization="Basic $( [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes('admin:secret')) )"}