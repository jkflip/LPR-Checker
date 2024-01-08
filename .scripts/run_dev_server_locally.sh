#!/bin/bash

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "Running development Django server locally..."

## --------------------------------------
## Edit project name here
project_name=lpr_checker_project

## Edit app name here
app_name=easy_ocr_app
app_name=lpr_checker_app

## Edit workdir here
manage_py_dir=$SCRIPT_DIR/../$project_name
## --------------------------------------

cat << EOF
========================================
Directory Settings:
    Project Name: $project_name
    App Name: $app_name
    Workdir: $manage_py_dir
========================================
EOF

echo "[1] --- Activating virtual environment..."
source $SCRIPT_DIR/../.venv/bin/activate

# echo "Starting django app..."
# python3 manage.py startapp $app_name

# echo "[2] --- Migrating database..."
# python3 "${manage_py_dir}/manage.py" makemigrations $app_name
# python3 "${manage_py_dir}/manage.py" migrate

echo "[3] --- Running development server..."
python3 "${manage_py_dir}/manage.py" runserver

echo "Done!"
