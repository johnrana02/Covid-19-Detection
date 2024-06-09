import os
import yaml
from pathlib import Path
from src.cnnclassifier import logger
from box import ConfigBox
from ensure import ensure_annotations
from typing import Any
import base64
import joblib

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> dict:
    """Reads a YAML file and returns the content as a Box object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        Box: Contents of the YAML file as a Box object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully")
            return Box(content)
    except Exception as e:
        logger.exception(f"Error reading YAML file {path_to_yaml}: {e}")
        raise



@ensure_annotations
def create_directories(path_to_directories: list[str], verbose: bool = True):
    """Create directories specified in the list if they don't exist.

    Args:
        path_to_directories (List[str]): List of directory paths to create.
        verbose (bool): Whether to log messages (default is True).
    """
    for path in path_to_directories:
        if not os.path.exists(path):
            os.makedirs(path)
            if verbose:
                logger.info(f"Directory created: {path}")
        elif verbose:
            logger.info(f"Directory already exists: {path}")
            
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """Save data to a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to save to the JSON file.
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logger.info(f"JSON data saved to: {path}")
    except Exception as e:
        logger.exception(f"Error saving JSON data to {path}: {e}")
        raise
    
@ensure_annotations
def load_json(path: Path) -> dict:
    """Load JSON data from a file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        dict: Loaded JSON data.
    """
    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
        logger.info(f"JSON data loaded from: {path}")
        return data
    except Exception as e:
        logger.exception(f"Error loading JSON data from {path}: {e}")
        raise

@ensure_annotations
def save_bin(path: Path, data: bytes):
    """Save binary data to a file.

    Args:
        path (Path): Path to the binary file.
        data (bytes): Binary data to save.
    """
    try:
        with open(path, 'wb') as bin_file:
            bin_file.write(data)
        logger.info(f"Binary data saved to: {path}")
    except Exception as e:
        logger.exception(f"Error saving binary data to {path}: {e}")
        raise
    
    
@ensure_annotations
def load_bin(path: Path) -> bytes:
    """Load binary data from a file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        bytes: Loaded binary data.
    """
    try:
        with open(path, 'rb') as bin_file:
            data = bin_file.read()
        logger.info(f"Binary data loaded from: {path}")
        return data
    except Exception as e:
        logger.exception(f"Error loading binary data from {path}: {e}")
        raise
    
@ensure_annotations
def get_file_size(file_path: Path) -> int:
    """Get the size of a file in bytes.

    Args:
        file_path (Path): Path to the file.

    Returns:
        int: Size of the file in bytes.
    """
    try:
        size = file_path.stat().st_size
        logger.info(f"File size of {file_path}: {size} bytes")
        return size
    except Exception as e:
        logger.exception(f"Error getting file size of {file_path}: {e}")
        raise
    
@ensure_annotations
def decodeimage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close
        
        
        
@ensure_annotations
def encodeImageintoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())








