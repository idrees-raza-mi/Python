class Marks():
    smarks = [11]
    def input():
      for i in range(0, 3):
        Marks.smarks=int(input("insert your marks :"))
    def Grade(self):
         for i in range(0,3):
                if(self.smarks[i]<50):
                    print("F")
                else:
                    print("Pass")

    
Marks.input()
Marks.Grade()
