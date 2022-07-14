import smtplib
import numpy as np 
import pandas as pd

df = pd.read_csv("Emails.csv")
emails = df.values.flatten()


try:
    senderEmail = "shahzaneer.dev@gmail.com"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(senderEmail, "ENTER_YOUR_PASSWORD_HERE")
    msg = """
    Dear Reciever, this is an automated email from python.
    Please bear it with me.       
"""

    subject = "Python Automated Msg"
    body = "subject: {}\n\n{}".format(subject, msg)


    for i in emails:
        server.sendmail(senderEmail, i, body)

    server.quit()

    print("your details have been emailed successfully!")

except Exception as f:
    print("Please try again ! we found a connectivity issue !")
    print(f)

finally:
    print("Thanks for using our services ")

    
    
    
