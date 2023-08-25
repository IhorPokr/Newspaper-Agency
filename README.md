# Newspaper-Agency

## Description
As the chief of a newspaper agency, you lead a talented team of Redactors responsible for producing quality content.
However, you've noticed a lack of proper tracking for the newspapers published by your agency. To address this issue, 
you have taken the initiative to create a systematic tracking system for Redactors, ensuring that you always have a 
record of which Redactors were assigned to each newspaper. This system will allow you to easily identify the publishers 
of each newspaper and enhance the efficiency and organization of your agency's operations.

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/IhorPokr/Newspaper-Agency.git
cd Newspaper-Agency
```

### Step 2: Sett Up Virtual Environment and Install Requirements
If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements
in it, but if not:
```bash
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

### Step 3: Create .env file
The .env file is used to store environment variables for your application. These variables can include sensitive
information like API keys, database credentials, and other configuration settings. To ensure security and separation 
of sensitive data from your codebase, you should never commit the .env file to version control.


#### Create a .env file at the root of the Project
```bash
...
├── .env #here
└── manage.py
```

#### Set Environment Variable in .env file
```bash
SECRET_KEY=<your_secret_key>
```

#### Add the .env file to .gitignore file


### Step 4: Start Django Server
```bash
python manage.py migrate
python manage.py runserver # starts Django Server
```

### Step 5: Login
```
username: admin_user
password: xde123qw
```
