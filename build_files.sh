#!/bin/bash
echo "BUILD START"

# Ensure we have pip
python3 -m ensurepip || echo "ensurepip failed"
python3 -m pip install --upgrade pip || echo "pip upgrade failed"

# Install dependencies
python3 -m pip install -r requirements.txt || pip install -r requirements.txt

# Create output directory
mkdir -p staticfiles_build

# Collect static files
# Use python3 and fall back to python3.9 if needed
python3 manage.py collectstatic --noinput --clear || python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
