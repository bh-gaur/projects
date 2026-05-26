from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}

@app.get("/subtract")
def subtract_numbers(a: int, b: int):
    return {"result": a - b}

@app.get("/multiply")
def multiply_numbers(a: int, b: int):
    return {"result": a * b}

@app.get("/divide")
def divide_numbers(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": a / b}
