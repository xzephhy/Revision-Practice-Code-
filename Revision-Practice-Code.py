#This is just a quick example code, I decided to practise on for the upcoming test.
j = 0

while j < 3:
  j = j + 1
  i = 1
  while i <= 3:
    if (13*j)+i == 41:
      print("Success", ",", 13*j+i)
    else:
      print("Failure", ",", 13*j+i)
      
    i = i + 1

print("End of Program.")

