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
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def change_name(self, new_name):
       self.new_name = new_name
       
    def change_age(self, new_age):
        self.new_age = new_age

    def add_track(self, add_track):
        self.add_track = add_track

    def get_score(self):
        return self.score
    
    def display_newinfo(self):
        print(self.name, self.age, self.tracks, self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

print(Bob.change_name("Peter"))
print(Bob.change_age("34"))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())

Bob.display_newinfo()