#!/bin/bash

set -e

# Check for virtual env
if [ -d ".venv" ]; then
  echo "Virtual environment already exists. Run 'source .venv/bin/activate' to activate."
  exit 1
fi

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip3 install --upgrade pip
pip3 install pipenv

# Install dependencies from Pipfile
pipenv install --dev

echo "Setup complete. Run 'source .venv/bin/activate' to activate virtual environment."
