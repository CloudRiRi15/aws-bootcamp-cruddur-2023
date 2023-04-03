![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/aws-week-0-1.jpg)

# TABLE OF CONTENTS

 + [Introduction](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#introduction)
 + [Project Scenario](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#project-scenario-woman_technologist)
 + [Pre-Requisites Technologies and Set-up Instructions](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#technologies-and-pre-requisites)
 + [The Challenges and Set-Backs](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#the-challenges-and-set-backs)
 + [Week 0 Homework Required Tasks](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/week0.md#required-homeworktasks)
   - [Watch Week 0 - Live Streamed Video and other required videos for Week 0]
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

[Margaret Valtierra](https://www.linkedin.com/in/margaretvaltierra/), who is an AWS Community Hero, used a beautiful concept (user personnas) to help us visualise the project scenario. I still see Tony talking to me in the conference room.😆 

## Pre-Requisites Technologies and Set-up Instructions

Before getting started with this Cloud Project BootCamp, you will need to have the following:

 +  A [Free-tier AWS](https://www.youtube.com/watch?v=uZT8dA3G-S4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=7) account with appropriate permissions to create the necessary resources.
 +  Understand the basic concepts of virtualization and [containers](https://lnkd.in/eY-Ws2zj).
 +  Basic Knowledge of these programming languages 
    - [Python 3](https://www.youtube.com/watch?v=eWRfhZUzrAc)
    - [Javascript ECMAScript 6 (ES6)](https://www.youtube.com/watch?v=PkZNo7MFNFg&t=8s)
    - YAML and JSON files
 + [Git](https://www.youtube.com/watch?v=rirBD2CZZXQ&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=2), [Gitpod](https://www.youtube.com/watch?v=yh9kz9Sh1T8&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=4), [Github Codespaces](https://www.youtube.com/watch?v=OwFVrU5B3xs) and Online [Version Control Systems]() VSC Knowledge.
 + [Honeycomb.io account](https://www.youtube.com/watch?v=7IwtVLfSD0o)
 + [Rollbar account](https://www.youtube.com/watch?v=Lpm6oAP3Fb0)
 + [Lucidcharts account](https://www.youtube.com/watch?v=bgFzBYLT3sU)
 + [Momento account](https://www.gomomento.com/)
 
 **All setup videos for the pre-requisite technologies are courtsey of [@Giftedlane](https://www.youtube.com/@GiftedLane)**

# The Challenges and Set-Backs

## Challenge No. 1

### Personal Challenges: *I Can't attend BootCamp from Day 1* :sob::sob:
 
Right off the bet, I am faced with some personal challenges which will require my full attention over the next 3-weeks or so, this is going to affect my full participation during this period and it has proven to be very discouraging. I am consoled and encouraged at the fact that after speaking to the BootCamp Organizer, Andrew Brown, he was very understanding and is willing to give me considerations with homework submissions. I am however to ensure that I document that in the student portal under the considerations.

## Challenge No. 2

### GitHub *What is this and how do I use it* :thinking:

 Yes I said GitHub. To be precise writing a markdown files and basic technical writing skills. I am finding that I am struggling with what to include or not include in my journal. How detailed should the information be, just how much to put and what to leave out. After careful study *over a week long* I think I have sort of figured it out. I thought to myself since the goal of this BootCamp is to help an associate level certification holder to build a cloud project with enough complexity to merit worthiness on their resume and combine multiple cloud services to emulate a real-world production workload, I am going to make sure that I document my project journey with as much detail as possible while making it as easy to read and understand,3 using simple language to explain complex technical processess.Here is a list of some of the resources I used to help me with GitHub and Technical Documentation.
 + [Git and Github CrashCourse](https://www.youtube.com/watch?v=RGOj5yH7evk)
 + [Github Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
 + [Technical Writing](https://developers.google.com/tech-writing)

## Challenge No. 3
  
  ### Playing Catch-Up :running_woman::running_woman:
  
I finally managed to start on some of the content for week-0 and I have been playing catch-up ever since. The 1st thing that I did wrong is I rushed through the homeworks without documenting or taking screenshots as proof of work done and realised that my work can not be verified. I had to go back to my account and destroy everything I had done and start again this time making sure to take screen shots as explained in Andrew Brown's YouTube video [Updating your journal in Github](https://www.youtube.com/watch?v=mWaSBRJhUFM&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=19)

# Week 0 — Billing and Architecture

## Required Homework/Tasks

### Watched the live stream video and all required videos for week 0 as outlined in the [student portal](https://student.cloudprojectbootcamp.com/). Videos can be found on the [BootCamp official playlist](https://www.youtube.com/watch?v=8b8SvQHc4Pk&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv)

### Conceptual Architectural Diagram (Napkin Diagram)

We were tasked with drawing a conceptual diagram of the Cruddur App we are building. The purpose of this is to sort of put things into perspective, this is like a foundation being laid. As it the time I watched this I didnt haveany access to a real actual napkin so I used my white. I plan to still do it in a napkin though for the kicks of it.

**to insert napkin image as proof of work done**

### Generating AWS Credentials

I set up my AWS Credentials and got them working. 

**Install AWS CLI via Gitpod**


### Set an AWS Budget
From the root account, grant the IAM user billing access and permissions. **NB** if you do not grant the IAM user billing access, the IAM user will not be able to access the billing console. 

**to insert budget image as proof of work done**

Once you grant your IAM user access to billing permissions, log in to your IAM console to set a budget. I created Zero Spend Budget for this BootCamp, since the goal was to make use of the free-tier account. This was very simple and starightforward to implement.

From the AWS billing Console >Select Budgets > Create Budget > Choose Budget Type
Budget Setup and Templates (*new*) will show as per image below.
Under Template, I selected the Zero Spend Budget and **Click Create Budget**

**insert Zero spend Budget as proof of work done**

**to insert budget image as proof of work done**

### Set a Billing Alarm

For the task of creating a billing alarm, I chose to use the AWS CLI. Inorder for you to create a billing alarm you follow the following steps:

Step 1: Create an SNS Topic




**to insert billing image as proof of work done**

### Using CloudShell

###Applying AWS credits to AWS Account. 

Using the step by step guide from Chirag's [Video](https://www.youtube.com/watch?v=OVw3RrlP-sI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=13) on Pricing Basics and Free Tier I was able to successfully apply AWS credits to my AWS account. 

1. From the Billing Console navigate to the credits panel and click on `Redeem credits`.
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/AWS%20Credits1.png)


2. This will take you to the `Redeem Credits` page and in the `Promotion Code` box type in your credits code and Also fill in the security check code in the `Security code` box. At the bottom of that page click `Redeem credit`
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/AWS%20credits2.png)


3. A green banner will appear at the top of the screen to verify that you have redeemed your credits successfully. The amount of your redeemed credits will show in your summary right below.
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/AWS%20credits3.png)


## HomeWork Challenges

### Create an Architectural Diagram CI/CD Pipeline (to the best of your ability) in Lucid Charts
**to insert lucid chart architectural image as proof of work done**

### Use EventBridge to hook up Health Dashboard to SNS and send notification when there is a service health issue

### Review each question in each pillar of the Well-Architected Tool (No specialised lens)



*This File will get updated as I go through this BootCamp to make it is detailed as possible and hopefully it helps someone else*
*Going to work on the well-Architected Tool right now and hopefully I get time to do the health DashBoard too*



