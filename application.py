from flask import Flask, request, redirect

application = Flask(__name__)

#####################
# Debug Mode Switch #
#####################


# application.config['FLASK_ENV'] = 'development'
application.config['FLASK_DEBUG'] = True


############
# methods #
############

def isVowel(c):
    c = ord(c.lower())
    if c == 97 or c == 101 or c == 105 or c == 111 or c == 117 or c == 121:
        return True
    return False

# finds index of first vowel. if there is none, return len - 1
def findFirstVowel(word):
    for i in range(len(word)):
        if isVowel(word[i]):
            return i
    return len(word) - 1


def translateWord(word):
    if not word[0].isalpha():
        return word
    firstVowel = findFirstVowel(word)

    # for consonant(s)
    if firstVowel >= 1:
        # handle capitalization
        if word[0].isupper():
            if len(word) > 1:
                word = word[:firstVowel].lower() + word[firstVowel].upper() + word[firstVowel + 1:]
            else:
                word = word[:firstVowel].lower() + word[firstVowel].upper()
        return word[firstVowel:] + word[:firstVowel] + 'ay'

    # for everything else including vowels
    else:
        return word + 'ay'

def translateSentence(text):
    output = ""
    for word in text.split():
        if len(word) > 1 and not word[-1].isalpha():
            output += translateWord(word[:-1]) + word[-1] + ' '
        else:
            output += translateWord(word) + ' '
    if len(output) > 0:
        return output[:-1]
    return output


#####################
# application Route #
#####################

@application.route('/')
def home():
    return redirect('/translate')

@application.route('/translate', methods=['GET'])
def translate():
    if 'text' in request.args:
        text = str(request.args['text'])
        return translateSentence(text)
    else:
        return "No text field given. Please add you text input into the text argument."


