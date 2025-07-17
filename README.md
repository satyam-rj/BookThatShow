# Movie Management System with Django and MongoDB - Verditales

This project provides a web-based system for managing movies, including functionalities for adding, archiving, and removing movies. It uses Django for the web framework and MongoDB for the database.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.7 or later
- MongoDB
- pip (Python package installer)

## Installation and Setup

### 1. Install Django

1. Create a virtual environment for the project (optional but recommended):

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install Django:

   ```bash
   pip install django
   ```

### 2. Set Up MongoDB

1. Download and install MongoDB from the [official MongoDB website](https://www.mongodb.com/try/download/community).

2. Start the MongoDB server. By default, MongoDB runs on port 27017.

   ```bash
   mongod
   ```

3. Connect to the MongoDB shell:

   ```bash
   mongo
   ```

4. Create the database and collections:

   ```javascript
   use verditales
   db.createCollection("admin")
   db.createCollection("movies")
   ```

### 3. Upload Sample Data

1. Navigate to the `MongoDBSampleData` folder.

2. Load sample data into the `verditales` database. For example, if your sample data files are in JSON format, use the following command:

   ```bash
   mongoimport --db verditales --collection admin --file admin_sample_data.json --jsonArray
   mongoimport --db verditales --collection movies --file movies_sample_data.json --jsonArray
   ```

   Adjust the file names and paths as necessary based on your actual sample data files.

### 4. Configure Django to Use MongoDB

1. Install the `djongo` package, which allows Django to work with MongoDB:

   ```bash
   pip install djongo
   ```

2. Configure your Django settings to use MongoDB. In `settings.py`, update the `DATABASES` setting as follows:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': 'verditales',
       }
   }
   ```

3. Run Django migrations to set up the initial database schema:

   ```bash
   python manage.py migrate
   ```

### 5. Start the Django Development Server

1. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

2. Access the web application in your browser at `http://127.0.0.1:8000/`.

## Project Structure

- `manage.py` - Django's command-line utility.
- `app/` - Your Django application directory (contains models, views, etc.).
- `MongoDBSampleData/` - Folder containing JSON files with sample data.
- `settings.py` - Django settings file where database configurations are set.

## Sample Data

The `MongoDBSampleData` folder contains sample data files for the `admin` and `movies` collections. Ensure these files are in JSON format and correctly formatted for MongoDB import.
