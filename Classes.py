class Students:
    def __init__(self, n, w):
        self.name = n
        self.weight = w
    
    def wieghtCheck(self):
        if self.weight >= 50:
            print(self.name, "is overwieght")

        elif self.weight == 0:
            print("Wieght incorrect!!!")
        
        else:
            print(self.name, "is Fit")

dhruv = Students("Dhruv Unde", 63)
dhruv.wieghtCheck()