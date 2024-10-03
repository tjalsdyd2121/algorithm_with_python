class Calculator : 
  # class variable
  version = '1.0.0'
  
  # For >> self << , it would be Object itself.
  # For first parameter of method, it must be self.
  
  def __init__(self): # constructer : __init__
    self.result = 0
  def add(self,num) : # fucntion in class == Method.
    self.result += num
    return self.result

cal1 = Calculator() # Object 1 
cal2 = Calculator() # Object 2

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# useful form with loop.
print(Calculator.add(cal1, 2))

# inheritance : 
class Calculator_with_substract(Calculator):
  def sub(self,num) :
    self.result -= num
  # method overriding
  def add(self,num) :
    self.result += num * 2

sub_cal = Calculator_with_substract()
print(sub_cal.add(3))

