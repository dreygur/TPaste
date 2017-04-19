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

#xml = XmlDictConfig()

# Parser options...
parser.add_option("-t", "--title", help="Your Paste-name e.g, 'Hello Totul!'", default="Title of paste", action="store")
parser.add_option("-c", "--code", help="Your source-code file name with extension...", default="Hello World!", action="store")
parser.add_option("-f", "--format", help="defines data format e.g, python", default="python", action="store")
parser.add_option("-p", "--privacy", help="Valid options are public, unlisted, private", default="unlisted", action="store")
parser.add_option("-e", "--expiry", help="Valid options are N, 10M, 1H, 1D, 1M ('None', '10 Minutes', '1 Hour', '1 Day', '1 Month'", default="1H", action="store")
parser.add_option("-u", "--udetails", help="User's Paste Details or your profile!", action="store_true")
parser.add_option("--trending", help="All Trending Pastes!", action="store_true")
parser.add_option("--pastes", help="All Pastes by the user!", action="store_true")
parser.add_option("-d", "--delete", help="Delete a paste...", default="None", action="store")
parser.add_option("--pf", help="Shows all valid 'Paste' formats", action="store_true")

# Gathering all parser-options in a variable
(args, _) = parser.parse_args()

# App api and login informations
dev_key = '10077d8a87d91e8542b35339b5d883e8'	# Don't Change this !important
username = ''							# Your username
password = ''							# Your Password

# Generating User-Key
if username and password is not None:
	user_key = api.generate_user_key(dev_key, username, password)
else:
	user_key = None

# Pastes by the user
def user_pastes(up_d, up_u):
	if up_u is not None:
		u_pastes = api.pastes_by_user(up_d, up_u, None)
		print u_pastes
	else:
		print '\nYou are not logged in.\nPlease log-in and try again...'

# Deleting Pastes
def del_paste(dp_d, dp_u, dp_p):
	if dp_u is not None:
		try:
			paste_key = args.delete
			paste_to_delete = api.delete_paste(dp_d, dp_u, dp_p)
			print paste_to_delete
		except:
			pass
	else:
		print '\nYou are not logged in.\nPlease log-in and try again...'

# Trending Posts
if args.trending is True:
	paste_trending = api.trending(dev_key)
	print paste_trending

# User Details... If you want to see the details then simply print it
def user_details(ud_d, ud_u):
	u_details = api.user_details(ud_d, ud_u)
	print '\n'+u_details


# Printing all valid paste formats
if args.pf is True:
	paste_f = list(api.paste_format)
	print '\n'+paste_f

#The main function
def main():
	if args.pastes is True:
		user_pastes(dev_key, user_key)

	if args.udetails is True:
		user_details(dev_key, user_key)

	if args.delete is True:
		del_paste(dev_key, user_key, paste_key)
	
	if args.title is not None:
		# file-open parameters for pasting your desired file
		try:
		    file = open(args.code, "r")
		    code = file.read()
		    file.close()
		    # Sending Data to pastebin.com
		    url = api.paste(
			        api_dev_key = dev_key,
					api_paste_code = code,
					paste_name = args.title,
					api_user_key = user_key, 
			        paste_format = args.format,
					paste_private = args.privacy,
					paste_expire_date = args.expiry)
		    print '\nYour paste link: '+url+'Thanks for using tPaste...' #Prints the paste url
		except:
			pass


if __name__ == "__main__":
	main()
# end..............................................
