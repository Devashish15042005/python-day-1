class father:
    def skill(self):
        print("father can drive")
class mother:
    def skill(self):
        print("mother can cook")
class child(father,mother):
    def skill(self):
        father.skill(self)
        mother.skill(self)
        print("child can code")
c = child()
c.skill()