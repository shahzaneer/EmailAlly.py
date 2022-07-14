from pdf_mail import sendpdf
import pandas as pd
import numpy as np

# reading csv file into a data Frame
df = pd.read_csv("Emails.csv")
# making a numpy array by the dataFrame Values
emails =  np.array(df.values.flatten())



senderEmail = 'shahzaneer.dev@gmail.com'
senderPass = 'ENTER_YOUR_PASSWORD_HERE'
subject = "Resume for Data Science Intern"
bodyEmail = """
Assalam-O-Alaikum!\n
THIS IS PYTHON AUTOMATED EMAIL KINDLY IGNORE IT >> 👩
\tHope this email finds you in the best of health and spirits!\n
This is Shahzaneer Ahmed ,CS Sophomore CUI Islamabad.
I'm looking for an opportunity as Data Science Intern.
My resume is attached for further info about me.\n
Thank you\n
Shahzaneer Ahmed\n
Flutter Islamabad\n
GDSC CUI\n
shahzaneer.dev@gmail.com\n
"""

filename = 'ShahzaneerAhmedCV'
location = "E:\EmailAlly.py/"

for i in emails:
    send = sendpdf(senderEmail,i,senderPass,subject,bodyEmail,filename,location)
    send.email_send()

print("DONE THAT")
