#!/bin/bash

#Shell file to run all python JSON extraction scripts at the same time

echo "Running all .py scripts, extracting JSON files to CSV..."
python3 Denver_Health.py
python3 Poudre_Valley.py
python3 University_of_Colorado.py
python3 Uh_Cleveland_Medical_Center.py
echo "Done"
