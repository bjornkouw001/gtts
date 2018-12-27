from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from weather import Weather

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"
    
# 
        




    def secondTweetArticle():
        talkToMe("There is an article in this Story, I can read it if you want.")


    def secondTweet():
        talkToMe("US bank 'sorry' for calling police on black man cashing pay cheque")
        secondTweetArticle()

    def Image_Y_N():
        talkToMe("I can send you the picture from Donald Trump tweet on your phone.")
        picture = myCommand()
        if 'yes' in picture:
            talkToMe("Okee send let's go to the next tweet")
            secondTweet()

        elif "No" in picture:
            talkToMe("Oke not send let's go to the next tweet ")

    # Twitter feed open en naar Image ja of nee 

    if 'my friends their Twitter messages' in command:
        talkToMe("Russia, Iran, Syria and many others are not happy about the U.S. leaving, despite what the Fake News says, because now they will have to fight ISIS and others, who they hate, without us. I am building by far the most powerful military in the world. ISIS hits us they are doomed!")
        Image_Y_N()


    if 'lost twitter messages from my friends' in command:
        talkToMe("Russia, Iran, Syria and many others are not happy about the U.S. leaving, despite what the Fake News says, because now they will have to fight ISIS and others, who they hate, without us. I am building by far the most powerful military in the world. ISIS hits us they are doomed!    ")
        Image_Y_N()

    if 'My friends their twitter updates' in command:
        talkToMe("Russia, Iran, Syria and many others are not happy about the U.S. leaving, despite what the Fake News says, because now they will have to fight ISIS and others, who they hate, without us. I am building by far the most powerful military in the world. ISIS hits us they are doomed!    ")
        Image_Y_N()

    if 'What are my friends saying on twitter?' in command:
        talkToMe("Russia, Iran, Syria and many others are not happy about the U.S. leaving, despite what the Fake News says, because now they will have to fight ISIS and others, who they hate, without us. I am building by far the most powerful military in the world. ISIS hits us they are doomed!    ")
        Image_Y_N()
    if 'What are my friends saying on twitter?' in command:
        talkToMe("Russia, Iran, Syria and many others are not happy about the U.S. leaving, despite what the Fake News says, because now they will have to fight ISIS and others, who they hate, without us. I am building by far the most powerful military in the world. ISIS hits us they are doomed!    ")
        Image_Y_N()

    if 'my followers their Twitter messages' in command:
        talkToMe("Russia, Iran, Syria and many others are not happy about the U.S. leaving, despite what the Fake News says, because now they will have to fight ISIS and others, who they hate, without us. I am building by far the most powerful military in the world. ISIS hits us they are doomed!")
        Image_Y_N()


    if 'lost twitter messages from my followers' in command:
        talkToMe("Russia, Iran, Syria and many others are not happy about the U.S. leaving, despite what the Fake News says, because now they will have to fight ISIS and others, who they hate, without us. I am building by far the most powerful military in the world. ISIS hits us they are doomed!    ")
        Image_Y_N()

    if 'My followers their twitter updates' in command:
        talkToMe("Russia, Iran, Syria and many others are not happy about the U.S. leaving, despite what the Fake News says, because now they will have to fight ISIS and others, who they hate, without us. I am building by far the most powerful military in the world. ISIS hits us they are doomed!    ")
        Image_Y_N()

    if 'What are my followers saying on twitter?' in command:
        talkToMe("Russia, Iran, Syria and many others are not happy about the U.S. leaving, despite what the Fake News says, because now they will have to fight ISIS and others, who they hate, without us. I am building by far the most powerful military in the world. ISIS hits us they are doomed!    ")
        Image_Y_N()
    if 'What are my followers saying on twitter?' in command:
        talkToMe("Russia, Iran, Syria and many others are not happy about the U.S. leaving, despite what the Fake News says, because now they will have to fight ISIS and others, who they hate, without us. I am building by far the most powerful military in the world. ISIS hits us they are doomed!    ")
        Image_Y_N()



# Twitter open maar niet gespecificeerd welke feed 

    if 'What is going on on twitter' in command:
        talkToMe("Which category tweets do you want to open? I can open your friends or news tweets for example.")
        which_feed = myCommand()
        if "friends" in which_feed:
            talkToMe("hmm Let me look for the most important tweets from your friends")

        elif "friends" in which_feed:
            talkToMe("hmm Let me look for the most important tweets from your followers")
        else: 
            talkToMe("Couldnt find any tweets in this category")


    if 'twitter' in command:
        talkToMe("Which category tweets do you want to open? I can open your friends or news tweets for example.")
        which_feed = myCommand()
        if "friends" in which_feed:
            talkToMe("hmm Let me look for the most important tweets from your friends")

        elif "friends" in which_feed:
            talkToMe("hmm Let me look for the most important tweets from your followers")
        else: 
            talkToMe("Couldnt find any tweets in this category")

    if 'Open twitter' in command:
        talkToMe("Which category tweets do you want to open? I can open your friends or news tweets for example.")
        which_feed = myCommand()
        if "friends" in which_feed:
            talkToMe("hmm Let me look for the most important tweets from your friends")

        elif "friends" in which_feed:
            talkToMe("hmm Let me look for the most important tweets from your followers")
        else: 
            talkToMe("Couldnt find any tweets in this category")

    if 'twitter' in command:
        talkToMe("Which category tweets do you want to open? I can open your friends or news tweets for example.")
        which_feed = myCommand()
        if "friends" in which_feed:
            talkToMe("hmm Let me look for the most important tweets from your friends")

        elif "friends" in which_feed:
            talkToMe("hmm Let me look for the most important tweets from your followers")
        else: 
            talkToMe("Couldnt find any tweets in this category")

    if 'I would like to open twitter' in command:
        talkToMe("Which category tweets do you want to open? I can open your friends or news tweets for example.")
        which_feed = myCommand()
        if "friends" in which_feed:
            talkToMe("hmm Let me look for the most important tweets from your friends")

        elif "friends" in which_feed:
            talkToMe("hmm Let me look for the most important tweets from your followers")
        else: 
            talkToMe("Couldnt find any tweets in this category")

    if 'twitter open' in command:
        talkToMe("Which category tweets do you want to open? I can open your friends or news tweets for example.")
        which_feed = myCommand()
        if "friends" in which_feed:
            talkToMe("hmm Let me look for the most important tweets from your friends")

        elif "friends" in which_feed:
            talkToMe("hmm Let me look for the most important tweets from your followers")
        else: 
            talkToMe("Couldnt find any tweets in this category")












    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'John' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('John Fisher', 'JARVIS2.0@protonmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

        else:
            talkToMe('Sorry I do not understand you, try to say something else.')


talkToMe('Hi Dan, how can I help you?')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())