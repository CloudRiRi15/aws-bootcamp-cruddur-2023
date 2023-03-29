![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/aws-week-0-1.jpg)

# TABLE OF CONTENTS

 + [Introduction](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#introduction)
 + [Project Scenario](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#project-scenario-woman_technologist)
 + [Technologies and Pre-Requisites](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#technologies-and-pre-requisites)
 + [Set-up Instructions](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#set-up-instructions)
 + [The Challenges and Set-Backs](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#the-challenges-and-set-backs)
 + [Week 0 Homework Required Tasks]
   - [Watch Week 0 - Live Streamed Video] 
   - [Watch Chirag's Week 0 - Spend Considerations]
   - [Watch Ashish's Week 0 - Security Considerations]
   - [Recreate Conceptual Diagram in Lucid Charts or on a Napkin](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#conceptual-architectural-diagram-napkin-diagram)
   - [Recreate Logical Architectual Diagram in Lucid Charts]
   - [Create an Admin User]
   - [Use CloudShell]
   - [Generate AWS Credentials](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#generating-aws-credentials)
   - [Installed AWS CLI]
   - [Create a Billing Alarm]
   - [Create a Budget](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#set-an-aws-budget)
+ [Week 0 Homework Challenges](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#homework-challenges)
  - Destroy your root account credentials, Set MFA, IAM role
  - [Review all the questions of each pillars in the Well Architected Tool (No specialized lens)]
  - [Use EventBridge to hookup Health Dashboard to SNS and send notification when there is a service health issue]
  - [Create an architectural diagram (to the best of your ability) the CI/CD logical pipeline in Lucid Charts]
  - [Research the technical and service limits of specific services and how they could impact the technical path for technical flexibility]
  - [Open a support ticket and request a service limit]



# Introduction

I got enrolled in the 15-week Free AWS Project BootCamp with AWS Community Hero Andrew Brown. The purpose of this BootCamp is to bridge the gap between Certification and actual real world work experience for students who have acquired an associate level certification. I am excited to be part of this great opportunity and plan to be part of each and every part of the process and learn as much as I can and stretch myself to gain actual real work exprience. *A detailed document about the Cloud Project BootCamp can be found [here](https://docs.google.com/document/d/19XMyd5zCk7S9QT2q1_Cg-wvbnBwOge7EgzgvtVCgcz0/edit#)* 

![FREE AWS CLOUD PROJECT BOOTCAMP GOAL](assets/BootCamp%20Goal.png)

![FREE AWS CLOUD PRJECT-LEVEL](assets/Project%20Level-250.png)

## Project Scenario :woman_technologist:

A startup company has decided to build their own micro-blogging platform and has hired you to be its first cloud engineer.The company paid a web-development firm to translate their wireframe designs into a mock web-application for the purpose of demoing to raise capital. After a successful round of funding, you [the cloud engineer] have been tasked with taking the mock web-application and making it production ready at scale.

The startup company consulted a fractional CTO to help choose some of the technical requirements to place the company on a good technical roadmap:

+ The frontend application should be written in Javascript using React (functional components).
+ The backend application should be written in Python using Flask
  - Since we plan to be API only
  - Since we want to choose a popular framework API only framework
  - Since we want a micro-framework because we are offloading as much to the cloud as possible to avoid be a monolithic application
  - Since we don’t want an ORM because the CTO considers it an anti-pattern
  - Since Python is the most popular language being learned for cloud right now
+ That an API specification be defined detailing the exact endpoints required.
+ The web application:
  -  Shall be deployed to AWS.
  -  Takes advantage of modern-applications cloud services.

The startup company has spent the majority of their funding on hiring you for the next 6 months (but mostly spent the money on marketing and buying a really cool domain) and so you also need to ensure you keep the cloud provider costs as low as possible.

## Technologies and Pre-Requisites



## Set-up Instructions




# The Challenges and Set-Backs

## Challenge No. 1

### Personal Challenges: *I Can't attend BootCamp from Day 1* :sob::sob:
 
Right off the bet, I am faced with some personal challenges which will require my full attention over the next 3-weeks or so, this is going to affect my full participation during this period and it has proven to be very discouraging. I am consoled and encouraged at the fact that after speaking to the BootCamp Organizer, Andrew Brown, he was very understanding and is willing to give me considerations with homework submissions. I am however to ensure that I document that in the student portal under the considerations.

## Challenge No. 2

### GitHub *What is this and how do I use it* :thinking:

 Yes I said GitHub. To be precise writing a markdown files and basic technical writing skills. I am finding that I am struggling with what to include or not include in my journal. How detailed should the information be, just how much to put and what to leave out. After careful study *over a week long* I think I have sort of figured it out. Here is a list of some of the resources I used to help me with GitHub and Technical Documentation, can be found here **to insert a link of all the resources used**.I thought to myself since the goal of this BootCamp is to help an associate level certification holder to build a cloud project with enough complexity to merit worthiness on their resume and combine multiple cloud services to emulate a real-world production workload, I am going to make sure that I document my project journey with as much details as possible while making it as easy to read and understand as possible, using simple language to explain complex technical processess.

  ## Challenge No. 3
  
  ### Playing Catch-Up :running_woman::running_woman:
  
I finally managed to start on some of the content for week-0 and I have been playing catch-up ever since. The 1st thing that I did wrong is I rushed through the homeworks without documenting or taking screenshots as proof of work done and realised that my work can not be verified. I had to go back to my account and destroy everything I had done and start again this time making sure to take screen shots as explained in Andrew Brown's YouTube video [Updating your journal in Github](https://www.youtube.com/watch?v=mWaSBRJhUFM&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=19)

# Week 0 — Billing and Architecture

## Required Homework/Tasks

### Conceptual Architectural Diagram (Napkin Diagram)

We were tasked with drawing a conceptual diagram of the Cruddur App we are building. The purpose of this is to sort of put things into perspective, this is like a foundation being laid.

**to insert napkin image as proof of work done**

### Generating AWS Credentials

**Install AWS CLI via Gitpod**


### Set an AWS Budget
From the root account, grant the IAM user billing access and permissions. **NB** if you do not grant the IAM user billing access, the IAM user will not be able to access the billing console. 

**to insert budget image as proof of work done**

Once you grant your IAM user access to billing permissions, log in to your IAM console to set a budget. I created 2 budgets for this BootCamp, since the goal was to make use of the free-tier account I first created a Zero Spend Budget. This was very simple and starightforward to do. 
From the AWS billing Console >Select Budgets > Create Budget > Choose Budget Type
Budget Setup and Templates (*new*) will show as per image below.
Under Template, I selected the Zero Spend Budget and **Click Create Budget**

**insert Zero spend Budget as proof of work done**

**to insert budget image as proof of work done**

### Set a Billing Alarm

For the task of creating a billing I chose to use the AWS CLI.Inorder for you to create a billing alarm you will need to firstly  I followed the following steps to achieve this

Step 1

Create an SNS Topic



**to insert billing image as proof of work done**

### Using CloudShell

## HomeWork Challenges

### Create an Architectural Diagram CI/CD Pipeline (to the best of your ability) in Lucid Charts
**to insert lucid chart architectural image as proof of work done**

### Use EventBridge to hook up Health Dashboard to SNS and send notification when there is a service health issue

### Review each question in each pillar of the Well-Architected Tool (No specialised lens)



*This File will get updated as I go through this BootCamp to make it is detailed as possible and hopefully it helps someone else*
*Going to work on the well-Architected Tool right now and hopefully I get time to do the health DashBoard too*



