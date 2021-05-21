<!-- FLASK TEMPLATE -->

## Flask Template

Simple Flask web app template with user authentication.

### Prerequisites

- Python 3.6+
- PostgreSQL database

### Virtual Environment

Create a virtual environment by calling:
```sh
python3 -m venv <your_venv_name>
```

Then, activate your virtual environment to install the dependencies.

On Windows, run:
```sh
<your_venv_name>\Scripts\activate
```
On Linux/MacOS, run:
```sh
<your_venv_name>/bin/activate
```

### Dependencies

To install all required dependencies in your virtual environment, run the command:
```sh
pip install -r requirements.txt
```
To install the dependencies manually, the following libraries are used in the project:
```sh
pip install flask
pip install flask-login
pip install flask-migrate
pip install flask-sqlalchemy
pip install psycopg2-binary
```

### Environment Variables

```sh
FLASK_SECRET_KEY
POSTGRES_URI
```

### Start The Application
To start the application, simply run the command:
```sh
python main.py
```
