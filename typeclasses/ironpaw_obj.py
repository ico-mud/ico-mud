# end of file mygame/typeclasses/objects.py
from evennia import DefaultObject
 
class Static_object(DefaultObject):
  "Static Object"
  def at_object_creation(self):
    "Called whenever a new object is created"
    # lock the object down by default
    self.locks.add("get:false()")
    # the default "get" command looks for this Attribute in order
    # to return a customized error message (we just happen to know
    # this, you'd have to look at the code of the 'get' command to
    # find out).
    self.db.get_err_msg = "Seriously? You want to pick up THAT?"
    self.locks.add("edit:false(Player)")
pass

class Light_object(DefaultObject):
       "Light Object"
       def at_object_creation(self):
                 "Called whenever a new object is created"
          # lock the object down by default
pass

class Furniture(DefaultObject):
       "Furniture"
       def at_object_creation(self):
           "Called whenever a new object is created"
           self.db.weight =0
           self.db.desc = ""
           self.db.value = 0
           # lock the object down by default
           self.locks.add("edit:false(Player)")
pass