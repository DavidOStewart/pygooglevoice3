from distutils.core import setup


README = """Python Google Voice
====================

Joe McCall & Justin Quick

Exposing the Google Voice "API" to the Python language
-------------------------------------------------------

Google Voice for Python Allows you to place calls, send sms, download voicemail, and check the various folders of your Google Voice Accounts.
You can use the Python API or command line script to schedule calls, check for new recieved calls/sms, or even sync your recorded voicemails/calls.  
Works for Python 2.

-------------------------------------------------------

This version has been updated and edited by David Stewart to be compatible with Python 3.4.

Available at: https://github.com/DavidOStewart/pygooglevoice3
"""

setup(
    name = "pygooglevoice3",
    version = '1.0',
    url = 'https://github.com/DavidOStewart/pygooglevoice3',
    author = 'David Stewart',
    author_email='dstewart@cct.lsu.edu',
    description = 'Python 3 Interface for Google Voice',
    long_description = README,
    packages = ['googlevoice'],
    scripts = ['bin/gvoice','bin/asterisk-gvoice-setup', 'bin/gvi']
)