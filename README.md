# Library Project

Welcome to the Library Project! This is a web application built using Django and Django REST Framework. The application allows users to manage a collection of books.

## Features

- View books
- Search for books by title, author, or description
- API endpoints to access book data

## Technologies Used

- Django: A high-level Python web framework
- Django REST Framework: A powerful toolkit for building Web APIs

## Installation

To get started with the Library Project, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/library-project.git
    cd library-project
    ```

2. **Create and activate a virtual environment:**
    ```sh
    pipenv shell
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run database migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Start the development server:**
    ```sh
    python manage.py runserver
    ```

## Usage

1. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000`.

2. **API Endpoints:**
   - List all books: `GET /api/v1/books/`
   - Retrieve a book by ID: `GET /api/v1/books/<id>/`
   - Retrieve a book by slug: `GET /api/v1/books/<slug>/`

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin`. Use your superuser credentials to log in and manage the data.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- All the open-source libraries and tools used in this project.

---
