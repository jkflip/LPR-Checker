#!/bin/bash

set -e

# Check for virtual env
if [ -d ".venv" ]; then
  echo "Virtual environment already exists."
else
  # Create virtual environment
  python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip3 install --upgrade pip
pip3 install pipenv

# Install dependencies from Pipfile
pipenv install --dev

echo "Setup complete. Run 'source .venv/bin/activate' to activate virtual environment."
