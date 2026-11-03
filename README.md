# IVAANA DESIGNERS

### About Ivaana Designers
**Ivaana Designers** is a clothing platform offering stylish and comfortable feeding and non-feeding outfits for women. It brings collections into one place, helping customers explore designs and find clothing for everyday wear and special occasions.
The application uses React for the user interface, Python and FastAPI for backend APIs, and PostgreSQL for data storage. Alembic manages database migrations.

## Requirements
    - Python 3.10+
    - Node.js 22.12+ (or Node 20.19+)
    - PostgreSQL
    - pgAdmin or psql
    - A configured backend environment file

## 1. Database (postgresql setup)
    1. Connect to PostgreSQL by Open pgadmin or psql 
    2. The create a user by using below command
        **CREATE USER postgres WITH PASSWORD 'use_a_strong_password'**
    3. After user creation, create a Database for ivaanadesigners using below command
        **CREATE DATABASE ivaanadesigners OWNER postgres;**
    4. Add the user password to Environment variable as pet Step 6.

## 2. Backend setup
    ### Create Virtual Environment
        Open new cmd terminal from project directory
        cd backend
        python -m venv .venv

    ### Active Virtual Environment
        .venv\Scripts\Activate.ps1

    ### Install Python packages dependencies 
        pip install -r requirements.txt

    ### Run Alembic Migrations 
        alembic upgrade head

    ### API Server Run
        uvicorn app.main:app --reload
