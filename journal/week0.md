# Week 0 — Billing and Architecture

## Required Homework/Tasks

### Conceptual Architectural Diagram (Napkin Diagram)
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
**to insert billing image as proof of work done**

### Using CloudShell

## HomeWork Challenges

### Create an Architectural Diagram CI/CD Pipeline (to the best of your ability) in Lucid Charts
**to insert lucid chart architectural image as proof of work done**

### Use EventBridge to hook up Health Dashboard to SNS and send notification when there is a service health issue

### Review each question in each pillar of the Well-Architected Tool (No specialised lens)

