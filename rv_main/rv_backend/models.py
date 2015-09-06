from django.db import models
from django.contrib.auth.models import User

"""
The Map model contains all the information about the relations between the games
that you have added to it. It also contains the user associated with it. It also keeps an array of changes to it that are pending user approval. Keeps an array of games and personal ratings of those games as well. 
"""
class Map(models.Model):
   #Placeholder to prevent interpretation error
   pass 

"""
Initializer for Friendlist objects. create_Friendlist takes a User, a boolean
stating whether the list is private or not and the user's steamID
"""
class FriendlistManager(models.Manager):
   def create_Friendlist(self, user, private, steamID):
      Friendlist = self.create(user=user, private=private, steamID=steamID)
      
      return Friendlist



"""
The Friendlist model has an associated user, a set of friends, a boolean stating
whether the Friendlist is private, which defaults to false. There is a set of 
pendingFriends which are all the users who have friend requested you, there is
also an associated steamID for looking up games to add to the Map. 
"""

class Friendlist(models.Model):
   
   #Change to owner
   user = models.ForeignKey(User, related_name="friendlist_set")
   friends = models.ManyToManyField(User, related_name="friends_set")
   private = models.BooleanField(default=False)
   pendingFriends = models.ManyToManyField(User, related_name="pendingFriends_set")
   steamID = models.CharField(max_length=30)
   objects = FriendlistManager()
    
   def __unicode__(self):
      return self.user.username


"""
The Game model holds a title as well as an associated game id number. It also holds an array of ratings that are based on different metrics and how it holds to different genres.
"""
class Game(models.Model):
   #Placeholder to prevent interpretation error
   pass
