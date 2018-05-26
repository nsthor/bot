""" Array Out Of Bounds roles definition

Used in Discord Bot release by IT from Stud-IO
"""
__author__ = 'DABE Christophe'
__copyright__ = 'All rights reserved, Stud-IO 2018'
__server__ = 'ArrayOutOfBound'

# TO SET IN JSON FILE
full_help = "```This is the commands who you are allowed :\n\
    !player         Initialize music player \n\
    !join           Make the bot join your current voice channel\n\
    !help           Get this message\n\
```"

# Defines the roles for the given server
role_tab = {'Dieu': 1, 'Bot': 2, 'Drunk': 2,'Sorcier': 3, 'Robin': 4, 'Moldu': 5, 'ElfeDeMaison': 99}

help_tab = {1: full_help, 2: full_help, 3: full_help, 4:full_help}

# Get the number value for a given name from the role_tab dictionnary
# Return max value if the name is not found
def get_role_number(name):
    if(name in role_tab.keys()):
        return(role_tab[name])
    return 99


# Retrieve the help message for the given rank
# Return "Nothing" for other roles
def get_help_message(rank):
    if(rank in help_tab.keys()):
        return(help_tab[rank])
    return("Nothing")
