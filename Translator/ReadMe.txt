Westley Kirkham


This python 3 program takes the html of a website and filters text out of it. If the text can be translated into another language it does so.

It requires bs4, googletrans, json, sys, urllib.request and webbrowser libraries to run.

The command line inputs supported for this program are of the format:

	python ./translator.py url from_lang to_lang

or

	python ./translator.py url to_lang

If the from_lang isn't specified then the program will attempt to auto-detect the language to be translated from. The from_ and to_lang must be the two letter language codes that the googletrans library accepts. For example, english is en, croatian is hr, and german is de.

If the translation is successful it saves the file to an html in the python projects folder. If the 'filename' variable properly directs to the file location the file is displayed in a web browser. 'username' in the path must be changed to the name of the local user folder.

The larger the website the longer it'll take to translate. There are still some issues with the translation picking up text in certain places. The best translation I got was from professor Regehr's website, though text after :s still wasn't translated. Best to pick one article and translate that. If you visit the main page it will try to translate everything he ever wrote.