#!/bin/bash
echo "BUILD START"

# Install pip and dependencies
# Using 'python3 -m ensurepip' might help if pip is missing
python3 -m ensurepip
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Ensure the output directory exists
mkdir -p staticfiles_build

# Run collectstatic
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"
