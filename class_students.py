class students :
    def __init__(self, First=None , Last=None, English=None , Math=None, Scince=None, Average=None):
        self.First = First
        self.Last = Last
        self.English = English
        self.Math = Math
        self.Scince = Scince
        self.av = Average
    
    def average(self):
        self.av = (self.English + self.Math + self.Scince)/3
        return self.av

    def passed(self):
        if self.av < 10 :
            return "FAILED"
        else:
            return "PASSED"

shahrad = students("shahrad", "fakhr", 12, 4, 5)
shahrad_av = shahrad.average()
print(shahrad_av)
print(shahrad.passed())