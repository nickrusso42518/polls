#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Collect national and state level polling for US
presidential elections.
"""

from core import get_rcp_averages

elections = [
    ("US", "/president/us/general_election_trump_vs_biden-6247.html"),
    ("AZ", "/president/az/arizona_trump_vs_biden-6807.html"),
    ("FL", "/president/fl/florida_trump_vs_biden-6841.html"),
    ("IA", "/president/ia/iowa_trump_vs_biden-6787.html"),
    ("MI", "/president/mi/michigan_trump_vs_biden-6761.html"),
    ("MN", "/president/mn/minnesota_trump_vs_biden-6966.html"),
    ("NC", "/president/nc/north_carolina_trump_vs_biden-6744.html"),
    ("NH", "/president/nh/new_hampshire_trump_vs_biden-6779.html"),
    ("NV", "/president/nv/nevada_trump_vs_biden-6867.html"),
    ("OH", "/president/oh/ohio_trump_vs_biden-6765.html"),
    ("PA", "/president/pa/pennsylvania_trump_vs_biden-6861.html"),
    ("TX", "/president/tx/texas_trump_vs_biden-6818.html"),
    ("VA", "/president/va/virginia_trump_vs_biden-6988.html"),
    ("WI", "/president/wi/wisconsin_trump_vs_biden-6849.html"),
]
get_rcp_averages(elections)
