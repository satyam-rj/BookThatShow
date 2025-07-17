Installation
Clone the Repository:

git clone <your_repository_url>
Install Dependencies:

cd verditales
pip install -r requirements.txt
Configure MongoDB: Create Database and Collections:

Open your MongoDB shell.
Create a new database (e.g., verditales_db).
Create collections within the database: admin and movies.
Set Environment Variables:

Create a .env file in the project root directory.
Add the following environment variables:
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_NAME=verditales_db
Replace your_secret_key with a unique secret key.
Run Django Development Server:

python manage.py runserver
