print("Before") 
for thing in [9,41,12,3,74,15]:
    print(thing)
print("after")

print("Before")
t = [9,41,12,3,74,15]
for i in t:
    print(i)
print("After")


t = [9,41,12,3,74,15]
largest_so_far = -1
for i in t:
    if i > largest_so_far:
        largest_so_far = i
    print(largest_so_far)


t = [9,41,12,3,74,15]
count = 0
for i in t:
    count += 1
    print(count,i)


t = [9,41,12,3,74,15]
total = 0
for i in t:
    total += i
    print(total)

    
t = [9,41,12,3,74,15]
count = 0
total = 0
for i in t:
    count += 1 
    total += i
    print(count,total,total/count)


t = [9,41,12,3,74,15]
for i in t:
    if i > 25:
        print(i) #filteering a loop


t = [9,41,12,3,74,15]
smallest = -1
for i in t:
    if i < smallest:
        smallest = i
    print(smallest, i) #smqllest value


t = [9,41,12,3,74,15]
found = False
for i in t:
    if i == 3:
        found = True
    print(found,i) #boolean

t = [9,41,12,3,74,15]
smallest = None
for i in t:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
    print(smallest)

count = 0
while count < 100:
    count += 1
    print(count)

count = 100
while count > 0:
    print(count)
    count -= 1

def find_max( a, b,c ):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(find_max(1,21,3))



sample = (8,2,3,0,7)
def find_sum(sample):
    total = 0
    for x in sample:
        total += x
    return total
print(find_sum(sample))


sample = (8,2,3,-1,7)
def multiply(sample):
    total = 1
    for i in sample:
        total *= i
    return total
print(multiply(sample))


def find_factorial(n):
    if n <= 1:
        return 1
    if n > 1:
        return n * find_factorial(n-1)

print(find_factorial(6))

fruit = "banana"
for l in fruit:
    print(l)


fruit = "banana"
count = 0
while count < len(fruit):
    letter = fruit[count]
    print(count,letter)
    count += 1

word = "banana"
count = 0
for l in word:
    if l == "a":
        count += 1
print(count)

word = "banana"
if "nana"  in word:
    print("Found it")

word = "banana is mine"
print(word.find("na"))

data = "From stephen.marquard@uct.ac.za Sat Jan 5 9:14:16 2008"
s = data.find("@")
ss = data.find("Sat")
sss = data[s:ss]
print(sss)

txt = "welcome to the jungle"
x = txt.split()
x.sort() # the sort function is used without a variable.

print(x)


#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
   # line = line.rstrip()
  #  l = line.split()
 #   for words in l:
#        if words in lst:
   #         continue
  #      else:
 #           lst.append(words)
#lst.sort()
#print(lst)

data = [1,2,3,4,5,6]
#data.reverse()
#Syntax: reversed_list = systems[start:stop:step] 
#data_2 = data[::-1]
for o in reversed(data):
    print(o)
#print(data_2)

counts = dict()
names = ["one", "two","one", "three", "one", "two"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

counts = dict()
names = ["one", "two","one", "three", "one", "two"]
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)

# x = input(" enter your statement:")
# g = x.split()
# counts = dict()
# for name in g:
#     counts[name] = counts.get(name,0) + 1
# print(counts)

data = {"Joseph":1, "Esther":2, "Michael":3, "Isaac":4}
for key in data:
    print(key, data[key])


data = {"Joseph":1, "Esther":2, "Michael":3, "Isaac":4}
print(data)
print(list(data))
print(data.items())
print(data.keys())
print(data.values())

data = {"Joseph":1, "Esther":2, "Michael":3, "Isaac":4}
for d,k in data.items():
    print(d,k)

# import socket #the use of sockets
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(("data.pr4e.org", 80))
# cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end="")
# mysock.close()

# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
# for line in fhand:
#     print(line.decode())

import xml.etree.ElementTree as ET
data = '''<person>
             <name>Chuck</name>
             <phone type = "yes" >
                 +255741769611
             </phone>
             <email hide = "yes"/>
          </person>'''

j = ET.fromstring(data)
print("Name:", j.find("name").text)
print("Attribute:",j.find("email").get("hide"))

import xml.etree.ElementTree as ET

data = '''<users>
             <user x = "2">
                <name>Chuck</name>
                <age>7</age>
                <sex>male</sex>
             </user>
             <user x = "7">
                <name>Essy</name>
                <age>18</age>
                <sex>female</sex>
             </user>
          </users>'''
d = ET.fromstring(data)
lst = d.findall("users/user")
print("Count:", len(lst)) # daata to be copied from the net.

# IN JSON json.loads converts the json string into an object in python while
# the json.dumps converts the object into the string
# the json.load loads a file into an object

import json

data = '''{"people":
                    [
                    {
                    "name": "Isaac kabucho",
                    "phone": "0712345687",
                    "emails": ["kk@gmail.com","ii@yahoo.com"],
                    "has_license": false
                    },
                    {
                    "name": "Michael Kuria",
                    "phone": null,
                    "emails":["mk@gmail.com","mw@hotmail.com"],
                    "has_license": true
                    }
                    ]
                    }'''

d = json.loads(data)
# for person in d["people"]:
#     print(person["name"],person["emails"])
for person in d["people"]:
    del person["phone"]
e = json.dumps(d, indent = 2, sort_keys = True)
print(e)

import json
from urllib.request import urlopen

# with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
#     source = response.read()
#
# d = json.loads(source)
# print(d)

import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(usd_rates['USD/INR'])

