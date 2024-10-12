from dotenv import load_dotenv
import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(PROJECT_ROOT, '..', '.env')

if os.path.exists(CONFIG_PATH):
    load_dotenv(CONFIG_PATH)