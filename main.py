# class Student:
#     # [assignment] Skeleton class. Add your code here
#     def __init__(self):
#         pass



# Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# # Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()

class Student:
    def __init__(self, name:str, age:int, tracks:list, score:float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def change_name(self, new_name):
        self.name = new_name
       
    def change_age(self, new_age):
        self.age = new_age 

    def add_track(self, new_track):
        self.tracks.extend([new_track])
        
    def get_score(self):
        return self.score
    
    def updated_info(self):
        print()
        print("Name:", self.name)
        print("Age:", self.age)
        print("Track: ", self.tracks)
        print("Score:", self.score)
        print()

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

Bob.change_name("Peter")
Bob.change_age("34")
Bob.add_track("UI/UX")
Bob.get_score()

Bob.updated_info()