#!/usr/bin/python

#Example for using a Raspberry Pi as a basic security alarm. This code has no warranty, and I'm not responsible for what you do with it. Do not use unless you agree to hold me harmless. Feel free to copy/steal/etc.
#listens for a change in switch state and sends an email if it does
#Author: Jeffrey DeYoung; 28 Jan 19
#usage: nohup sudo ./secWatcher.py & (or set it up to run as a service, etc)

import RPi.GPIO as GPIO
import time
import datetime
import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def main():
	printWithDate("Sec listener starting up...")
	GPIO.setmode(GPIO.BOARD) #use board pin (logical) pin numbers
	pin = 19 # set the pin you want to use here; change this as needed
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	#  use pin# ^  input ^    ^ pin gets power when switch is tripped: https://www.raspberrypi.org/forums/viewtopic.php?t=87292
	printWithDate("Sec listener started successfully.") #log that we can access the GIPO
	#sys.stdout.flush() #force to print all messages now
	GPIO.add_event_detect(pin, GPIO.RISING, callback=stateChange, bouncetime=1000) #set callback fuction; trigger if the switch is closed (RISING); you can change this to "FALLING" for having the switch opened, or "BOTH" for having it change state (open to close or vise-versa)
	while True:
		time.sleep(1000) #do nothing once everything is setup; just wait

	GPIO.cleanup() #cleanup; not sure if this will ever get called


# our call back function; gets called anytime the switch state gets changed
def stateChange(switch_state):
	printWithDate("Switch state: " + str(switch_state))
	sendEmail(); #send an email! Or do whatever else you want here... just don't be stupid (ex: don't use this to trigger a call to the police, or lock in a burgler)

# helper to log our prints with the date
def printWithDate(toPrint):
	print "["+str(datetime.datetime.now())+"] " + toPrint
	sys.stdout.flush() #force to print all messages now

#def send email
def sendEmail():
	email_from = "<email username here>" #email username
	server = smtplib.SMTP('smtp.gmail.com', 587)#if your using gmail to send this; if not, use your own server name/port
	server.starttls() #use TLS encryption to connect to the mail server
	server.login(email_from, "<email password here>")
    msg = MIMEMultipart()
 	msg_str = str("Security Alarm Triggered! " + str(datetime.datetime.now())) #subject/message for the email
	msg.attach(MIMEText(msg_str, 'plain'))
	msg['Subject'] = msg_str 
	to = [] # declare that we're using an array for the "TO:" list
	to.append('<email address one here>')
	to.append('<email address two here>') #add as many here as you want
	server.sendmail(email_from, to, msg.as_string())
	server.quit()
	printWithDate("Email sent!")


if __name__ == "__main__": main()

