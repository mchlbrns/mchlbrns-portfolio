#!/bin/bash
echo "BUILD START"

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create output directory
mkdir -p staticfiles_build

# Collect static files
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"
