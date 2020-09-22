# Table of contents

* [What is this?](#whatsthis)
* [How do I use it?](#usage)
* [Requirements](#requirements)
* [Feature changes](#versionlog)

# <a name="whatsthis"></a> What is this?

This is my automated bot to retrieve covid-19 data from the Dutch RIVM and access it through a telegram bot. This is a first start, in the future this will be extended. This project is mainly to challenge my own personal technical skills and meanwhile make something informational / useful.

# <a name="usage"></a> How do I use it?

It cannot be used on its own, you need to do the following:

1. In telegram, chat to the @botfather and request a new bot, copy its token
2. Install Python 3 including requirements (see below)
3. Create a Mysql database with a user with all rights (excluding GRANT) on that database
4. Checkout the code of this GIT
5. Create a copy of config_original.py to config.py and fill in the values of step (1), and (3)
6. Run createtables.py once
7. Configure to run refreshCovidData.py on a regular basis, usually daily after the information is released
8. Configure to run logTemperature.py regularly as well, usually every 15 minutes.
9. Start nigelsautobot.py which is the actual bot

# <a name="requirements"></a>Requirements
The following python packages are required, some of them are installed by default:
* `mysql-connector-python`
* `datetime`
* `local`
* `python-telegram-bot`
* `logging`
* `matplotlib`

The requirements can be installed by typing `pip3 install <package name>` into your terminal, after installing pip3

# <a name="versionlog"></a>Feature changes

## Still to do

* TODO: Markdown enabeling for temperature message
* TODO: Implement (unit) testing
* TODO: Find an additional use for this bot, maybe with temperature sensors
* TODO: Refactor the graph creation out of logTemperature and refreshCovidData
* TODO: See if you can refactor dbconnector, it's starting to get quite complicated and long
* TODO: Add access log: who executed which command?

NOTE: Just that it's in this todo list, doesn't mean it's going to be in the next version.

## Current version: 0.10

NOTE: Upgrading from before this version to this version or later? You need another column in your temperature table. Execute the following SQL to add it: 

`ALTER TABLE ``temperatureLog`` ADD COLUMN alerttext TEXT AFTER temperature`

For new systems, this column is added to the table when executing the createtables script.

* (bugfix): switched axis labels for covid graphs
* Added min/max temperature and times to the temperature message
* Added alert logging and showing of text when there's a weather alert

## Version 0.9

* Add /help command to display which commands are available
* (bugfix): switched axes labels in temp graph
* Added two graphs to the /covid command: hospitalisations and deceased, including data in the database for that

## Version 0.8.1

* Fixed temperature graph order and time/date display now actually uses const.

## Version 0.8

* Fixed version number and missing information in the configuration file
* Added temperature graph over period of time

## Version 0.7

This version requires some new config information and a re-run of createtables.py. Also, setup to run logTemperature about every 15 minutes.

* Set up and implemented first unit tests (refreshCovidData and covid handler).
* Added the command '/temp' to the bot to return temperature information, which should be updated regularly by the logTemperature .

## Version 0.6

* Fixed the reply stuf, now it doesn't quote anymore in groups
* Added a lot of settings to enable testing, like a default testfile instead of reading in the data and printing messages instead of starting the bot
* moved a lot of the covid code to a separate covid handler
* added commandline functionality for '--test' command

## Version 0.5.1

* Fix a but with today's results not being available throwing an exception

## Version 0.5

* Added functionality to create a graph and send it over telegram

## Version 0.4

* Locales are a pain in the dark place, so moved it to the config. You can pick your own poison now.
* Use the telegram bot context, so that it is future proof (honestly, I just got annoyed by the error messages)
* Added loads of inline comments (I needed a reason to touch every file again)
* Added /version command, call it and it returns the application version number
* Added some basic (info and debug) logging to some modules.
* Added TOC to README
* Minor makeup changes in README

## Version 0.3

* added a separate dbconnector class to separate the database connection from the rest of the code
* added a separate const class to separate constants
* updated text to display a good, human format date including the day of the week, in Dutch locale.
* cast config into a class *note:* this means you need to copy the changes to your own config file for this to work!
* Added requirements to documentation

## Version 0.2

First version and start of version log.