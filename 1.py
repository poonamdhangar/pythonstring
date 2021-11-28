# string interpolation method
name="poonam"
name1="sokin"
print(name +" "+name1)
# 2
print(f"hello {name} welcome too python tutorials and welcome to {name1} ")
#3
print("Hello {} Welcome to python tutorial".format(name))
# 3.1
print("Hello {p} wecome to python".format(p=name))
# 4
print("Hello Mr %s  welcome to python tutorial " %(name))
# 5
from string import Template
program ='python'
new = Template('Hello $name! This is $program.')
print(new.substitute(name= name,program=program))








