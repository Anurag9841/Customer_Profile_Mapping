# Entity Matching

## Getting Started 


### 1. Setting up the Virtual Environment

Set up a virtual environment to manage dependencies:

```sh
python3 -m venv airflow-env  
source airflow-env/bin/activate
```

### 2. Install required dependencies within the Virtual Environment

```sh
pip install -r requirements.txt
```

### 3. Set AIRFLOW_HOME 
Before installing Airflow, you can optionally set up `AIRFLOW_HOME`. If not set, the default will be `~/airflow` (e.g., `/home/user/airflow`).

Open your  `.zshrc` file for MacOS or `.bashrc` for Linux using the vim or any other text editor:

```zsh
vim ~/.zshrc
```

Add the following lines to the file:

```zsh
export AIRFLOW_HOME=<PATH-OF-YOUR-DIRECTORY>
```

Save and exit the editor. Then, apply the changes:

```zsh
source ~/.zshrc
```

Verify the environment variable:

```zsh
echo $AIRFLOW_HOME
```

### 4. Initializing the Database

```sh
airflow db init
```

### 5. Create an Airflow User with Administrative Privileges

```sh
airflow users create --username admin --password admin --firstname admin --lastname admin --role Admin --email admin@email.com
```

Verify the created user:

```sh
airflow users list
```

### 6. Optionally make changes to airflow.cfg

Set 
```plaintext 
load_examples = False
```

in airflow.cfg after intializing the database.

### 7. Make changes to .env file according to your MySQL credentials and your project path. 

```
SQL_USERNAME = 
SQL_PASSWORD = 
SQL_HOST = 
SQL_PORT = 
ROOT_PATH = 
DATABASE_NAME = "entity_matching"
```

Create a database named "entity_matching" in MySQL Server.

### 8. Running Airflow Webserver and Scheduler

```sh
airflow webserver --port 8080 
```

```sh
airflow scheduler
```

---
