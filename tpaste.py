#!/usr/bin/env python

"""
Copyright (c) 2017 ISTT_Cyborgs (fb.com/groups/istt.cse.2017)
Author: Rakibul Yeasin Totul (fb.com/rytotul)
See the file 'doc/COPYING' for copying permission
"""

# importing modules
import sys
sys.dont_write_bytecode = True

from optparse import OptionParser
from lib.pastebin import PastebinAPI

# calling from modules...
parser = OptionParser()
api = PastebinAPI()

# Parser options...
parser.add_option("-t", "--title", action="store", dest="p_name", default="Title of paste", help="Your Paste-name e.g, 'Hello Totul!'")
parser.add_option("-c", "--code", action="store", dest="p_code", default="Hello World!", help="Your source-code file name with extension...")
parser.add_option("-f", "--format", action="store_true", dest="p_format", default="python", help="defines data format e.g, python")
parser.add_option("-p", "--privacy", action="store_true", dest="p_private", default="unlisted", help="Valid options are public, unlisted, private")
parser.add_option("-e", "--expiry", action="store_true", dest="p_expire_date", default="1H", help="Valid options are N, 10M, 1H, 1D, 1M ('None', '10 Minutes', '1 Hour', '1 Day', '1 Month'")
parser.add_option("--ud", "--details", action="store_true", dest="u_details", default="u_details", help="User's Paste Details or your profile!")
parser.add_option("--trending", action="store_true", dest="p_trending", default="p_trending", help="All Trending Pastes!")
parser.add_option("--pastes", action="store_true", dest="my_paste", default="my_paste", help="All Pastes by the user!")
parser.add_option("-d", "--delete", action="store_true", dest="d_paste", default="d_paste", help="Delete a paste...")
parser.add_option("--pf", action="store_true", dest="p_f", default="p_f", help="Shows all valid 'Paste' formats")

# Gathering all parser-options in a variable
(options, args) = parser.parse_args()

# App api and login informations
dev_key = '10077d8a87d91e8542b35339b5d883e8'	# Don't Change this !important
username = 'mdazharulcu'							# Your username
password = '01792261115'							# Your Password

# Generating User-Key
user_key = api.generate_user_key(dev_key, username, password)

# Pastes by the user
if options.my_paste == True:
	u_pastes = api.pastes_by_user(dev_key, user_key, results_limit=None)
	print u_pastes

# Deleting Pastes
if options.d_paste == True:
	paste_key = api.api_paste_key(d_paste)
	d_paste = api.delete_paste(dev_key, user_key, paste_key)
	print d_paste

# Trending Posts
if options.p_trending == True:
	paste_trending = api.trending(dev_key)
	print paste_trending

# User Details... If you want to see the details then simply print it
if options.u_details == True:
	details = api.user_details(dev_key, user_key)
	print details

# Printing all valid paste formats
if options.p_f == True:
	paste_f = list(api.paste_format)
	print paste_f

# file-open parameters for pasting your desired file
try:
        file = open(options.p_code, "r")
        code = file.read()
        file.close()
        # Sending Data to pastebin.com
        url = api.paste(api_dev_key = dev_key,
				api_paste_code = code,
				paste_name = options.p_name,
				api_user_key = user_key, 
        			paste_format = options.p_format,
				paste_private = 'unlisted',
				paste_expire_date = options.p_expire_date)
        print url # Printing the pastebin.com url
except:
        pass

# end..............................................
