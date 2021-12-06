class StudentInfo :
    name = " "
    roll = " "
    cgpa = " "
    session = " "

    def setValue( self,name, roll, cgpa, session) :
        self.name = name
        self.roll = roll
        self.cgpa = cgpa
        self.session = session

    def display(self):
        print(f" Name : {self.name}, Roll : {self.roll}, Cgpa : {self.cgpa}, Session : {self.session}")


rahim = StudentInfo()
rahim.setValue("Khalekuzzaman","191","3.95","20")
rahim.display()

karim = StudentInfo()
karim.setValue("kaochar","161","3.85","70")
karim.display()
