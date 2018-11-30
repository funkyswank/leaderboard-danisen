# leaderboard-danisen
This is a barebones Danisen format leaderboard, designed to be run through Heroku. I don't fully understand why, but despite my set-up being done with the default SQLite database, it works directly with Heroku after linking a Heroku PostgreSQL to it via some bash commands. 
The Danisen format is based on Japanese Gamespot Versus stuff, where players gain points for winning, lose points for losing, and their rank is determined by said points.
There are four "models" or tables in the structure as it currently exists. 
Fighters, for the character a player chooses to use.
Players, as in the competitors themselves.
Ranks, as in the structure of the leaderboard.
Matchlog, as in each individual battle played between two players.

Ranks require a +/- threshold to say, when a Player reaches + points they move up a rank and reset points to 0, or - points they are demoted and reset points to 0.
Fighters could be literally anything; if you like Soul Calibur, use Soul Calibur characters. These do not show up on the Admin page, and will be entered just from direct database access.
Pretty much all data will be entered by an admin on the admin page. That admin is added through direct database access. 
Once Fighters, Ranks, and Players are set up (in that order), the only thing that needs to be added are matches as they occur. Player rank and points will automatically update once winner/loser are saved to the database, though any mistakes can certainly be rolled back via manual editing.

This should also work if run locally  (manage python.py runserver). 
