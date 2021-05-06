# Sending emails without attachments using Python.
# importing the required library. 
import smtplib 
  
# creates SMTP session 
email = smtplib.SMTP('smtp.gmail.com', 587) 
  
# TLS for security 
email.starttls() 
  
# authentication
# compiler gives an error for wrong credential. 
email.login("remtask@gmail.com", "Taskrem@2021") 
  
# message to be sent 
message = "HELLO THIS IS TASKREM"
  
# sending the mail 
email.sendmail("remtask@gmail.com", "hi5daksh@gmail.com", message) 
  
# terminating the session 
email.quit()