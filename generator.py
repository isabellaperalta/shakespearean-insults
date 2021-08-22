import sys
import random
from time import sleep

adjective1 = ["ugly", "venomous", "poisonous", "foolish", "cowardly", "haggard", "disloyal", "hideous", "terrible", "unsightly", "revolting", "repellent", "repulsive", "repugnant", "grotesque", "disgusting", "monstrous", "reptilian", "disfigured"]
adjective2 = ["foul", "corrupted", "pigeon-livered", "sodden-witted", "loathesome", "false", "ghastly", "unbecoming", "frightful", "vile", "misshapen", "despicable", "horrible", "spiteful", "sinister", "dishonourable", "obnoxious", "rotten", "vicious"]
noun = ["flesh-monger", "lump of foul deformity", "toad", "worm", "boil", "plague", "harpy", "lout", "maggot-pie", "foot-licker", "strumpet", "measle", "codpiece", "barnacle", "sore", "miscreant", "bladder", "ratsbane", "malt-worm"]

while True:
    print "Thou %s" % (random.choice(adjective1)) + " %s" % (random.choice(adjective2)) + " %s!" % (random.choice(noun))
    sleep (3)
