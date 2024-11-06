import psycopg2
import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path("environment/.env")
load_dotenv(dotenv_path=dotenv_path)
def initializeDB():
    DB_DICT= {
        "host": os.environ.get("DB_HOST"),
        "port": os.environ.get("DB_PORT"),
        "database": os.environ.get("DB_NAME"),
        "user": os.environ.get("DB_USER"),
        "password": os.environ.get("DB_PSWD"),
    }
    # Connect to DB
    connection = psycopg2.connect(**DB_DICT)
    cursor = connection.cursor()

    # Create Tables
    cursor.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE (EmployeeID INT PRIMARY KEY, FirstName VARCHAR(30), MiddleName VARCHAR(30), LastName VARCHAR(30), DOB DATE, Picture BYTEA, RoleKey VARCHAR(10), EmpContactID INT, EmpAccountID INT)")

    cursor.execute("CREATE TABLE IF NOT EXISTS ROLE (RoleID INT PRIMARY KEY, RoleKey VARCHAR(10), RoleName VARCHAR(30))")

    cursor.execute("CREATE TABLE IF NOT EXISTS EMP_CONTACT (EmpContactID INT PRIMARY KEY, EmployeeID INT, PhoneNumber VARCHAR(50), EmailAddress VARCHAR(100), Address VARCHAR(100), ContactType VARCHAR(5))")

    cursor.execute("CREATE TABLE IF NOT EXISTS EMP_ACCOUNT (EmpAccountID INT PRIMARY KEY, EmployeeID INT, UserName VARCHAR(30), Password VARCHAR(255), AccountType VARCHAR(5), Status BOOLEAN)")

    connection.commit()

    cursor.close()
    connection.close()
