# libraries to be imported for email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PIL import Image

import speech_recognition as sr
from playsound import playsound
r = sr.Recognizer()

fromaddr = "halomyth7@gmail.com"
toaddr = "gannapu.reddy.17csc@bml.edu.in"

# Welcome Messages

##1 Namaskaram and Welcome to BML
playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/bot_welcome.mpeg")
##2 Bot name
playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/bot_name.mpeg")
##3 Bot tasks and ask for input
playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/bot_tasks.mpeg")
playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/bot_help.mp3")

# User task Input
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

try:
    option = r.recognize_google(audio, language = "te-IN")
    print("You said " + option)    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")

# Task 1: Send Message
if option == "1":
    # 1.1: Name
    playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/user_name.mpeg")
    with sr.Microphone() as source: # use the default microphone as the audio source
        audio = r.listen(source)

    try:
        user_name = r.recognize_google(audio, language = "te-IN")
        print("Name: " + user_name) # recognize speech using Google Speech Recognition
    except LookupError: # speech is unintelligible
        print("Could not understand audio")

    # 1.2: Location
    playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/user_location.mpeg")
    with sr.Microphone() as source: # use the default microphone as the audio source
        audio = r.listen(source)

    try:
        user_location = r.recognize_google(audio, language = "te-IN")
        print("Location " + user_location) # recognize speech using Google Speech Recognition
    except LookupError: # speech is unintelligible
        print("Could not understand audio")

    # 1.3: Message recipient
    print("Who should the message be sent to?")
    with sr.Microphone() as source: # use the default microphone as the audio source
        audio = r.listen(source)

    try:
        user_professor = r.recognize_google(audio, language = "en")
        if user_professor == "Anish":
            toaddr = "aneesh.vandanapu.17cse@bml.edu.in"
        elif user_professor == "Atul Mishra":
            toaddr = "gannapu.reddy.17csc@bml.edu.in"
        print("Recipient " + user_professor) # recognize speech using Google Speech Recognition
    except LookupError: # speech is unintelligible
        print("Could not understand audio")

    # 1.4: Message to be sent
    playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/user_message.mpeg")
    with sr.Microphone() as source: # use the default microphone as the audio source
        audio = r.listen(source)

    try:
        user_message = r.recognize_google(audio, language = "te-IN")
        print("Message: " + user_message) # recognize speech using Google Speech Recognition
    except LookupError: # speech is unintelligible
        print("Could not understand audio")

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Hey! You have a message from reception"

    # string to store the body of the mail
    body = "From: " + user_name + "\nLocation: " + user_location + "\nMessage: " + user_message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "gSAI@2000")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

    # 1.5: Message Sent
    playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/user_message_sent.mp3")
    print("Your message has been sent.")


# Task 2: Meet someone
elif option == "2":
    # 2.1: Name
    playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/user_name.mpeg")
    with sr.Microphone() as source: # use the default microphone as the audio source
        audio = r.listen(source)

    try:
        user_name = r.recognize_google(audio, language = "te-IN")
        print("Name: " + user_name) # recognize speech using Google Speech Recognition
    except LookupError: # speech is unintelligible
        print("Could not understand audio")

    # 2.2: Location
    playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/user_location.mpeg")
    with sr.Microphone() as source: # use the default microphone as the audio source
        audio = r.listen(source)

    try:
        user_location = r.recognize_google(audio, language = "te-IN")
        print("Location " + user_location) # recognize speech using Google Speech Recognition
    except LookupError: # speech is unintelligible
        print("Could not understand audio")

    # 2.3: Meet whom?
    playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/user_who_meet.mpeg")
    with sr.Microphone() as source: # use the default microphone as the audio source
        audio = r.listen(source)

    try:
        user_professor = r.recognize_google(audio, language = "en")
        if user_professor == "Anish":
            toaddr = "aneesh.vandanapu.17cse@bml.edu.in"
        elif user_professor == "Atul Mishra":
            toaddr = "gannapu.reddy.17csc@bml.edu.in"
        print("Meet whom: " + user_professor) # recognize speech using Google Speech Recognition
    except LookupError: # speech is unintelligible
        print("Could not understand audio")

    # 2.4: Meet why?
    playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/user_why_meet.mpeg")
    with sr.Microphone() as source: # use the default microphone as the audio source
        audio = r.listen(source)

    try:
        user_meet_reason = r.recognize_google(audio, language = "te-IN")
        print("Meeting reason: " + user_meet_reason) # recognize speech using Google Speech Recognition
    except LookupError: # speech is unintelligible
        print("Could not understand audio")

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Hey! You have " + user_name + " waiting for you at the reception"

    # string to store the body of the mail
    body = "From: " + user_name + "\nLocation: " + user_location + "\nReason: " + user_meet_reason

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "gSAI@2000")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

    # 2.3: Please wait for the professor
    playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/user_wait_professor.mp3")
    print("Please wait for a while. Professor will be here.")


# Task 3: Guide
elif option == "3":
    # Go where
    playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/guide_where.mpeg")
    with sr.Microphone() as source: # use the default microphone as the audio source
        audio = r.listen(source)

    try:
        user_destination = r.recognize_google(audio, language = "te-IN")
        print("Guide to: " + user_destination) # recognize speech using Google Speech Recognition
    except LookupError: # speech is unintelligible
        print("Could not understand audio")

    try:
        img = Image.open("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/images/bml_guide.PNG")
        img.show()
    except IOError:
        print("Image not found!")
        pass


else:
    print("Invalid Option")


# Thank you
playsound("C:/Users/AVINASH/PycharmProjects/nlpTermPaper/output_audio/bot_thankyou.mp3")