# What is this?

This is my automated bot to retrieve covid-19 data from the Dutch RIVM and access it through a telegram bot. This is a first start, in the future this will be extended.

# How do I use it?

It cannot be used on its own, you need to do the following:

1. In telegram, chat to the @botfather and request a new bot, copy its token
2. Install Python 3 including requirements (see below)
3. Create a Mysql database with a user with all rights (excluding GRANT) on that database
4. Checkout the code of this GIT
5. Create a copy of config_original.py to config.py and fill in the values of step (1), and (3)
6. Run createtables.py once
7. Configure to run refreshCovidData.py on a regular basis, usually daily after the information is released
8. Start nigelsautobot.py which is the actual bot

# Requirements
The following python packages are required, some of them are installed by default:
* mysql-connector-python
* datetime
* local
* python-telegram-bot

The requirements can be installed by typing `pip3 install <package name>` into your terminal, after installing pip3

# Feature changes

## Current version: 0.3

* added a separate dbconnector class to separate the database connection from the rest of the code
* added a separate const class to separate constants
* updated text to display a good, human format date including the day of the week, in Dutch locale.
* cast config into a class *note:* this means you need to copy the changes to your own config file for this to work!
* Added requirements to documentation

Still, there's a lot of stuff to do:
* TODO: To have a overall script with commandline arguments, so the application only has to be called from one location
* TODO: Implement (unit) testing

## Version 0.2

First version and start of version log.