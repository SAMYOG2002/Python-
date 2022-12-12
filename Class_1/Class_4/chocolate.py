rs = int(input("enter rupees: "))
choc = 0
wrap = 0
while(rs >= 1 ):
   choc = choc + 1
   rs = rs - 1
   wrap = wrap + 1
   while(wrap >= 3 ):
      choc = choc + 1
      wrap = wrap - 3 + 1

print("The amount of chocolate you can get is: ",choc)     
