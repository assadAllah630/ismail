import os
# NOTE: If you see an import error for 'dotenv', make sure to install 'python-dotenv' (see requirements.txt)
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_secret')
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD_HASH = os.getenv('ADMIN_PASSWORD_HASH', '$2b$12$R0eWuvEMN/0tAe6OTxOP4Ows6UqWddIpUcvTCH9XJmULv6YbXL7P2')
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER', 'root')}:{os.getenv('DB_PASSWORD', '')}"
        f"@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '3306')}/{os.getenv('DB_NAME', 'ismail_furniture')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_SERVICE_ACCOUNT_JSON = os.getenv('GOOGLE_SERVICE_ACCOUNT_JSON', 'service_account.json')
    GOOGLE_DRIVE_FOLDER_ID = os.getenv('GOOGLE_DRIVE_FOLDER_ID', '') 
