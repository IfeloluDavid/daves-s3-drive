Dave’s Drive is a scalable, AWS-powered cloud storage system that allows users to securely upload, store, and retrieve files of any size. This project explores various AWS services to implement a serverless, containerized file storage solution.

🛑 Problem & Solution

The Problem:

Modern applications require secure, scalable, and cost-effective cloud storage solutions. Uploading large files directly to a backend can create performance bottlenecks and security risks.

The Solution:

Instead of uploading files directly to the backend, Dave’s Drive generates a pre-signed S3 URL that enables users to upload files directly to Amazon S3. This ensures scalability, security, and efficiency while offloading storage concerns from the backend.

⚡ Why This Approach?

While there are simpler ways to achieve file storage, such as directly integrating S3 with a frontend, this project was built using multiple AWS services to:
✅ Enhance security by preventing direct S3 access.
✅ Improve scalability using serverless functions.
✅ Explore AWS services like ECS, Lambda, and API Gateway for real-world applications.

🏗️ Architecture & Workflow

How Dave’s Drive Works:

Deployment:

The application runs on Elastic Container Service (ECS) with containers stored in Elastic Container Registry (ECR).

File Upload Flow:

The frontend calls an API Gateway endpoint.

API Gateway triggers a Lambda function to generate a pre-signed URL.

The user uploads files via the URL, storing them securely in Amazon S3.

File Retrieval Flow:

Users navigate to a page displaying all uploaded files.

A second Lambda function (invoked via Lambda URL) fetches metadata from S3.

Users can download files directly from the interface.

Architecture Diagram

📌 Add an architecture diagram here if available.

🚀 AWS Services Used

Service

Purpose

Amazon S3

Stores all uploaded files securely.

API Gateway

Routes API requests for file uploads and retrievals.

AWS Lambda

Generates pre-signed URLs and fetches file metadata.

Elastic Container Service (ECS)

Runs the application as a containerized service.

Elastic Container Registry (ECR)

Stores container images for ECS deployment.

Walkthrough: https://youtu.be/Lbr8xFj-PNU
