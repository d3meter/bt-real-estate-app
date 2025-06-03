# Real Estate App (In progress)

> **Status:** This project is currently a **work in progress**.

## Overview

This is a **practice project built with Python and Django**, where I take an existing static HTML real estate website template and transform it into a fully dynamic, database-driven web application using Django.

The goal is to deepen my understanding of Django by integrating it step-by-step into a real-world layout, turning static content into dynamic elements backed by a PostgreSQL database.

## Features

- 🛠️ Based on a pre-designed **static HTML template** turned into a Django project.
- 🐍 Built with **Django** (Python web framework).
- 🗄️ Uses **PostgreSQL** as the database backend.
- ⚙️ Includes a **custom-styled Django Admin** that visually aligns with the main site's theme.
- 🧱 Work in progress: additional features, models, and admin enhancements are continuously being added.

## Technologies Used

- Python 3
- Django
- PostgreSQL
- HTML/CSS (from the original template)
- Custom admin styling

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/d3meter/bt-real-estate-app.git
   cd bt-real-estate-app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Make sure **PostgreSQL** is installed and running locally.
   - Create a new database for the project.
   - In the project root directory, create a `.env` file with the following variables:
      ```env
      DB_HOST=your_database_host
      DB_NAME=your_database_name
      DB_USER=your_database_user
      DB_PASS=your_database_password
      DB_HOST=your_database_host
      DB_PORT=your_database_port
      ```

6. Run migrations:
   ```bash
   python manage.py migrate
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the site at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Admin Interface

The Django admin panel is accessible at `/admin/` and has been visually customized to match the aesthetic of the public site.
