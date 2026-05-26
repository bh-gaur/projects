from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
import uvicorn
import requests

app = FastAPI()

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello"}

# Simple GET endpoint
@app.get("/get")
async def get_request():
    return {"message": "Hello, from /get"}

# Get client IP
@app.get("/client-ip")
async def get_client_ip(request: Request):
    client_host = request.client.host
    return {"client_ip": client_host}

# Get Server IP (public IP)
@app.get("/server-ip")
async def get_server_ip():
    public_ip = requests.get("https://ipinfo.io/ip").text.strip()
    return {"server_ip": public_ip}

# Handle 404 errors → redirect to GitHub
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return RedirectResponse(url="https://github.com/bh-gaur")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)








# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# # Product model
# class Product(BaseModel):
#     id: int
#     name: str
#     price: float

# # Example product list
# products = [
#     {"id": 1, "name": "Turmeric", "price": 199},
#     {"id": 2, "name": "Chili Powder", "price": 249},
# ]

# # Home route
# @app.get("/")
# def home():
#     return {"message": "Welcome to my API!"}

# # Example GET endpoint
# @app.get("/hello/{name}")
# def hello(name: str):
#     return {"message": f"Hello, {name}!"}

# # POST endpoint with request body
# class AddRequest(BaseModel):
#     a: int
#     b: int

# @app.post("/add")
# def add_numbers(data: AddRequest):
#     return {"sum": data.a + data.b}

# # Get list of products
# @app.get("/products", response_model=List[Product])
# def get_products():
#     return products









# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Home route
# @app.route("/")
# def home():
#     return {"message": "Welcome to my API!"}

# # Example GET endpoint
# @app.route("/hello/<name>", methods=["GET"])
# def hello(name):
#     return {"message": f"Hello, {name}!"}

# # Example POST endpoint
# @app.route("/add", methods=["POST"])
# def add_numbers():
#     data = request.get_json()
#     a = data.get("a")
#     b = data.get("b")
#     return {"sum": a + b}

# # Example for retrieving list of products
# products = [
#     {"id": 1, "name": "Turmeric", "price": 199},
#     {"id": 2, "name": "Chili Powder", "price": 249},
# ]

# @app.route("/products", methods=["GET"])
# def get_products():
#     return jsonify(products)

# if __name__ == "__main__":
#     app.run(debug=True)
