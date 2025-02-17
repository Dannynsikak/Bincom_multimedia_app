# Multimedia Management App

A Django-based multimedia management application that allows users to upload, view, and delete media files such as images, videos, and audio files.

# Features

Upload multimedia files (images, videos, and audio)

Display uploaded media in a responsive interface

Delete media files

Secure CSRF protection for form submissions

# Technologies Used

Backend: Django (Python)

Frontend: HTML, CSS

Database: SQLite

# Installation

Prerequisites

Ensure you have the following installed on your system:

Python (3.10 or higher)

Django (latest version recommended)

# Setup Instructions

Clone the Repository

    git clone https://github.com/Dannynsikak/Bincom_multimedia_app.git

cd Bincom_multimedia-app

Create a Virtual Environment

python -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Apply Migrations

python manage.py migrate

Run the Development Server

python manage.py runserver

Access the App
Open your browser and go to: http://127.0.0.1:8000/

Project Structure

    Bincom_multimedia-app/
    │── media_app/
    │   ├── migrations/         # Database migrations
    │   ├── static/             # Static files (CSS, JavaScript)
    │   ├── templates/
    │   │   ├── media_app/
    │   │   │   ├── media_list.html  # Display media files
    │   │   │   ├── upload_media.html  # Upload form
    │   ├── models.py           # Database models
    │   ├── views.py            # Django views
    │   ├── urls.py             # URL routing
    │   ├── Uploadform.py       # Form handling
    │── db.sqlite3              # SQLite database
    │── manage.py               # Django management script
    │── requirements.txt        # Project dependencies
    │── README.md               # Project documentation

# API Endpoints

`Endpoint

Method

Description

/

GET

View all media files

/upload/

POST

Upload a media file

/delete/<id>/

POST

Delete a media file`

# Contributing

If you’d like to contribute:

Fork the repository.

Create a new branch (feature-branch).

Commit your changes.

Push to your branch and submit a Pull Request.
