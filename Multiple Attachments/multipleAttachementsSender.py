from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import schedule as aukaat
import time
import pandas as pd , numpy as np

df = pd.read_csv("Emails.csv")
emails = df.values.flatten()

# initialize connection to our
# email server, we will use gmail here
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()

# Login with your email and password
smtp.login('shahzaneer.dev@gmail.com', 'ENTER_YOUR_EMAIL_PASSWORD_HERE')


# send our email message 'msg'
def message(subject="Python Automation Update",
			text="", img=None,
			attachment=None):
	
	# build message contents
	msg = MIMEMultipart()
	
	# Add Subject
	msg['Subject'] = subject
	
	# Add text contents
	msg.attach(MIMEText(text))

	# Check if we have anything
	# given in the img parameter
	if img is not None:
		
		# Check whether we have the lists of images or not!
		if type(img) is not list:
			
			# if it isn't a list, make it one
			img = [img]

		# Now iterate through our list
		for one_img in img:
			
			# read the image binary data
			img_data = open(one_img, 'rb').read()
			# Attach the image data to MIMEMultipart
			# using MIMEImage, we add the given filename use os.basename
			msg.attach(MIMEImage(img_data,name=os.path.basename(one_img)))

	# We do the same for
	# attachments as we did for images
	if attachment is not None:
		
		# Check whether we have the
		# lists of attachments or not!
		if type(attachment) is not list:
			
			# if it isn't a list, make it one
			attachment = [attachment]

		for one_attachment in attachment:

			with open(one_attachment, 'rb') as f:
				
				# Read in the attachment
				# using MIMEApplication
				file = MIMEApplication(
					f.read(),
					name=os.path.basename(one_attachment))
			file['Content-Disposition'] = f'attachment;\
			filename="{os.path.basename(one_attachment)}"'
			
			# At last, Add the attachment to our message object
			msg.attach(file)
	return msg


def mail():
	# Call the message function
	msg = message("Hello Hello Hello","I'm Automated Email and you are probably my Friend's Friend. I'm making bulk email sender with attachements of different kinds also it will schedule when to send email as well ",
				r"E:\EmailAlly.py/Pakistan.jpeg",    
				r"E:\EmailAlly.py/gdsc-logo.gif")

	# Make a list of emails, where you wanna send mail
	to = emails

	# Provide some data to the sendmail function!
	smtp.sendmail(from_addr="shahzaneer.dev@gmail.com",
				to_addrs=to, msg=msg.as_string())

aukaat.every(2).seconds.do(mail)
aukaat	
		
# Finally, don't forget to close the connection
smtp.quit()

while True:
    aukaat.run_pending()
    time.sleep(1)
    
