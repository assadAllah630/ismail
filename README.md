# Ismail Furniture Media Manager

A web application to manage furniture products and associated media, with admin authentication and Google Drive integration.

## Features
- Admin login (single user, no registration)
- Manage products, categories, tags, photos, and media
- Upload product photos and media files to Google Drive (public links)
- Search and filter products and media
- Responsive Bootstrap UI

## Tech Stack
- Python (Flask, SQLAlchemy)
- MySQL
- Google Drive API (Service Account)
- Bootstrap (HTML/Jinja2)

## Setup Instructions

### 1. MySQL Database
- Install MySQL and start the server (default: `localhost:3306`, user: `root`, no password)
- Create the database:
  ```sql
  CREATE DATABASE ismail_furniture;
  ```
- Run the schema:
  ```sql
  USE ismail_furniture;
  SOURCE schema.sql;
  ```

### 2. Google Drive API Setup
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project (or use an existing one)
- Enable the Google Drive API
- Create a Service Account and download the JSON credentials file
- Share your target Google Drive folder with the service account email (found in the JSON file)
- Note the folder ID (from the Drive URL)

### 3. Environment Variables
- Copy `.env.example` to `.env` and fill in the values:
  - `SECRET_KEY`: Flask secret key
  - `ADMIN_USERNAME`: Admin login username
  - `ADMIN_PASSWORD_HASH`: Hashed password (use werkzeug or Flask shell to generate)
  - `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`: MySQL settings
  - `GOOGLE_SERVICE_ACCOUNT_JSON`: Path to your service account JSON file
  - `GOOGLE_DRIVE_FOLDER_ID`: ID of your shared Google Drive folder

### 4. Install Dependencies
```
pip install -r requirements.txt
```

### 5. Run Locally
```
flask run
```

### 6. Deploy on Render.com
- Push your code to a GitHub repo
- Create a new Web Service on Render
- Set environment variables in the Render dashboard (as in `.env`)
- Add a MySQL database (or connect to your own)
- Deploy!

## Password Hashing
To generate a password hash for the admin password:
```python
from werkzeug.security import generate_password_hash
print(generate_password_hash('yourpassword'))
```
Copy the output to `ADMIN_PASSWORD_HASH` in your `.env`.

## Notes
- All uploads go to Google Drive and are set to public (anyone with the link can view)
- Only the admin can add/edit products and media
- For any issues, check your environment variables and Google Drive permissions 