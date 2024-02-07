# MoneyBasketball #

## Description
A React + Flask webapp for visualizing NBA.com shot data, with a focus on offensive efficiency.

## Getting Started

Follow these steps to initialize up the Python backend and React frontend.

## Backend

### Prerequisites
Ensure that you have Python 3 installed on your system. You can download Python from [python.org](https://www.python.org/). The backend code is located in `backend/`.

    cd backend

### Initialize a Virtual Environment (recommended)

    python3 -m venv venv
    source venv/bin/activate

### Dependencies
Install the required pip packages, as specified in `requirements.txt`.

    pip3 install -r requirements.txt

### Initializing a Development Database (Sqlite3)
To initialize a database locally when you begin using the project, navigate to the `shot_diet` directory and run `flask db upgrade` in order to initialize your database, using the migration files found in the `backend/shot_diet/migrations/` directory.

    cd shot_diet
    flask db upgrade
    flask run

### Starting the Backend Server
Navigate to the `shot_diet` directory and run `flask run` in order to start the backend server.

    cd shot_diet
    flask run 

This command will start the Flask app in development mode. Open http://localhost:5000 to view it in the browser.

## Frontend

### Prerequisites

Before proceeding, ensure you have the following installed on your system:

- Node.js: [Download & Install Node.js](https://nodejs.org/en/download/)
- npm (Node Package Manager): Comes with Node.js.

The frontend code is located in `frontend/`.

    cd frontend

### Dependencies
Run `npm install` to install the necessary dependencies for the React app, as specified in `package.json`.

    npm install

### Start the Development Server
Once the installation is complete, start the React development server:

    npm start

This command will start the React app in development mode. Open http://localhost:3000 to view it in the browser.

## Adding Dependencies
### Frontend
To add any npm packages, run

    npm install --save-dev <package>

### Backend
To add any python packages, ensure you are running in the virtual environment, install the required packages, and then output the results of `pip freeze` to `backend/requirements.txt`.

    cd backend
    pip freeze > requirements.txt

## Makefile
You can find helpful commands for linting and autolinting in the `Makefile`. For example, to execute the lint checks, which must pass in order to merge to `main`, run:

    make lint

To lint in place (using the `eslint` and `prettier` npm packages for the frontend code, and the `black` package for the backend code), run:
    
    make autolint

Note that this will edit the files in place.

To launch a development server, run `make run` to build the latest versions of the frontend and backend containers and run them, via `docker-compose up --build`

    make run
