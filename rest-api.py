#! /bin/env /usr/bin/python3
"""Example of a REST API server using Flask."""
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data: list of products with ID, name, and price
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99},
    {"id": 3, "name": "Tablet", "price": 299.99},
    {"id": 4, "name": "Headphones", "price": 199.99},
    {"id": 5, "name": "Smartwatch", "price": 149.99}
]

# Endpoint to get the list of all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Endpoint to get a specific product by ID
@app.route('/products/<int:id>', methods=['GET'])
def get_item(id):
    item = next((item for item in products if item["id"] == id), None)
    return jsonify(item) if item else ('', 404)

# Endpoint to create a new product
@app.route('/products', methods=['POST'])
def create_item():
    """Create a new product, accepting just the name and price.
    generate a new ID by finding the maximum existing ID and adding 1,
    or setting it to 1 if the list is empty."""
    new_item = request.json
    # Generate a new ID by adding one to the maximum ID in the list
    # This is more robust than assuming the new ID will be the length of the list + 1
    new_id = max(product['id'] for product in products) + 1 if products else 1
    new_product = {
        "id": new_id,
        "name": new_item["name"],
        "price": new_item["price"]
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Endpoint to update an existing product by ID
@app.route('/products/<int:id>', methods=['PUT'])
def update_item(id):
    item = next((item for item in products if item["id"] == id), None)
    if item:
        item.update(request.json)
        return jsonify(item)
    return ('', 404)

# Endpoint to delete a product by ID
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_item(id):
    global products
    products = [item for item in products if item["id"] != id]
    return ('', 204)

# Endpoint to partially update a product by ID
@app.route('/products/<int:id>', methods=['PATCH'])
def patch_item(id):
    item = next((item for item in products if item["id"] == id), None)
    if item:
        item.update(request.json)
        return jsonify(item)
    return ('', 404)

if __name__ == '__main__':
    app.run(debug=True)