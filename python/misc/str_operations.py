# string operations
s = "   The cat has another cat for a friend.   "

# Index and find
# index will raise an exception if the not found, can be used on all iterables
# find can be used only on str to find the substrings

print(s)
print("s.count('cat')   => ", s.count("cat"))
print("s.find('cat')      => ", s.find("cat"))
print("s.index('cat')   => ", s.index("cat"))
print("s.find('dog')     => ", s.find("dog"))
print("s.index('dog')  => exception")
#  r denotes --> finds the right most or the last occurence of 'cat'
print("s.rfine('cat')    =>", s.rfind("cat"))
print("s.rindex('cat')  =>", s.rindex("cat"))
print("s.lower()         =>", s.lower())
print(" s.upper()        => ", s.upper())
print(" s.replace('cat', 'dog') => ", s.replace("cat", "dog"))
print(" s.strip()        => ", s.strip())
print(" s.rstrip()        => ", s.rstrip())
print(" s.split(' ')       => ", s.split(" "))
print(" s.split()          => ", s.split())
print(" s.split('t')       => ", s.split("t"))
