# RNGArenaPython

The RNGArena iOS game by Hezekiah Valdez, David Pham, Geoffery Cheung, and Prem Panchal converted to Python for the Artificial 
Intelligence Class

Game Idea:
The player is going to try to defeat as many enemies as possible to achieve the high score. The player will utilize a randomly 
distributed four abilities. The opponenets will be of random level, have random abilities, and always choose random abilities 
to use against the player.

Gameplay:

1. The player starts with one skill randomly chosen for them at the start of the game
2. When the game starts the AI opponent will always go first and use a skill against the player character. This is to prevent a possible infinite game length)
3. When an opponent is defeated the player will be awarded one point.
4. If and when the opponent is defeated the player will be awarded one of four things. A heal of 20HP or one of three abilities from a randomly generated set of three.
5. The game will continue until the player's HP hits zero. 
6. Once the game is concluded the player's score should be recorded in a highscore counter. The player should also be given the option to restart the game.
