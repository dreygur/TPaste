============
Pastebin App
============
About
-----

The package allows you to communicate directly with Pastebin.com from your Python application, either logged in or anonymously. This can be handy 

for a number of reasons - dumping error logs before an abort, regular web based status updates, but can't be bothered getting a web-server running etc.

It allows you to do everything the API allows, which is:

- Paste, either logged in or anonymously
- 200+ selectable languages for syntax highlighting
- Set expiry times on pastes
- Set public/private/unlisted status for pastes
- See trending pastes
- See pastes by a particular user
- Delete your pastes
- Retrieve your user details
- Generate a session (user) key for added security
- Paste using the old, non-token anonymous API (for as long as they keep it open)




Installation
------------
You should have the Pastebin module Developed by Ian Havelock
Download from: https://github.com/rytotul/Pastebin

If you have downloaded the source distribution, to install do the following at the commandline: 

::
   
   $ python setup.py install


If you can use and install Python Egg's, you can do:

::

   $ easy_install TPaste


And it will download the latest version from the Python Package Index.
