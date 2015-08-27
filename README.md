#Replay value

In order to start developing Replay Value first pull the repo as follows

git pull origin master

Next you'll need to install the virtual environment that will make it possible to run django. virtualenv is already installed server wide, so just:

virtualenv env

will start up your env folder, then to use it run

source env/bin/activate

Finally all from this same directory run

pip install -r requirements.txt

And you will have the environment required to run the replayvalue server.

#Starting up a server

In order to start up a server just run the following from the top level of the django project:(Should be usr/replayvalue/replayvalue/)

python manage.py runserver 0:9001    (could be any number greater than 9000 and less than 10000)

Finally you should be able to see the results of your server running on the web at www.replayvalue.net:9001 or whatever number you're using.

So now you should be able to see how doing different things affects django and be able to start writing code. 
