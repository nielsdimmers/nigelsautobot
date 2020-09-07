# What is this?

This is my automated bot to retrieve covid-19 data from the Dutch RIVM and access it through a telegram bot. This is a first start, in the future this will be extended.

# How do I use it

It cannot be used on its own, you need to do the following:

1. In telegram, chat to the @botfather and request a new bot, copy its token
2. Install Python 3 including requirements
3. Create a Mysql database with a user with all rights (excluding GRANT) on that database
4. Checkout the code of this GIT
5. Create a copy of config_original.py to config.py and fill in the values of step (1), and (3)
6. Run createtables.py once
7. Configure to run refreshCovidData.py on a regular basis, usually daily after the information is released
8. Start nigelsautobot.py which is the actual bot