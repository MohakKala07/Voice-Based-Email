import pyaudio
import platform
import sys
import pyglet
import os
import time
import speech_recognition as sr
import smtplib
import ssl
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
from email.mime.multipart import MIMEMultipart

print("-"*60)
print("       Voice based Email for visually impaired")
print("-"*60)

# To display and speak out project name

s = gTTS(text="Voice based Email for visually impaired", lang='en')
tsname = "name.mp3"
s.save(tsname)

music = pyglet.media.load(tsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

# login from os

login = os.getlogin
print("You are logged In from : "+login())

# To Input Users Email ID

print("Please speak your Email ID")
s = gTTS(text="Please speak your Email ID", lang='en')
tsname = "mail.mp3"
s.save(tsname)

music = pyglet.media.load(tsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Your Mail ID is :")
    mic_audio = r.listen(source)
    print("ok done!!")

try:
    mailID1 = r.recognize_google(mic_audio)
    mailID3 = mailID1.replace("-", "")
    mailID2 = mailID3.replace(" ", "")
    print("You said : "+mailID2)
    s = gTTS(text="You Said:"+mailID2, lang='en')
    tsname = "mailID2.mp3"
    s.save(tsname)

    music = pyglet.media.load(tsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(tsname)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Input of password through speech

print("Please speak your Password")
s = gTTS(text="Please speak your Password", lang='en')
tsname = "password.mp3"
s.save(tsname)

music = pyglet.media.load(tsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Your Password is:")
    mic_audio = r.listen(source)
    print("ok done!!")

try:
    password1 = r.recognize_google(mic_audio)
    password3 = password1.replace("attherate", "@")
    password4 = password3.replace("hashtag", "#")
    password2 = password4.replace(" ", "")
    print("You said : "+password2)
    s = gTTS(text="You Said:" + password2, lang='en')
    tsname = "password2.mp3"
    s.save(tsname)

    music = pyglet.media.load(tsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(tsname)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Type of Command to Perform via this

print("1. Composed a mail.")
s = gTTS(text="option 1. Composed a mail.", lang='en')
tsname = "option1.mp3"
s.save(tsname)

music = pyglet.media.load(tsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

print("2. Check your inbox")
s = gTTS(text="option 2. Check your inbox", lang='en')
tsname = "option2.mp3"
s.save(tsname)

music = pyglet.media.load(tsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

# What Choice of input the Visually Impaired person has made

s = gTTS(text="Your choice ", lang='en')
tsname = "option.mp3"
s.save(tsname)

music = pyglet.media.load(tsname, streaming=False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

# voice recognition part for Choice

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Your choice:")
    mic_audio = r.listen(source)
    print("ok done!!")

try:
    text4 = r.recognize_google(mic_audio)
    text = text4.replace("Tu", "2")
    print("You said : "+text)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# If-Else block for the two choices given

if int(text) == 1:

    # Receiver's mailID

    print("Please speak Receiver's MailID")
    s = gTTS(text="Please speak Receiver's MailID", lang='en')
    tsname = "receiver.mp3"
    s.save(tsname)

    music = pyglet.media.load(tsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(tsname)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Receiver's mailID is:")
        mic_audio = r.listen(source)
        print("ok done!!")

    try:
        receiverID1 = r.recognize_google(mic_audio)
        receiverID3 = receiverID1.replace("-", "")
        receiverID2 = receiverID3.replace(" ", "")
        print("You said : " + receiverID2)
        s = gTTS(text="You Said:" + receiverID2, lang='en')
        tsname = "receiverID2.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# To Listen and accept Subject of Mail

    print("Please speak the Subject")
    s = gTTS(text="Please speak the Subject ", lang='en')
    tsname = "subject.mp3"
    s.save(tsname)

    music = pyglet.media.load(tsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(tsname)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Subject is:")
        mic_audio = r.listen(source)
        print("ok done!!")

    try:
        subject = r.recognize_google(mic_audio)
        print("You said : " + subject)
        s = gTTS(text="Subject:" + subject, lang='en')
        tsname = "subject.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# To Listen and accept Message of Mail

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your message :")
        mic_audio = r.listen(source)
        print("ok done!!")
    try:
        text1 = r.recognize_google(mic_audio)
        print("You said : "+text1)
        s = gTTS(text="Your message:" + text1, lang='en')
        tsname = "msg.mp3"
        s.save(tsname)

        music = pyglet.media.load(tsname, streaming=False)
        music.play()

        time.sleep(music.duration)
        os.remove(tsname)

        msg = text1

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Block where we send mail

    smtp_server = 'smtp.gmail.com'
    port = 465

    context = ssl.create_default_context()
    msg = """
    From:{}
    To:{}
    Subject:{}
    """.format(mailID2, receiverID2, subject)

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(mailID2, password2)
        server.sendmail(mailID2, receiverID2, text1)

    print("Congrats! Your mail has been sent. ")
    s = gTTS(text="Congrats! Your mail has been sent. ", lang='en')
    tsname = "send.mp3"
    s.save(tsname)
    music = pyglet.media.load(tsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)

if int(text) == 2:
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    mail.login(mailID2, password2)
    stat, total = mail.select('Inbox')
    print("Number of mails in your inbox :"+str(total))
    s = gTTS(text="Total mails are :"+str(total), lang='en')
    tsname = "total.mp3"
    s.save(tsname)
    music = pyglet.media.load(tsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)

    # To access unseen mails

    unseen = mail.search(None, 'UnSeen')
    print("Number of UnSeen mails :"+str(unseen))
    s = gTTS(text="Your Unseen mail :"+str(unseen), lang='en')
    tsname = "unseen.mp3"
    s.save(tsname)
    music = pyglet.media.load(tsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)

    # To search mails

    result, data = mail.uid('search', None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', new, '(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    print("From: "+email_message['From'])
    print("Subject: "+str(email_message['Subject']))
    s = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
    tsname = "mail.mp3"
    s.save(tsname)
    music = pyglet.media.load(tsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)

    # For the Body part of mails

    stat, total1 = mail.select('Inbox')
    stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    txt = soup.get_text()
    print("Body :"+txt)
    s = gTTS(text="Body: "+txt, lang='en')
    tsname = "body.mp3"
    s.save(tsname)
    music = pyglet.media.load(tsname, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    mail.close()
    mail.logout()
