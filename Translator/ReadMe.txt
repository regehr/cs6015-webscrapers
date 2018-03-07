Westley Kirkham


This program takes the html of a website and filters text out of it. If the text can be translated into another language it does so.

It requires bs4, googletrans, and json libraries to run.

The command line inputs supported for this program are of the format:

	python ./translator.py url from_lang to_lang

or

	python ./translator.py url to_lang

If the from_lang isn't specified then the program will attempt to auto-detect the language to be translated from. The from_ and to_lang must be the two letter language codes that the googletrans library accepts. For example, english is en, croatian is hr, and german is de.