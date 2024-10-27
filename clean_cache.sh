#!/bin/bash

echo "Cleaning Python cache and temporary files..."

# Eliminar directorios __pycache__ y .pytest_cache
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type d -name ".pytest_cache" -exec rm -r {} +

# Eliminar archivos con extensión .pyc y .pyo
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete

echo "Cache cleaned!"
