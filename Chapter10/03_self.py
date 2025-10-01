class Employee:
    language = "Python" # This is class attribute
    salary =1200000

    def getInfo():
        print(f"The language is {language}. The salary is {self.salary}")

    def greet(self):
        print("Good morning")

harry = Employee()
#harry language = "JavaScript" # This is an instance atteibute
# harry.getInfo()
#Employee.getInfo(harry)