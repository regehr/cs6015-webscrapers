# By: Junchen Zhang

import urllib


def main(team):
    url = "https://www.cbssports.com"

    page = str(urllib.urlopen(url + "/nba/teams/schedule/CLE/cleveland-cavaliers").read())

    team_start = page.find("/option")

    team = page.find(team, team_start, page.find("/select", team_start))

    if team == -1:
        print("wrong name")
        return

    team_start = page.find("/nba", team - 80)
    team_end = page.find(">", team_start) - 1
    url += page[team_start: team_end]

    page = str(urllib.urlopen(url).read())

    time = page.find("PM<") - 625
    time_start = page.find(">", time) + 1
    time_end = page.find("<", time_start)
    time = page[time_start: time_end]
    print("\nLast game:\n" + "Date:     " + time)

    opponent = page.find("page/", time_end) + 5
    opponent_start = page.find("/", opponent) + 1
    opponent_end = page.find(">", opponent_start) - 1
    opponents = page[opponent_start: opponent_end].split("-")
    opponent = ""
    for data in opponents:
        opponent += data.capitalize() + " "
    print("Opponent: " + opponent)

    result = page.find("recap", opponent_end)
    result_start = page.find(">", result) + 1
    result_end = page.find("<", result_start)
    result = page[result_start: result_end]
    print("Result:   " + result)

    time = page.find("scoreboard", result_end)
    time_start = page.find(">", time) + 1
    time_end = page.find("<", time_start)
    time = page[time_start: time_end]
    opponent = page.find("page/", time_end) + 5

    time_start = page.find("PM", team_end) - 10
    time_start = page.find(">", time_start) + 1
    time_end = page.find("<", time_start)
    time += ", " + page[time_start: time_end]
    print("\nNext game:\n" + "Time:     " + time)

    opponent_start = page.find("/", opponent) + 1
    opponent_end = page.find(">", opponent_start) - 1
    opponents = page[opponent_start: opponent_end].split("-")
    opponent = ""
    for data in opponents:
        opponent += data.capitalize() + " "
    print("Opponent: " + opponent + "\n")


team_name = raw_input("Please enter an NBA team: ")
main(team_name.split(" ")[0])
