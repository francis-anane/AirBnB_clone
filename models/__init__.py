#!/usr/bin/python3

from models.engine.file_storage import FileStorage

storage = FileStorage()  # Unique instance for FileStorage

# Load data from JSON file
storage.reload()
