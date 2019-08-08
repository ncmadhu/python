class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber
        
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.scores = scores
        self.average = sum(self.scores) / len(scores)
        Person.__init__(self,firstName, lastName, idNumber)
    
    def calculate(self):
        if 90 <= self.average <= 100:
            self.grade = 'O'
        elif 80 <= self.average <= 90:
            self.grade = 'E'
        elif 70 <= self.average <= 80:
            self.grade = 'A'
        elif 55 <= self.average <= 70:
            self.grade = 'P'
        elif 40 <= self.average <= 55:
            self.grade = 'D'
        else:
            self.grade = 'T'
        return self.grade
        
line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()