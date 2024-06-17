# Customer Profile Creation and Mapping

## About the Project

This project involves creating and mapping customer profiles using Apache Airflow and PySpark.

### Customer Profile Creation

The project fetches `Rw_transaction_data` and `Product_Category_map` from the database and joins these datasets to create an aggregation table. This table is updated incrementally as new data arrives, ensuring that the customer profiles are always up to date.

### Customer Mapping

Using the same `Rw_transaction_data` and `Product_Category_map` datasets, the project creates a map of customer product usage on a monthly basis. For instance, if a customer bought a product in month 1, month 2, month 3, and month 5 but not in month 4, the mapping would be `11101`. This mapping is updated manually as new data is received.

## Getting Started with Airflow with PySpark

## Contents

- [1. Installing Java](#1-installing-java)
- [2. Setting up the Virtual Environment](#2-setting-up-the-virtual-environment)
- [3. Making Connection to MySQL Running in Windows from WSL](#3-making-connection-to-mysql-running-in-windows-from-wsl)
    - [3.1 MySQL Client in WSL](#31-mysql-client-in-wsl)
    - [3.2 Find IPv4 Address of WSL](#32-find-ipv4-address-of-wsl)
    - [3.3 Making New User in MySQL to Make a Call from WSL](#33-making-new-user-in-mysql-to-make-a-call-from-wsl)
    - [3.4 Install PyMySQL](#34-install-pymysql)
    - [3.5 Initializing Database](#35-initializing-database)
- [4. Install Apache Airflow within the Virtual Environment](#4-install-apache-airflow-within-the-virtual-environment)
- [5. Initializing the Database](#5-initializing-the-database)
- [6. Create an Airflow User with Administrative Privileges](#6-create-an-airflow-user-with-administrative-privileges)
- [7. Running Airflow Webserver and Scheduler](#7-running-airflow-webserver-and-scheduler)

### 1. Installing Java

Install Java to run Apache Airflow with PySpark:

```sh
sudo apt-get install openjdk-11-jdk

nano ~/.bashrc
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
source ~/.bashrc
```

### 2. Setting up the Virtual Environment

Set up a virtual environment to manage dependencies:

```sh
pip install virtualenv
virtualenv airflow-env  # Replace 'airflow-env' with your preferred name for the virtual environment
source airflow-env/bin/activate
```

### 3. Making Connection to MySQL Running in Windows from WSL

#### 3.1 MySQL Client in WSL

```sh
sudo apt install mysql-client-core-8.0
```

#### 3.2 Find IPv4 Address of WSL

Go to Settings -> Network and Internet -> Status -> View Hardware and connection properties. Look for the name `vEthernet (WSL)`. It will usually be at the bottom.

#### 3.3 Making New User in MySQL to Make a Call from WSL

```sql
CREATE USER 'wsl_root'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'wsl_root'@'localhost' WITH GRANT OPTION;
CREATE USER 'wsl_root'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'wsl_root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

#### 3.4 Install PyMySQL

```sh
pip install PyMySQL==1.1.1
```

#### 3.5 Initializing Database

Edit the Airflow configuration file to connect to the MySQL database. Change the value of `sql_alchemy_conn` in `airflow.cfg`:

```cfg
sql_alchemy_conn = mysql+pymysql://wsl_root:password@my_ip/extenso_config
```

Replace `my_ip` with your WSL IP address.

### 4. Install Apache Airflow within the Virtual Environment

```sh
pip install apache-airflow
```

### 5. Initializing the Database

```sh
airflow db init
```

### 6. Create an Airflow User with Administrative Privileges

```sh
airflow users create --username admin --password admin --firstname admin --lastname admin --role Admin --email admin@email.com
```

Verify the created user:

```sh
airflow users list
```

### 7. Running Airflow Webserver and Scheduler

```sh
airflow webserver --port 8080 & airflow scheduler
```

---
