# Week 2 — Distributed Tracing
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/week2.png)

### Required Homework

- [Live-Stream Video](https://www.youtube.com/watch?v=2GD9xCzRId4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=30).
- Instrument Honeycomb with OTEL
- Instrument AWS X-Ray 
- Instrument AWS X-Ray Subsegments
- Configure custom logger to send to CloudWatch Logs	
- Integrate Rollbar and capture and error
- Spending Considerations
- Observability Security Considerations


### HoneyComb
Honeycomb is an "observability" tool, which means it helps developers gain insights into how their applications are performing and behaving in real-time. Honeycomb collects and analyzes data about various aspects of an application, such as user requests, database queries, server performance, and more. It then presents this data in a user-friendly way, allowing developers to visualize and understand what's happening within their application. We used it along with OTEL (Open Telemetry) to monitor our Flask backend application.

#### Instrument Honeycomb with OTEL
**Setting up the Environment**
From Honeycomb.io I created a new environment called 'bootcamp'.
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/Distributed%20Tracing%201b.png)  

**Connecting to Honeycomb.io**

I got an API key from Honeycomb.io, and saved this key as an environment variable in my Gitpod.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/Distributed%20Tracing%201c.png)  ![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/Distributed%20Tracing%201d.png)
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/Distributed%20Tracing%201e.png)

**Configuring OTEL**

I made some additions in the `docker-compose.yml` file, to include OTEL settings.This allowed me to send data to Honeycomb.io.
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/Distributed%20Tracing%201f.png)

**Backend Instrumentation**

I set up Honeycomb and OTEL for the backend part of our application making it possible to monitor and analyze what's happening on the server side of our app.

**Getting everything up and running**

To get everything working, I followed the quick start guide provided by Honeycomb.io documentation. This involved adding some code to the requirements.txt and App.py files of our project.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/Distributed%20Tracing%201h.png) 
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/Distributed%20Tracing%201j.png)

### X-Ray
#### Instrument AWS X-Ray and X-Ray Subsegments
**Adding X-ray Library and Code**

I added the AWS X-ray SDK library to the backend application's requirements.
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/X-Ray%201a.png) 

**Create a Sampling Rule**

A sampling rule helps one determine which requests should be captured and traced for analysis in X-ray. I manged to set my own sampling rule for the application.
  
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/X-Ray%201f.png)
   
**Setup X-ray Daemon and Logged Traces**

I managed to setup X-ray deamon by adding its configuration to my `docker-compose.yml` file. I ran the container and was able to get data (traces) from X-Ray.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/X-Ray%201g.png)
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/X-Ray%201n.png)

**Adding Subsegment**

The results from X-ray could be further enhanced and I did that by adding subsegments.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/Subseg%202.png)

### CloudWatch 

***Configure custom handler to send CloudWatch Logs***

I configured Watchtower by configuring it into our application. Once the configuration was completed I have able to send cloudwatch logs and get results from the CloudWatch consolein my AWs account.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/CW%20logs%202.png)
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/CW%20logs%204a%20implemented.png)

### Rollbar

***Integrate Rollbar and capture and error***

Inorder to use rollbar in our application, I had to first set it up in my Gitpod by adding it to my `requirements.txt` file. I then set the env vars for Rollbar in my Gitpod enviroment.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/Rollbar%201%20add%20files%20to%20rqmts%20txt.png)
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/Rollbar%203%20set%20env%20var%20and%20conf%20.png)

I also intergrated it with my application by adding some code to my `app.py` file.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/Rollbar%208%20placed%20code%20on%20a%20diff%20place%20to%20define%20app%20error%20in%20logs.png)


I was able to run a test to see if Rollbar was listening to my backend and got a response.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-2%20images/Rollbar%2011%20backend%20working.png)


