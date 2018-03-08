# Humanity Scraper

This is a simple web scraper written in Python 3 that accesses a specific
work scheduling website (i.e., https://www.humanity.com) and retrieves the employee work schedule
based on specified command line arguments.
It automates the site login process, using Selenium WebDriver for Google Chrome,
then parses html of the site pages for schedule data.

###Supported Schedule Criteria:
- Retrieve a single employee’s next upcoming shift or upcoming shift schedule (‘daily’ or ‘weekly’ view)
- Retrieve a schedule overview for all employees (‘daily’, ‘weekly’, or ‘monthly’ view)
