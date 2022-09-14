# Print Function in Python (end)
"""
print("Hello World", end=" * ")
print("This is First")
"""
# Print Function with seperater
'''
print("Vikrant","Aditya")
print("Vikrant","Aditya", sep="-", end="*")
'''
# Print Function with Escape Sequence
'''
print("c:\\nancy")
print("test:\"python2\"")
print("test:\'python2\'")
print("This is out python batch\n I am at lilly")
print("This is out python batch\n I am at\t lilly")
print("This is out python batch\n I\b am at lilly")
print("\x48\x45\x4C\x4C\x4F\x20\x57\x4F\x52\x4C\x44")
print(r"This is out python batch\n I\b am at lilly")
'''
# Store the output inside the file
'''
x=open("demo.txt", 'w')
print("Hello World", file = x)
x.close()
'''

