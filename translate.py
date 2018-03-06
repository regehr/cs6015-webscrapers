# learned from https://pypi.python.org/pypi/googletrans and
# https://docs.python.org/2/library/htmlparser.html
# supports formats ./a.out url From_lang to_lang or
# ./a.out url to_lang
import urllib.request, sys, re, json
from json import JSONDecodeError

from googletrans import Translator
from bs4 import BeautifulSoup
# print (sys.argv[0] + ' ' + sys.argv[1] +' ' + sys.argv[2])
translator = Translator()
# print(translator.translate("crvena", dest='en', src='hr'))
# with urllib.request.urlopen(sys.argv[1]) as f:
 #   print(BeautifulSoup(f.read(), 'html.parser').find().text.strip())

if (len(sys.argv) == 4):
    with urllib.request.urlopen(sys.argv[1]) as f:
        textbox = BeautifulSoup(f.read(), 'html.parser').find().text.strip()
        box_new = re.split('[&"+\-_\'*;$=#!?.{}()<>:/\n\r]+', textbox)
        for i in box_new:
            if i != None:
                try:
                    trans_phrase = translator.translate(i, dest=sys.argv[3], src=sys.argv[2])
                    print(trans_phrase.text)
                except JSONDecodeError:
                    continue


elif (len(sys.argv) == 3):
    with urllib.request.urlopen(sys.argv[1]) as f:
        textbox = BeautifulSoup(f.read(), 'html.parser').find().text.strip()
        box_new = re.split('[&"+\-_\'*;$=#!?.{}()<>:/\n\r]+', textbox)
        for i in box_new:
            if i != None:
                try:
                    trans_phrase = translator.translate(i, dest=sys.argv[2])
                    print(trans_phrase.text)
                except JSONDecodeError:
                    continue

else:
    print("Error, improper format. try: [program] [url] [to_language] [from_language]")
    print("or:  [program] [url] [to_language]")

