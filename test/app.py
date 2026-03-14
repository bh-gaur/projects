#!/usr/bin/env python3

import os
# import json
from flask import Flask, jsonify, request
import datetime
app = Flask(__name__)
@app.route('/')
def home():
    """Simple health check endpoint"""
    return jsonify({
        "message": "Hello from Python Test App!",
        "status": "healthy",
        "version": "1.0.0"
    })
@app.route('/health')
def health():
    """Health check endpoint for Kubernetes"""
    return jsonify({
        "status": "healthy",
        "service": "python-test-app"
    }), 200
@app.route('/api/info')
def info():
    """App information endpoint"""
    return jsonify({
        "app_name": "Python Test Application",
        "version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "port": int(os.getenv("PORT", 5000))
    })
@app.route('/api/echo', methods=['POST'])
def echo():
    """Echo endpoint for testing"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    return jsonify({
        "echo": data,
        "timestamp": str(datetime.datetime.now())
    })
if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("DEBUG", "False").lower() == "true"
    print(f"Starting Python Test App on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
