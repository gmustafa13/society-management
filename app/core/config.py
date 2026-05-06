from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    """Configuration class for application settings."""
    
    # Database configuration
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_USER = os.getenv('DB_USER', 'user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_NAME = os.getenv('DB_NAME', 'society_db')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_secret_key')
    
    # Other configurations can be added here as needed