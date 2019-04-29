# Pig-translator


##Installation

An API microservice designed to satisfy all your pig-latin translating needs! Just follow these simple instructions and you'll have yourself an English to Pig-Latin translator in no time.

First, make sure you have Python 3 installed on your computer. If you don't, head on over to the official Python website and install it here: https://www.python.org/downloads/

Next, `git clone` the repo and `cd Pig-Translator` into the folder.

Activate the virtual environment to avoid dependency issues.

For Macs:

`. venv/bin/activate`

For PC:

`venv\Scripts\activate`

Now, within the virtual environment, install Flask.

`pip install Flask`

Now installation is over, we can begin the app:

`export FLASK_APP=hello.py`

`python wsgi.py`

The app should be running at http://127.0.0.1:5000/translate?text=

Append your desired input text to the end of the end point within the text argument. The app will now return that text in pig-latin. Congrats! You've got yourself a fine translator.

 ##Considerations n Stuff
 
 I choose to use Flask for the framework of the API due to it's simplicity in mapping endpoints to functions as well as my past familiarity working with Flask Apps as well as python. 
 
 I usually focus primarily on the front-end side of things, so this is actually my first time building an API from scratch, and although I was initially a little lost in the transition, once I reviewed the documentation everything worked out. Overall, I was very satisfied with everything I learned and am defiantly looking forward to building more apps. 
 
 In total, I spent around 5 hours building the app, with a large portion of that time spent reading up on microservice architecture and documentation.
 
 ##Testing
 As for Unit testing, I made unit tests for all the examples given in the spec, as well as some original sentences included in the end. The unit tests were done with the pytest package, which can be installed with 
 
 `pip install pytest`
 
 and running 
 
 `pytest`
 
 from command line.