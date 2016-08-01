from django.db import models

"""
The Game model will contain basic information about the game, title, a list 
of applicable genres, year released and metacritic score.
"""

class Game:
	name = models.charField(max_length=100)
	    

"""
The Genre model will contain basic information about different genres. The name
of that genre, the list of other genres that have been linked to it and the

"""

class Genre:

"""
The Taste vector contains the values of a user's quantified tastes. Also performs arithmetic between taste 
vectors to find close vectors.

"""


class TasteVector:
