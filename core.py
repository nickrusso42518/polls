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
        if rcp_avg["Poll"].startswith("RCP"):
            print(f"{place}: {rcp_avg['Spread']} ({rcp_avg['Date']})")
        else:
            print(f"{place}: Did not find RCP average")
