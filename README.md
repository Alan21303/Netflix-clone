```markdown
# Netflix Clone

A Netflix clone web application mimicking the interface and features of Netflix. Built using HTML, CSS, JavaScript, Django, and PostgreSQL.

## Features
- User authentication (Sign up, Login, Logout).
- Admin dashboard to manage movies.
- Display featured and all movies.
- Responsive design for desktop and mobile.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Database**: PostgreSQL

## Setup Instructions

### Clone the Repository:
```bash
git clone https://github.com/Alan21303/Netflix-clone.git
cd netflix-clone
```

### Backend Setup:

1. **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up PostgreSQL:**

   - **Create a Database:**
     ```sql
     CREATE DATABASE netflix_clone;
     ```

   - **Update `DATABASES` in `settings.py` with your database credentials.**

4. **Run Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

### Frontend Setup:

1. Ensure static files (CSS, JS, images) are linked correctly in templates.

2. **Collect Static Files:**
    ```bash
    python manage.py collectstatic
    ```

### Run the Server:
```bash
python manage.py runserver
```

Access the app at `http://127.0.0.1:8000/`.

```

