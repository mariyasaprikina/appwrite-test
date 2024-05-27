from appwrite.client import Client
from appwrite.services.mails import Mails
import os
import requests


# This is your Appwrite function
# It's executed each time we get a request
def main(context):
    client = (
         Client()
         .set_endpoint("https://cloud.appwrite.io/v1")
         .set_project(os.environ["APPWRITE_FUNCTION_PROJECT_ID"])
         .set_key(os.environ["APPWRITE_API_KEY"])
     )

    # Create an instance of the Mails service
    mails = Mails(client)

    # Send an email
    mail_response = mails.create(
        subject='Test Email',
        body='This is a test email sent from Appwrite.',
        to='mariasaprykina07@gmail.com',
        from_email='your-email@example.com',
        from_name='Mariya Saprikina',
        reply_to='your-email@example.com',
        cc=[],
        bcc=[]
        )

    context.log(mail_response)

    # You can log messages to the console
    context.log("Hello, Logs!")

    # If something goes wrong, log an error
    context.error("Hello, Errors!")

    # The `ctx.req` object contains the request data
    if context.req.method == "GET":
        # Send a response with the res object helpers
        # `ctx.res.send()` dispatches a string back to the client
        return context.res.send("Hello, World!")

    # `ctx.res.json()` is a handy helper for sending JSON
    return context.res.json(
        {
            "motto": "Build like a team of hundreds_",
            "learn": "https://appwrite.io/docs",
            "connect": "https://appwrite.io/discord",
            "getInspired": "https://builtwith.appwrite.io",
        }
    )



def get_page_content(url):  
    response = requests.get(url)
    response.raise_for_status()
    return response.text
