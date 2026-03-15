# Legal Bridge ⚖️

Legal Bridge is a web platform connecting **Clients** and **Lawyers** with an integrated, user-friendly Glassmorphism UI. It provides role-based access and seamless dashboards for managing cases and user profiles.

## Features ✨

*   **Role-Based Authentication**: Secure registration and login for `Client`, `Lawyer`, and `Admin` roles.
*   **Custom Dashboards**: Tailored views and functionalities for each user type.
*   **Glassmorphism Design**: A sleek, modern user interface featuring smooth transitions and beautiful styling.
*   **Responsive Layouts**: Designed to work intuitively across different screen sizes.
  ## Host Link Here
   http://siddiq2.pythonanywhere.com

To get the project running locally:

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/siddiq1-max/ligal-bridge-.git
    cd ligal-bridge-
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    venv\Scripts\activate   # On Windows
    # source venv/bin/activate # On macOS/Linux
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Start the Development Server**
    ```bash
    python manage.py runserver
    ```
    Then visit `http://127.0.0.1:8000/` in your browser.

## Deployment 🌍

This application is configured for deployment on Render. It includes:
*   `render.yaml` for Blueprint deployment (Web service + PostgreSQL database).
*   `build.sh` script to install requirements, run migrations, and collect static files automatically upon deployment.
*   WhiteNoise integration for serving static files efficiently in production. 
