#!/usr/bin/env python

"""
Author: Nick Russo (njrusmc@gmail.com)
Purpose: Collect US senate polling in battleground states.
"""

from core import get_rcp_averages

elections = [
    ("AZ", "/senate/az/arizona_senate_mcsally_vs_kelly-6801.html"),
    ("CO", "/senate/co/colorado_senate_gardner_vs_hickenlooper-6945.html"),
    ("ME", "/senate/me/maine_senate_collins_vs_gideon-6928.html"),
    ("MI", "/senate/mi/michigan_senate_james_vs_peters-6964.html"),
    # ("MT", "/senate/mt/montana_senate_daines_vs_bullock-7063.html"),
    ("NC", "/senate/nc/north_carolina_senate_tillis_vs_cunningham-6908.html"),
]
get_rcp_averages(elections)
