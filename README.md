# MoneyBasketball #

## Description
A React + Flask webapp for visualizing NBA.com shot data, with a focus on offensive efficiency.

## Getting Started

Follow these steps to initialize up the Python backend and React front end.

### Backend

#### Prerequisites
Ensure that you have Python 3 installed on your system. You can download Python from [python.org](https://www.python.org/). The backend code is located in `backend/`.

    cd backend

#### Initialize a Virtual Environment (recommended)

    python3 -m venv venv
    source venv/bin/activate

#### Dependencies
Install the required pip packages, as specified in `requirements.txt`.

    pip3 install -r requirements.txt

#### Starting the Backend Server
Navigate to the `shot_diet` directory and run `flask run` in order to start the backend server.

    cd shot_diet
    flask run 

This command will start the Flask app in development mode. Open http://localhost:5000 to view it in the browser.

### Frontend

#### Prerequisites

Before proceeding, ensure you have the following installed on your system:

- Node.js: [Download & Install Node.js](https://nodejs.org/en/download/)
- npm (Node Package Manager): Comes with Node.js.

The frontend code is located in `frontend/`.

    cd frontend

#### Dependencies
Run `npm install` to install the necessary dependencies for the React app, as specified in `package.json`.

    npm install

#### Start the Development Server
Once the installation is complete, start the React development server:

    npm start

This command will start the React app in development mode. Open http://localhost:3000 to view it in the browser. The page will reload if you make edits, and you will also see any lint errors in the console.
