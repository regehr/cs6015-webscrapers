# learned from https://pypi.python.org/pypi/googletrans and
# https://docs.python.org/2/library/htmlparser.html

# supports formats: ./a.out url From_lang to_lang or
# ./a.out url to_lang

import urllib.request, sys, webbrowser
from json import JSONDecodeError

from googletrans import Translator
from bs4 import BeautifulSoup

translator = Translator()

if (len(sys.argv) == 4):
    file = sys.argv[3] + sys.argv[2] + '.html'
    with urllib.request.urlopen(sys.argv[1]) as f:
        textbox = BeautifulSoup(f.read(), 'html.parser')
        for tag in textbox.find_all():
            if tag.string is not None:
                try:
                    trans_phrase = translator.translate(tag.string, dest=sys.argv[3], src=sys.argv[2])
                    tag.string.replace_with(trans_phrase.text)
                except JSONDecodeError:
                    continue


elif (len(sys.argv) == 3):
    file = sys.argv[2] + '.html'
    with urllib.request.urlopen(sys.argv[1]) as f:
        textbox = BeautifulSoup(f.read(), 'html.parser')
        for tag in textbox.find_all():
            if tag.string is not None:
                try:
                    trans_phrase = translator.translate(tag.string, dest=sys.argv[2])
                    tag.string.replace_with(trans_phrase.text)
                except JSONDecodeError:
                    continue

else:
    print("Error, improper format. try: [program] [url] [to_language] [from_language]")
    print("or:  [program] [url] [to_language]")
    sys.exit()

f = open(file,'w')
page = str(textbox)
f.write(page)
f.close()

#Change path to reflect file location
filename = 'file:///Users/westleykirkham/PycharmProjects/Translator/' + file
webbrowser.open_new_tab(filename)
