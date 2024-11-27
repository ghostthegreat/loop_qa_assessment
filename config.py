import os
import sys
from dotenv import load_dotenv
from pathlib import Path

current_dir = Path(__file__).resolve().parent

load_dotenv(dotenv_path=current_dir / '.env')


username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
baseURL = os.getenv('baseURL')

config = {
    'use': {
        'baseURL': baseURL,
    },
    'credentials':{
        'username': username,
        'password': password,
    }
}
