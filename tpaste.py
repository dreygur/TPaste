#!/usr/bin/env python

"""
Copyright (c) 2017 ISTT_Cyborgs (fb.com/istt.cse)
Author: Totul (fb.com/rytotul)
See the file 'doc/COPYING' for copying permission
"""

import sys
from optparse import OptionParser
from pastebin import PastebinAPI

sys.dont_write_bytecode = True

# calling from modules...
parser = OptionParser()
api = PastebinAPI()

# Parser options...
parser.add_option("-t", "--title", dest="p_name", default="Title of paste", help="Your Paste-name e.g, Hello!")
parser.add_option("-c", "--code", dest="p_code", default="Hello World!", help="Your code...")
parser.add_option("-f", "--format", dest="p_format", default="python", help="defines data format e.g, python")
parser.add_option("-p", "--privacy", dest="p_private", default="unlisted", help="Valid options are public, unlisted, private")
parser.add_option("-e", "--expiry", dest="p_expire_date", default="10M", help="Valid options are N, 10M, 1H, 1D, 1M ('None', '10 Minutes', '1 Hour', '1 Day', '1 Month'")
(options, args) = parser.parse_args()

# App api and login informations
dev_key = '10077d8a87d91e8542b35339b5d883e8'	# Don't Change this !important
username = ''							# Your username
password = ''					# Your Password

# file-open parameters for pasting your desired file
file = open(options.p_code, "r")
code = file.read()
file.close()

# Generating User-Key
user_key = api.generate_user_key(dev_key, username, password)

# User Details... If you want to see the details then simply print it
details = api.user_details(dev_key, user_key)

# Sending Data to pastebin.com
url = api.paste(api_dev_key = dev_key,
				api_paste_code = code,
				paste_name = options.p_name,
				api_user_key = user_key, 
				paste_format = options.p_format,
				paste_private = 'unlisted',
				paste_expire_date = options.p_expire_date)

# Printing the pastebin.com url
print url
