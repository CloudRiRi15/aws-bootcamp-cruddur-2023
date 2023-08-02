# Week 4 — Postgres and RDS
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-4/week4.png)

## Required Homework

- Create RDS Postgres Instance	
- Create Schema for Postgres	
- Bash scripting for common database actions 
- Install Postgres driver in backend application
- Create AWS Cognito trigger to insert user into database
- Create new activities with a database insert
- Security Considerations



### Create RDS Postgres Instance	
We will create our Postgres DB instance from the CLI as it is much easier. First we reviewed the parameters when creating a Db via the AWS Console but did not create it. 
I then went to the CLI and ran the command below to create the Postgres DB instance 

```
aws rds create-db-instance \
  --db-instance-identifier cruddur-db-instance \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --engine-version  14.6 \
  --master-username cruddurroot \
  --master-user-password <password>\
  --allocated-storage 20 \
  --availability-zone us-east-1a \
  --backup-retention-period 0 \
  --port 5432 \
  --no-multi-az \
  --db-name cruddur \
  --storage-type gp2 \
  --publicly-accessible \
  --storage-encrypted \
  --enable-performance-insights \
  --performance-insights-retention-period 7 \
  --no-deletion-protection
```
Ensure you set a strong master password for your RDS instance.
 I was a ble to create my databse and confirmed it was created via the Console. Ensure that you stop the Instance temporarily since we wontbe using it now. RDS will stop the instance for & days.Set an alarm and remember to stop it again so it doesnt run in the background.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-4/postgres%20db%202.png) 
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-4/postgres%20db%203.png) pics 2,3

We then connected to our Postgres container we build in week 1 Containerization class. To do this we ran the code below
```psql -Upostgres --host localhost``

Once I was connected. I took time to try out some of the common PSQL commands like the ones below:
```
\x on -- expanded display when looking at data
\q -- Quit PSQL
\l -- List all databases
\c database_name -- Connect to a specific database
\dt -- List all tables in the current database
\d table_name -- Describe a specific table
\du -- List all users and their roles
\dn -- List all schemas in the current database
CREATE DATABASE database_name; -- Create a new database
DROP DATABASE database_name; -- Delete a database
CREATE TABLE table_name (column1 datatype1, column2 datatype2, ...); -- Create a new table
DROP TABLE table_name; -- Delete a table
SELECT column1, column2, ... FROM table_name WHERE condition; -- Select data from a table
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...); -- Insert data into a table
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition; -- Update data in a table
DELETE FROM table_name WHERE condition; -- Delete data from a table
```
Now that we have warmed up our fingers with some psql commands lets proceed.




### Create Schema for Postgres
***Create  Database***
By running the command `CREATE DATABASE cruddur;` I was able to creeate my databse. I then proceeded to create a schema for postgres.

From the backend Flask application, create a `db/schema.sql` file. In your `schema.sql` file add the following: 
```
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

Proceed and load the schema youjust created by running the following command:

```
psql -Upostgres cruddur < db/schemal.sql -h localhost -U postgres
```

You will be prompted for a password.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-4/postgres%20db%208.png)

Now set the connection url for your postgres by running the following commands;
```
export CONNECTION_URL="postgresql://postgres:password@localhost:5432/cruddur"
gp env CONNECTION_URL="postgresql://postgres:password@localhost:5432/cruddur"
```

Test your connection and ensure your postgres is connecting locally.
```
psql $CONNECTION_URL
```

### Bash scripting for common database actions 
 We will create a few new files that will contain xecutable bash scripts to make it easier for us to execute commands. The first 3 scripts we will create are as below.

 ```
./bin
├── db-create
├── db-drop
└── db-schema-load
```
By default when you create a file it is not executable 
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-4/postgres%20db%2013.png)

We can our new files executable by running the chmod u+x command like below:

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-4/postgres%20db%2014.png)

Wemade our bash scripts look pretty by adding colour to them
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-4/postgres%20db%2016.png)

 

### Install Postgres driver in backend application
In our `requirements.txt` file we will add the postgres driver by adding the following lines of code;
```
psycopg[binary]
psycopg[pool]
```


### Create AWS Cognito trigger to insert user into database
We set up a Lambda function to our cognito user pool to trigger a few things, like post-confirmation and signup.
Lambda Code below:
```
import json
import psycopg2
import os

def lambda_handler(event, context):
    user = event["request"]["userAttributes"]
    print("User attributes ----->", user)
    try:
        conn = psycopg2.connect(os.getenv("CONNECTION_URL"))
        cur = conn.cursor()

        parameters = [
            user["name"],
            user["email"],
            user["preferred_username"],
            user["sub"],
        ]

        sql = f"INSERT INTO public.users (display_name, email, handle, cognito_user_id) VALUES (%s, %s, %s, %s)"

        cur.execute(sql, *parameters)

        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print("Database connection closed.")

    return event
```






