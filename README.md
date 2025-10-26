# Data Engineering Assignment
This project demonstrates a complete data pipeline that extracts movie data from The Movie Database (TMDb) API, processes it, and stores it in Snowflake using AWS services like Lambda, S3, SNS, and SQS.
# Workflow Overview
<img width="767" height="422" alt="image" src="https://github.com/user-attachments/assets/785a4fa2-aa01-43ff-9f08-ab024e5c3835" />

## 1. Data Extraction with AWS Lambda
A Python script running on an AWS Lambda function is scheduled to periodically fetch movie data from the https://www.themoviedb.org/documentation/api.
The Lambda function extracts relevant movie metadata such as:
Movie ID
Title
Overview
Release Date
Popularity
Vote Average
Vote Count
<img width="1365" height="681" alt="image" src="https://github.com/user-attachments/assets/285ddc5b-c591-432d-bbf0-df9e700988ca" />
## 2. Storing Extracted Data in Amazon S3
The extracted data is saved as CSV files in an Amazon S3 bucket. 
<img width="1362" height="610" alt="image" src="https://github.com/user-attachments/assets/cbedf888-8c06-4952-a724-ad4e9c9da112" />
## 3. Ingesting Data into Snowflake via Snowpipe
Using Snowpipe, the data from the S3 bucket is automatically ingested into a Snowflake table (raw_data).
This is achieved by configuring:
S3 Event Notifications
Amazon SNS (Simple Notification Service)
Amazon SQS (Simple Queue Service)
<img width="1365" height="682" alt="image" src="https://github.com/user-attachments/assets/caab1e0a-09ce-4c5d-94b0-9841de37c40a" />
## 4. Data Transformation Using Streams and Tasks
A Snowflake Stream is created on the raw_data table to capture changes (inserts/updates).
A Snowflake Task is scheduled to run a MERGE operation that:
Standardizes the Overview field
Categorizes movies based on rating and vote count
Extracts year, month, and decade from the release date
Inserts or updates records in the transformed_data table
<img width="1362" height="686" alt="image" src="https://github.com/user-attachments/assets/62615340-6f10-4082-93c0-378c3b607703" />
<img width="1365" height="679" alt="image" src="https://github.com/user-attachments/assets/6fefe29a-66de-464e-b847-910763fe3728" />




