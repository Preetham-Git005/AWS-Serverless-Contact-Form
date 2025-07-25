# AWS Serverless Contact Form

This project implements a **serverless contact form** using the following AWS services:
- 🗂️ S3 for hosting the static resume website
- 🛡️ API Gateway to expose a secure HTTP POST endpoint
- ⚙️ AWS Lambda to handle form submissions
- 📧 AWS SES to send email notifications

## 🌐 Live Demo

[Click here to view/download my resume](http://ksaipreetham-resume-site.s3-website.ap-south-1.amazonaws.com/)

## 💡 How It Works

1. User fills the form on the `resume.html` page.
2. On submission, the form sends a POST request to an API Gateway endpoint.
3. API Gateway triggers a Lambda function.
4. Lambda extracts the form data and sends an email using AWS SES.

## 📂 Files

- `resume.html` – Website with the contact form
- `lambda_function.py` – AWS Lambda function code to process the form
- `screenshot.png` – Optional proof of working project

## 🛠️ AWS Stack

- S3 (Static website hosting)
- API Gateway (HTTP API)
- AWS Lambda (Python 3.12)
- Amazon SES (Verified sender email)

## 🧠 Author

[Sai Preetham](https://github.com/Preetham-Git005)
