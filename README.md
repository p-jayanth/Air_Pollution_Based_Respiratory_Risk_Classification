PROJECT OVERVIEW

  This project aims to predict respiratory diseases such as asthma and pulmonary fibrosis based on air quality index (AQI) and pollutant concentration levels. By leveraging machine learning models, we     lassify high-risk areas for respiratory diseases based on environmental factors. The project is deployed using AWS services, including AWS Lambda, AWS ECR, and API Gateway, with containerization using   Docker.

Features:-

  Train machine learning models using AQI and pollutant data

  Deploy models using AWS Lambda with Docker containers

  API integration for real-time predictions

  Secure deployment with AWS IAM and AWS CLI

  Test API responses using Postman

![Screenshot 2025-03-24 135648](https://github.com/user-attachments/assets/e08f3310-8abe-4d50-8ccb-636c01e1a883)

Installation and Setup

Step 1: Install Dependencies

Install the required packages using:

![Screenshot 2025-03-24 135901](https://github.com/user-attachments/assets/6ba304f6-27c8-4bfa-9d10-4dc14f1a33d5)


Step 2: Train the Model

Run the training script to develop the necessary models:

![Screenshot 2025-03-24 135946](https://github.com/user-attachments/assets/091f1fe6-53a6-4480-9f0d-de6cc1146aea)



Step 3: Set Up AWS CLI

Download and configure AWS CLI with your security credentials:

![Screenshot 2025-03-24 140045](https://github.com/user-attachments/assets/e0b8f279-4217-43ec-b0df-51d9c73f237d)


Step 4: Set Up Docker

Download and install Docker Desktop.

Step 5: Push Docker Image to AWS ECR

1)Create an AWS ECR repository:
  aws ecr create-repository --repository-name air-pollution-risk-classification
  
2)Authenticate Docker to AWS ECR:
  aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com
  
3)Tag and push the image:

  docker tag air_pollution_risk_model:latest <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/air-pollution-risk-classification:latest
  docker push <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/air-pollution-risk-classification:latest

Step 6: Deploy on AWS Lambda

1)Create an AWS Lambda function.

2)Select Container Image as the deployment package.

3)Choose the ECR image and deploy.

4)Set up API Gateway with the AWS Proxy template.


Step 7: Testing the API

Use Postman or a similar tool to test the deployed Lambda function. Send a POST request with JSON data to the API Gateway endpoint:

![Screenshot 2025-03-24 140827](https://github.com/user-attachments/assets/4d56fbb1-a599-4d27-b1b3-e0d172f562b1)

Credit

This project is inspired by the work of siddhardhan23. The original project, deploy-ml-model-aws-lambda-docker-main, served as the foundation for this implementation.

