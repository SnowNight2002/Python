class People:
    def  __init__ (self, vaccine):  #(a) define the constructor
        self.vaccine= vaccine  	 #(b) initialize the instance variable vaccine
        self.shotCount = 0   	  # (c) initialize the instance variable shotCount
    
    def shoot(self):
        if  self.shotCount == 2     :  #(d) the maximum number of shots is two
            print("Cannot receive more than 2 shots of " + self.vaccine)
        else:
            self.shotCount +=1  	   # (e) update the instance variable shotCount 
    
    def report(self):
        print(f"Received {self.shotCount} shot(s) of {self.vaccine}")  #(f) display current values of all instance variables

jack = People("Vaccine-X")  # jack plans to take a vaccine named "Vaccine-X"
for i in range(3):
    jack.shoot()
    jack.report()