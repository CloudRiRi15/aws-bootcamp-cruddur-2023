![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/aws-week-0-1.jpg)

# TABLE OF CONTENTS

 + [Introduction](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#introduction)
 + [Project Scenario](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#project-scenario-woman_technologist)
 + [Pre-Requisites Technologies and Set-up Instructions](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#technologies-and-pre-requisites)
 + [The Challenges and Set-Backs](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#the-challenges-and-set-backs)
 + [Week 0 Homework Required Tasks](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/week0.md#required-homeworktasks)
   - [Watch Week 0 - Live Streamed Video and other required videos for Week 0](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/week0.md#watched-the-live-stream-video-and-all-required-videos-for-week-0-as-outlined-in-the-student-portal-videos-can-be-found-on-the-bootcamp-official-playlist)
   - [Recreate Conceptual Diagram in Lucid Charts or on a Napkin](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#conceptual-architectural-diagram-napkin-diagram)
   - [Recreate Logical Architectual Diagram in Lucid Charts]()
   - [Create an Admin User](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#create-and-iam-user)
   - [Use CloudShell](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/week0.md#using-cloudshell)
   - [Generate AWS Credentials](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#generating-aws-credentials)
   - [Install AWS CLI](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/edit/main/journal/week0.md#install-aws-cli-via-gitpod)
   - [Create a Billing Alarm](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/week0.md#set-a-billing-alarm)
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

### Create an IAM User

From the root account navigate to IAM console. You will notice that there will be a few recommendations from the `IAM dashboard` that will be in red. You will need to do those things as best practice. See image below showing some of the recommendations in my root account.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Root%20User%20Credentials%20before%20MFA%20and%20IAM%20Role.png)

What we are going to do now is to create a `User`. From the `IAM console` select `Users` and Click `Add Users`.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/create%20user%201.png)
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/create%20user%202.png)

From the `Specify user details` page enter the details for the user you want to create by filling in the `User name` box. Tick the `Provide user access to the AWS Management Console` box and Select the `I want to create an IAM user` option`.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/create%20user%203.png)

Scroll down to the `Console Password` panel and fill out the details according to your preferences. You can either select an `Autogenerated password` or a `Custom password`. I chose the autogenerated password. Click `Next`.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/create%20user%204.png)

Next you set permissions for the user you are creating by selecting from the different option boxes shown. Select the `Add user to group option`. If you dont have a group created you will click the `Create group` tab and create an Admin Group with full access and click on `Create group`.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/create%20user%205.png)
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/create%20user%206.png)

A green banner will show at the top of your console to confirm that your Admin user group was created.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/create%20user%207.png)

Once your group is created click the checkbox to add your user to the newly created `Admin group` and click `Create user`.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/create%20user%208.png)

Congratulations you have created an `IAM user` with Admin permissions. Notice that your `IAM user` does not have `Access keys` enabled.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/CREATED%20IAM%20USER%20PROOF.png)

### Generating AWS Credentials

The next step is to create AWS Credentials for your newly created `IAM user`. Firstly log out of the root account and log in to your `IAM user` account. Using the `console sign-in link`. Follow the prompts to create a new password for your `IAM user`

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/access%20keys%20step%201a.png)
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/access%20keys%20step%201b.png)

Once you are logged into the `IAM user` account navigate to the `IAM console` and select `User` from the panel. Click the checkbox to select the `IAM user` you just created.
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/access%20keys%20step%201c.png)

We have to navigate our way to the security credentials tab inorder to get access to create access keys for this user. Select the `Security Credentials` tab. Scroll down to `Access Keys`. Notice that the are no access keys. Click `Create access keys`

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/access%20keys%20step%201d.png)
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/access%20keys%20step%201.png)

This will take you to the `Access key best practices & alternatives` page. From the options below select `Command Line Interface (CLI)`.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/access%20keys%20step%202.png)

Scroll down and check the box `I understand the above reccomendation and want to proceed to create access key`. Click `Next`.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/access%20keys%20step%203.png)

Under no circumstance do you share your `Access key` with anyone asit is a huge security risk. You can download your `.csv` file to save your access key. Click `Done`.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/access%20keys%20step%204.png)

Notice that your `Access key` status is `Active`. Congratulations you have successfully created access keys for the IAM user. 

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Access%20keys%20step%205%20created.png)

### Install AWS CLI via Gitpod.

From your Github Bootcamp repository, launch Gitpod by clicking the `Gitpod` button.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/CLI%20install%201.png)

Once your enviroment has been provisioned in `Gitpod`, proceed to the terminal and run the code below to install `AWS CLI` into our Gitpod enviroment.

``` curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install```
      
In my case I ran the code and got back an error as shown in the image below.

![Error when trying to install AWS CLI](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/CLI%20install%203%20%20Gitpod%20Command%20not%20found.png)

After running into the `command not found error`, I had to debug and find reasons why it was not working and if there are alternative ways to complete the installation. I looked through the [Gitpod Documents](https://www.gitpod.io/guides/integrate-aws-cli-ecr) and found an alternative code to install the CLI onto `Gitpod`. I found the code below:

``` curl -fSsl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip -qq awscliv2.zip
sudo ./aws/install --update
rm awscliv2.zip ```

![Code to Install AWS CLI on Gitpod](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/CLI%20install%204%20on%20Gitpod%20alternative%20success.png)


I ran the first line of the code using the `curl -fSsl` command and was able to successfully download the `awscliv2.zip` file for installation onto my `Gitpod` enviroment. 

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/CLI%20install%205%20success%20main.png)

Out of curiosity I asked `ChatGPT` what exactly this command does as a way to get an understanding of why the first command had failed and `ChatGPT` gave me the response below:

![ChatGPT breakdown of the Command](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/CLI%20install%20chatgpt.png)

Now that the `awscliv2.zip` file has been downloaded its ready for installation onto your `Gitpod` enviroment.















### Set an AWS Budget
From the root account, grant the IAM user billing access and permissions. **NB** if you do not grant the IAM user billing access, the IAM user will not be able to access the billing console. 

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Create%20Budget%201.png)

Once you grant your IAM user access to billing permissions, log in to your **IAM user account** to set a budget. I created Zero Spend Budget for this BootCamp, since the goal was to make use of the free-tier account. This was very simple and staightforward to implement.

From the AWS `Billing Console` >Select `Budgets` > Click on `Create Budget`. 

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Create%20Budget%202.png)
![](![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Create%20Budget%203.png))

This will to take you to the `Choose Budget Type` page. In the `Budget Setup` panel >Select `Use a template (*simplified*)`. The `Templates - new` selection boxes will show as per image below:

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Create%20Budget%204.png)

From the `Templates- new` options, I selected the `Zero Spend Budget` and Click `Create Budget`. My Zero Spend budget was created from the template.
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Create%20Budget%205.png)

### Set a Billing Alarm

For the task of creating a billing alarm, I chose to use the AWS CLI. Inorder for you to create a billing alarm you follow the following steps:

Step 1: Create an SNS Topic

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Step%201%20Create%20an%20sns%20Topic.png)

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Step%202%20Run%20Command.png)

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Step%203b%20From%20AWS%20Console%20notice%20the%20created%20Topic%20is%20pending%20Confirmation.png)

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Step%203b%20From%20AWS%20Console%20notice%20the%20created%20Topic%20is%20pending%20Confirmation.png)

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/Step%204%20Confirm%20Subscription%20Via%20link%20sent%20to%20your%20email.png)






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



