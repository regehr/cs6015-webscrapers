"""
For lack of a better assignment idea, I planned on scraping some SpaceX data, to help
setup a calendar event or email/text about the status of the next launch. As a kid, i
used to love watching the launches from Vandenburg AFB, the majority of which are now
by SpaceX.

While SpaceX has an idosyncratic (to be polite) CEO in Musk, it is still thrilling to
watch their exploits in the pursuit of manned space exploration. They are far from
shy about their activities and have a very active social media presence with multiple
channels to subscribe to.

However, I still hate waking up at 6 am to watch a launch, only to find it was actually
pushed back the evening prior and I simply didn't know about it. Or missing one completely
because I do not allow youtube or twitter to alert me directly about anything.

Luckily, someone already built a nice rest-api to access SpaceX data (unaffiliated),
which I have used to provide the user with several options from the CLI. They did a
really nice job, the JSON object returned is better than I could have come up with.

So this is less a scraper and more of an exploration of someone else's data collection
efforts. I learned a lot. Hopefully my implementation of the weather scraper counts for
the form submission requirement for this assignment.

"""

import sys
import requests
import dateutil
import arrow
from apscheduler.schedulers.blocking import BlockingScheduler

debug = False

# setup and argument parsing/validation
scheduler = BlockingScheduler()
command = ''
phone_number = 8058675309

if debug:
    command = "last"
    phone_number = 8012346640

else:
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if sys.argv[1] is "next" or sys.argv[1] is "last":
            command = sys.argv[1]
            if len(sys.argv) > 2:
                phone_number = sys.argv[2]
    else:
        print("INVALID INPUT. Please enter the launch you are interested in.\n"
              "'>> spaceX.py next' will give you current information on the next launch.\n"
              "'>> spaceX.py last' will give you current information on the most recent launch\n"
              "'>> spaceX.py next 8058675309' will give you information on the next launch and setup SMS status alerts")
        quit()


# main script behaviors,
def create_message(_command):
    url = ""
    tense = ""

    if command is "last":
        url = 'https://api.spacexdata.com/v2/launches/latest'
        tense = " payload, was successfully launched "
    elif command is "next":
        url = 'https://api.spacexdata.com/v2/launches/upcoming'
        tense = " payload, is scheduled for launch "

    response = requests.get(url)
    launch = response.json()

    arrow_time = arrow.get(launch["launch_date_local"])

    # helpful for debugging
    # print(json.dumps(launch, indent=4))

    _message = "Flight " + str(launch['flight_number']) + ", a " + str(launch['rocket']['rocket_name']) + \
               " with the " + launch['rocket']['second_stage']['payloads'][0]['payload_id'] + \
               tense + "on " + str(arrow_time)

    return _message


print(create_message(command))
