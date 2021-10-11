# https://www.hackerrank.com/challenges/30-inheritance/problem?h_r=next-challenge&h_v=zen

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.score = (sum(scores)) / len(scores)
        self.grade = ''

    def calculate(self):
        if 90 <= self.score <= 100:
            self.grade = "O"
        elif 80 <= self.score < 90:
            self.grade = "E"
        elif 70 <= self.score < 80:
            self.grade = "A"
        elif 55 <= self.score < 70:
            self.grade = "P"
        elif 40 <= self.score < 55:
            self.grade = "D"
        elif self.score < 40:
            self.grade = "T"
        return self.grade


# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here


#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print(f"Grade: {s.calculate()}")
