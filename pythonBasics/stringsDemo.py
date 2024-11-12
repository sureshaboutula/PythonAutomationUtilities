str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"
print(str[1]) # a

print(str[0:5]) # 0 to n-1 # Rahul

print(str + str1) # RahulShettyAcademy.comConsulting firm

print(str3 in str) # True

var = str.split(".")
print(var) # ['RahulShettyAcademy', 'com']
print(var[0]) # RahulShettyAcademy

str4 = " great "
print(str4)
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())