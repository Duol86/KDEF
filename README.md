# KDEF
KDEF is a dictionary Discord bot made for a constructed language called 'Kygish' but, with a little editing of the code, it could be used for any language.

Originally, KDEF was created using Discord.py version 1.0, but the changes made to the project to introduce slash commands have forced KDEF to migrate to using Pycord, instead.

Special thanks to the creator of Pycord and of Discord.py for making this project possible.

Included, is a `kygish.db` file with a large chunk of the current words in the official bot (1004 words as of writing)

**Before running, make sure to run either setup.py or setup.sql to set up the database for use with KDEF**

# Dependencies
  - Pycord v2.0.1
  - HJSON
  - Simple-chalk
  
  (the above three are python modules and can be installed via `setup.py`)
  
  - Python 3.3.0 or above
  - Discord bot **with message content intents**, can be created at https://discord.com/developers/applications/
