
import random
import json
from generators.Generator import Generator
from generators.NPC import  NPC

class Business(Generator):
    """ Create a business."""
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)

        self.generate_features(self.kind)
        self.senses=[]

        #originally I was going to move these to a for loop, but the verb
        # doesn't match the variable name, so it would require refactoring
        # of the dataset and every other damn thing. Meh.
        if hasattr(self,  'smell'):
            self.smell='you smell '+self.smell
            self.senses.append(self.smell)
        if hasattr(self,  'sound'):
            self.sound='you hear '+self.sound
            self.senses.append(self.sound)
        if hasattr(self,  'sight'):
            self.sight='you see '+self.sight
            self.senses.append(self.sight)

        if not hasattr(self,  'owner'):
            self.owner=NPC(redis)

        #TODO patrons should be better calculated
        if not hasattr(self,  'patroncount'):
            self.patroncount=random.randint(1,10);

        # Business is one of the few classes where trailer doesn't start as part of the name
        # So we have to add it here.
        if hasattr(self,  'trailer'):
            self.name['trailer']=self.trailer
            self.name['full']=self.name['full'] +' '+self.trailer.title() 

        # If maxfloors isn'd designated, set it to 1
        if not hasattr(self,  'maxfloors'):
            self.maxfloors=1

        #don't set floors if it already exists
        if not hasattr(self,  'floor'):
            self.floor= random.randint(1,int(self.maxfloors))


