# Pastebin App
[![Build Status](https://travis-ci.org/rytotul/TPaste.svg?branch=master)](https://travis-ci.org/rytotul/TPaste)

## About
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

## Installation

Just clone the git and use as you wish:
``` bash
$ git clone https://github.com/rytotul/TPaste.git
```

Thats it.
You can help me to improve it by submitting an issue or commiting the changes. 

## Acknowledgements
- [Ian Havelock](https://github.com/Morrolan) _(For Pastebin API)_
