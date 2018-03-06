'''
Hustle is a web crawler intended to extract scheduling data from the website of a local indoor soccer facility.
'''
from datetime import datetime
from bs4 import BeautifulSoup
from sys import argv
import mechanize
import re

def search(team):
    """Searches for a team and returns its web page."""
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open("http://www.letsplaysoccer.com/facilities/16/teams")
    for link in br.links():
        if link.text.lower() == team.lower():
            return br.follow_link(link)
    return None

def parse(response, team):
    """ Returns a list of dictionaries where each dictionary represents a scheduled game.

    Arguments:
    response -- the browser response object for the team's web page
    team -- the name of the team in question, as given on the commandline
    """
    # First table = schedule; second table = standings
    rows = BeautifulSoup(response.read(), "html5lib").find_all("table")[0].find_all("tr")
    keys = ["Time", "", "", "Opponent", "Result"] # Ignore columns 1 and 2
    result = []
    for row in range(1, len(rows)): # Ignore table headers at row 0
        columns = rows[row].find_all("td")
        game = {}
        for column in range(0, len(columns)):
            if column == 1 or column == 2:
                continue # Ignore field no. and home team
            cell = columns[column]
            # Each cell contains either an anchor tag or plain text. Those with anchor tags are in column 0 ("Time") and column 3 ("Opponent"). The only non-ignored column with plain text is column 4 ("Result"). However, column 4 may not contain content if the game has not yet been played.
            if len(cell.find_all("a")) == 0:
                if re.match("\s[0-9]+", cell.text):
                    # columns[column - 2] = home team column
                    val = find_winner(cell, team, columns[column - 2])
                else:
                    val = "" # Game has not been played
            elif cell.a.text.lower() == team.lower():
                # This script assumes the visitor team to be the opponent. In order to extract the correct opponent, if the visitor is team then the opponent is found in the home team column.
                val = columns[column - 1].a.text
            else:
                val = cell.a.text
            game[keys[column]] = val # Each cell is added to a single game.
        result.append(game) # Each row represents a game.
    return result

def find_winner(cell, team, home):
    """Returns whether the match result was a win or loss."""
    lhs = int(cell.text[1:cell.text.index("-") - 1])
    rhs = int(cell.text[cell.text.index("-") + 1:])
    # The left-hand score pertains to the home team. Determine whether the winning score matches to the team in question.
    if (lhs > rhs and home.a.text.lower() == team.lower()) or (lhs < rhs and not (home.a.text.lower() == team.lower())):
        result = str(lhs) + "-" + str(rhs) + " W"
    else:
        result = str(lhs) + "-" + str(rhs) + " L"
    return result

def get_option(arg):
    """Returns the requested function"""
    options = {
        "d": default,
        "o": opponent,
        "f": full
    }
    return options[arg]

def next(game):
    # TODO: Return only the next game
    return

def compare(teams):
    # TODO: Find scheduling conflicts for an array of teams
    return

def default(game):
    return game["Time"]

def opponent(game):
    return game["Time"] + (" " * 3) + game["Opponent"]

def full(game):
    """Returns the full schedule including each game's result"""
    max_len = 15 # Max length of team name when printed
    pad = 3 # Space between each column of printed data
    opponent = game["Opponent"]
    return game["Time"] + (" " * pad) + opponent + (" " * (max_len - len(opponent) + pad)) + game["Result"]

def write(data, arg):
    """Writes the data to standard output with the specified options"""
    now = datetime.now()
    flag = False
    for game in data:
        gametime = datetime.strptime(game["Time"], '%a %m-%d-%y %I:%M %p')
        if flag == False and now < gametime:
            # ANSI encoding shows next game in green
            result = "\033[38;5;10m" + get_option(arg)(game) + "\033[0m"
            flag = True
        else:
            result = get_option(arg)(game)
        print result

def main():
    '''
    Searches for and navigates to the web page containing scheduling info for the team specified in argv[1]. If the page is not found, prints an error message. Prints the schedule as specified by argv[2].
    '''
    result = search(argv[1]) # Result = browser response object
    if result == None:
        print "Team not found"
        return
    if len(argv) == 2:
        arg = "d" # Default option
    else:
        arg = argv[2] # User-specified scheduling data
    write(parse(result, argv[1]), arg)

if __name__ == '__main__':
    main()
