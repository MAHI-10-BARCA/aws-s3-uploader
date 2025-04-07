# AWS S3 File Uploader 🗂️☁️

This is a simple Python script that allows you to upload any file to your AWS S3 bucket using the Boto3 SDK.

## 🔧 Features

- Upload any file from your local system to an S3 bucket
- Takes user input for file path and bucket name
- Provides upload success confirmation

## 📦 Requirements

- Python 3.x
- `boto3` library
- AWS CLI configured with valid access and secret keys

## 🧪 Installation

1. Clone the repo or download the script:
2. Install the required Python package:
3.  Make sure your AWS credentials are configured:


## 🚀 Usage

Run the script:

bash
python upload.py

Then follow the prompts:

Enter the path to your local file

Enter your S3 bucket name

📁 Enter the path of the file to upload: C:\Users\mahibalan\Desktop\file.png
☁️  Enter your S3 bucket name: mahibalan-files
✅ Successfully uploaded 'file.png' to S3 bucket 'mahibalan-files'

📁 File Structure
bash
Copy
Edit
aws_s3_uploader/
│
├── upload.py       # Main uploader script
└── README.md       # Project documentation

📌 Notes
Make sure your AWS IAM user has the right permissions (e.g., s3:PutObject)

Bucket name must already exist

Avoid special characters or spaces in file names if possible

🧑‍💻 Author
Mahibalan G
Information Technology – Anna University
GitHub: MAHI-10-BARCA



