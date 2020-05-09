#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Collect various polls regarding US Govt approval and other
national issues.
"""

from core import get_rcp_averages

elections = [
    ("Presidential approval ", "other/president_trump_job_approval-6179.html"),
    ("Congressional approval", "other/congressional_job_approval-903.html"),
    ("Generic congressional ", "other/2020_generic_congressional_vote-6722.html"),
    ("Direction of country  ", "other/direction_of_country-902.html"),
]
get_rcp_averages(elections, year="")
