#!/usr/bin/python
#####################################################################
# This script presents how use most basic features of the framework.
# It configures the engine, and makes agent perfrom random actions.
# It also gets current state and reward earned with the action.
# <episodes> number of episodes are played. 
# Random combination of buttons is chosen for every action.
# Game variables from state and last reward are printed.
# To see the scenario description go to "../../scenarios/README"
# 
#####################################################################
from __future__ import print_function
from vizia import DoomGame
from vizia import Button
from vizia import GameVariable
from vizia import ScreenFormat
from vizia import ScreenResolution
# Or just use from vizia import *

from random import choice
from time import sleep
from time import time


# Create DoomGame instance. It will run the game and communicate with you.
game = DoomGame()

# Now it's time for configuration!
# load_file could be used to load configuration instead of doing it here with code.
# If load_file is used in-code configuration will work. Note that the most recent changes will add to previous ones.

# Sets path to zdoom engine executive which will be spawned as a separate process. Default is just the same.
game.set_doom_engine_path("./viziazdoom")

# Sets path to doom2 iwad resource file which contains the actual doom game. Default is "./doom2.wad".
game.set_doom_doom_game_path("../../scenarios/doom2.wad")

# Sets path to additional resources iwad file which is basically your scenario iwad.
# If not specified default doom2 maps will be used and it's pretty much useles... unless you want to play doom.
game.set_doom_scenario_path("../../scenarios/basic.wad")

# Sets resolution. Default is 320X240
game.set_screen_resolution(ScreenResolution.RES_640X480)

# Adds buttons that will be allowed. 
game.add_available_button(Button.MOVE_LEFT)
game.add_available_button(Button.MOVE_RIGHT)
game.add_available_button(Button.ATTACK)

# Adds game variables that will be included in state.
game.add_available_game_variable(GameVariable.AMMO1)

# Causes episodes to finish after 200 tics (actions)
game.set_episode_timeout(200)

# Makes episodes start after 10 tics (~after producing the weapon)
game.set_episode_start_time(10)

# Makes the window appear (turned on by default)
game.set_window_visible(True)

# Sets the screen buffer format. Not used here but now you now that you can change it.
game.set_screen_format(ScreenFormat.RGB24)

# Initialize the game. Further configuration won't take any effect from now on.
game.init()


# Define some actions. Each list entry corresponds to declared buttons:
# MOVE_LEFT, MOVE_RIGHT, ATTACK
# 5 more combinations are naturally possible but only 3 are included for transparency when watching.	
actions = [[True,False,False],[False,True,False],[False,False,True]]

# Run this many episodes

episodes = 10

# Sets time that will pause the engine after each action.
# Without this everything would go too fast for you to keep track of what's happening.
# 0.05 is quite arbitrary, nice to watch with my hardware setup. 
sleep_time = 0.028

for i in range(episodes):
	print("Episode #" + str(i+1))

	# Starts a new episode. It is not neaded right after init() but it doesn't cost much. At least the loop is nicer.
	game.new_episode()

	while not game.is_episode_finished():
		
		# Gets the state (copy so you can break it)
		s = game.get_state()

		# Makes a random action and get remember reward.
		r = game.make_action(choice(actions))

		# Prints state's game variables. Printing the image is quite pointless.
		print("State #" + str(s.number))
		print("Game variables:", s.game_variables[0])
		print("Reward:", r)
		print("=====================")

		if sleep_time>0:
			sleep(sleep_time)

	# Check how the episode went.
	print("Episode finished.")
	print("Summary reward:", game.get_summary_reward())
	print("************************")


# It will be done automatically anyway but sometimes you need to do it in the middle of the program...
game.close()


    
