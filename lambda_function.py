import json
import boto3

ses = boto3.client('ses', region_name='ap-south-1')

SENDER = "sai.preetham2005@gmail.com"
RECIPIENT = "sai.preetham2005@gmail.com"

def lambda_handler(event, context):
    try:
        if 'body' in event:
            data = json.loads(event['body'])
        else:
            data = event

        name = data['name']
        email = data['email']
        message = data['message']

        subject = f"New Contact Message from {name}"
        body_text = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        response = ses.send_email(
            Source=SENDER,
            Destination={'ToAddresses': [RECIPIENT]},
            Message={
                'Subject': {'Data': subject},
                'Body': {
                    'Text': {'Data': body_text}
                }
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'text/plain'
            },
            'body': "Email sent successfully! 📧"
        }

    except Exception as e:
        print("SES Email Error:", str(e))
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'text/plain'
            },
            'body': f"Error sending message: {str(e)}"
        }