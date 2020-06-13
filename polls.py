#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Quickly collect the RealClearPolitics (RCP) average
from a collection of arbitrary elections.
"""

import json
from rcp import get_poll_data
from jinja2 import Environment, FileSystemLoader


def get_rcp_averages(filename):
    """
    Loads all election data from a JSON file, collects the
    RCP averages, then constructs an HTML file for displaying
    the results on a static website.
    """

    # Load the election data from the JSON file specified
    with open(filename, "r") as handle:
        elections = json.load(handle)

    # Define the base RCP URL to simplify the elections parameter
    base_url = "https://www.realclearpolitics.com/epolls/"

    # Unpack the election data to check each race
    for election in elections.values():
        for place, race in election.items():

            # If the poll is not enabled, do nothing and loop again
            if not race["enable"]:
                continue

            # Get the poll data and extract the first element
            polls = get_poll_data(poll=base_url + race["url"])
            rcp_avg = polls[0]["data"][0]

            # The first element should always be the RCP average. If it isn't,
            # then the RCP average doesn't exist, so don't display anything
            if not rcp_avg["Poll"].startswith("RCP"):
                race["text"] = f"{place}: Did not find RCP average"
                continue

            # The RCP average does exist; find out the candidate's party
            party = get_party(rcp_avg)

            # Update the race dictionary with the text to display
            spread, date = rcp_avg["Spread"], rcp_avg["Date"].replace(" ", "")
            race["text"] = f"{place}: {party} {spread} ({date})"

    # Setup the jinja2 templating environment and render the template
    j2_env = Environment(loader=FileSystemLoader("."), autoescape=True)
    template = j2_env.get_template("index.j2.html")
    html_text = template.render(data=elections)

    # Print the HTML text to stdout for a quick visual check
    print(html_text)


def get_party(rcp_avg):
    """
    Determine the party, such as (R), (D), etc. for the
    candidate currently winning the race.
    """

    # Figure out the winner first
    winner = rcp_avg["Spread"].split(" ")[0]

    # Search for the winner within the rcp_avg dict
    # If found, return the party after the name
    for k in rcp_avg.keys():
        if k.startswith(winner):
            return k.split(" ")[1]

    # Party not found; use a static string instead
    return "(?)"


if __name__ == "__main__":
    get_rcp_averages("elections.json")
