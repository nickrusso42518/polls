#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Quickly collect the RealClearPolitics (RCP) average
from a collection of arbitrary elections.
"""

from rcp import get_poll_data


def get_rcp_averages(elections, year=2020):
    """
    Collects the poll data from a list of elections, each of which is a
    2- tuple. The first part is a place/identifier and the second is the
    poll URL. The year argument is optional and defaults to 2020.
    """

    # Define the base RCP URL to simplify the elections parameter
    base_url = f"https://www.realclearpolitics.com/epolls/{year}"

    # For each election, get the poll data and extract the first element
    for place, url in elections:
        polls = get_poll_data(poll=base_url + url)
        rcp_avg = polls[0]["data"][0]

        # The first element should always be the RCP average. If it isn't,
        # then the RCP average doesn't exist, so don't display anything
        if not rcp_avg["Poll"].startswith("RCP"):
            print(f"{place}: Did not find RCP average")
            continue

        # The RCP average does exist; find out the candidate's party
        winner = rcp_avg["Spread"].split(" ")[0]
        for k in rcp_avg.keys():
            if k.startswith(winner):
                party = k.split(" ")[1]
                break
        else:
            party = "(?)"

        # Print summary of poll with party, winner/spread, and date range
        print(f"{place}: {party} {rcp_avg['Spread']} from {rcp_avg['Date']}")
