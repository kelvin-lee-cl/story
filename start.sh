#!/bin/bash

# Print environment info for debugging
echo "Python version: $(python --version)"
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting application..."
exec gunicorn app:app --config gunicorn.conf.py
