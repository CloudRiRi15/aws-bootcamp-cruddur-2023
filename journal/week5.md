# Week 5 — DynamoDB and Serverless Caching

## Required Homework
### Data Modelling
Our application is based on a simple table design, which presents some challenges in data modeling. To ensure the effectiveness and cost-efficiency of our database, it's crucial to map our data properly. By choosing a design that allows easy access to the required data without relying on Global Secondary Indexes (GSIs), we can optimize our application's performance and cost.

***Challenges and Considerations:***

- In DynamoDB, we don't have the luxury of joins, so it's essential to plan for a flat table structure.
- DynamoDB offers the option to use SQL, specifically PartiQL, for querying data.
- To improve scalability and accessibility, we have decided to structure all data in a single table, rather than using related tables.

***Some Key Points to Remember:***

- When designing the database model, start by listing the different access patterns required for the application. This step is critical to ensure efficient data retrieval.
- Minimize the use of Global Secondary Indexes (GSIs) to control costs and enhance performance.
- Utilize DynamoDB Streams to enable real-time updates and changes to message groups.
- Take advantage of DynamoDB's support for SQL with PartiQL for querying data.
- Opt for a flat table structure to accommodate the lack of joins in DynamoDB and to improve scalability.

#### Implement Schema Load Script 
I Added `boto3` to `requirements.txt`  and ran a pip-install to install all dependencies.
I then proceeded to create a new folder `ddb` in my backend-flask.
Once I had created the folder I added a new file `schema-load` and made it executable.
The file had the following code:
```
#! /usr/bin/env python3

import boto3
import sys

attrs = {"endpoint_url": "http://localhost:8000"}

if len(sys.argv) == 2:
    if "prod" in sys.argv[1]:
        attrs = {}

ddb = boto3.client("dynamodb", **attrs)
table_name = "cruddur-messages"

response = ddb.create_table(
    TableName=table_name,
    AttributeDefinitions=[
        {"AttributeName": "pk", "AttributeType": "S"},
        {"AttributeName": "sk", "AttributeType": "S"},
    ],
    KeySchema=[
        {"AttributeName": "pk", "KeyType": "HASH"},
        {"AttributeName": "sk", "KeyType": "RANGE"},
    ],
    # GlobalSecondaryIndexes=[
    # ],
    BillingMode="PROVISIONED",
    ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
)

print(response)
```
Use the following command to run this script `./bin/ddb/schema-load`. You should have the output below:

![]()bbb3 pic

I also created more bash scripts for diferent things.

### Implement Seed Script

Created a new file that's executable for our seed data.
Run the script using this command `./bin/ddb/seed`

image 9 and 12



Using the same concept as when we implemented the schema-load file, I implemented the seed script.
My seed script contained the code below:
```
#! /usr/bin/env python3

import boto3
import sys

attrs = {"endpoint_url": "http://localhost:8000"}

ddb = boto3.resource("dynamodb", **attrs)

table_name = "cruddur-messages"

table = ddb.Table(table_name)
response = table.scan()

print("RESPONSE >>>>>>>>", response)

items = response["Items"]

for item in items:
    print(item)
```


### Implement Scan Script

### Implement Pattern Scripts for Read and List Conversations


### Implement Update Cognito ID Script for Postgres Database




ddb 14





