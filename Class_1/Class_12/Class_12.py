class sagarmatha:
    def __init__(self,name):
        self.name = name
        print("Constructor")
    
    def home(self,age):
        print(self.name)
        print(f"My name is {self.name} age is {age}")
       
    def __del__(self):
        print("Destructor")
  
# sg1 = sagarmatha("samyog","21")
# sg2 = sagarmatha("subash","21")
# sg3 = sagarmatha("sujal","21")

# sg1.home()
# sg2.home()
# sg3.home()

sg = sagarmatha("samyog")
sg.home(21)








