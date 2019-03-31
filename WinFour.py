class Person():
    def __init__(self, name):
        self.name = name

class Room():
    rooms = {"LIVING ROOM":"A formal sitting room in a residential house for relaxing "\
            "and entertaining guests. It typically consists of a sofa, fancy chairs and "\
            "occasional table.",
            "DINING ROOM":"A room for consuming food. It's usually adjacent to the kitchen and "\
            "has a large dining table and dining chairs.",
            "BEDROOM":"A room in a house where people sleep. It consists of at least one bed, "\
            "night stand and a dreser.",
            "BATHROOM":"A room in the home for personal hygiene activities and generally contains "\
            "shower, face basin and a stall."}
    
    def __init__(self, rm, name):
        self.room = rm
        self.name = name

    def choose_room(self):
        for room_key in self.rooms:
            if self.room in self.rooms:
                print("Well done {}, you choose the {}!\n".format(self.name, self.room))
                print("A {} is: {}".format(self.room, self.rooms[self.room]))
                break
        else:
            print("Sorry, your room choice does not exist!")
                  
class Game():
    def __init__(self):
        pass

    def begin(self):
        name = input("What is your name?\n")
        person = Person(name)
        print("Welcome to the game, {}!".format(person.name))
              
        while True:
              desired_room = input("Please enter a room to go to, or 'q' to quit game.\n")
              if desired_room.upper() == "Q":
                  print("Thank you for playing..., goodbye!")
                  break
              if desired_room <= " ":
                  print("You did not enter a room, try again!")
                  continue          
              else:
                  room = Room(desired_room.upper(), person.name)
                  room.choose_room() 

game = Game()
game.begin()
