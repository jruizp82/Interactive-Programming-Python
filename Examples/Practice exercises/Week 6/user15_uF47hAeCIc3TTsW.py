# Implementation of Student class


#################################################
# Student adds code where appropriate

# definition of Student class
class Student:
    
    def __init__(self, name, pwd):
        self.full_name = name
        self.password = pwd
        self.projects = []
        
    def get_name(self):
        return self.full_name
    
    def check_password(self, pwd):
        return self.password == pwd
    
    def get_projects(self):
        return self.projects
    
    def add_project(self, project):
        self.projects.append(project)
        
 
    
###################################################
# Testing code

joe = Student("Joe Warren", "TopSecret")

print joe.get_name()
print joe.check_password("qwert")
print joe.check_password("TopSecret")

print joe.get_projects()
joe.add_project("Create practice exercises")
print joe.get_projects()
joe.add_project("Implement Minecraft")
print joe.get_projects()


####################################################
# Output of testing code 

#Joe Warren
#False
#True
#[]
#['Create practice exercises']
#['Create practice exercises', 'Implement Minecraft']


