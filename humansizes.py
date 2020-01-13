SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],   #all caps means it's a const
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}  #this is a 'dictionary', collection of key value pairs
#keys can be numbers, [] with things in it is a list, not an array

# Instead of the word `function`, in Python, you use `def`
def approximate_size(size, a_kilobyte_is_1024_bytes=True):   #template for declaring a function, params are positional like in JS
    #booleans are capitalized

#a more formal and descriptive "commment" about what this function does
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000   #ternary in python
    for suffix in SUFFIXES[multiple]:   #for loop,  suffix is taco on this line
        size /= multiple  # /= same as +=
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)  # or f'{size:.1f} {suffix}',

    raise ValueError('number too large') #indentation tells you this is the end of the function, next line is not indented

#if __name__ == '__main__':
    #print(approximate_size(16384, False))
    #print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=True))
    #print(approximate_size(-16384))


    #== means compare

name = "Fred"
def say_name():
    global name
    name = "Bubba"
    print("internal", name)

say_name()
print("external", name)


#if/else
name = "Stebe"
if name == "Steve":
    print("I feel great")
elif name == "Joe":
    print("You got the better instructor")
else: 
    print("I have a cold")


#string concatenation

#still have dynamic typing (but no implicit coercion)

print(f"My name is {name}") #need an f wherever there is string interpolation


#Collections
#list
junk = ["Fred", True, [1,2,3,], 234]
print(junk)

#adding to a list
junk.append("uh-oh") #append only ads one thing at a time
print(junk)
junk.insert(3, "oh i get it") #only adds two
print(junk)
junk.extend(["Mary", "Joseph", "Bob"]) #to add multiple things
print(junk)

names = ["Mary", "Joseph", "Bob"]
print(",".join(names))  #join outputs a string

#Dictionaries
my_pairs = {
    123: "number",
    "name": "Broomhilda"
}

print(my_pairs[123])
my_pairs["last"] = "Jones"
print(my_pairs)
my_pairs["address"] = {"number": 123,
"street": "Sesame St" }
print(my_pairs)

street_name = my_pairs["address"]["street"]

print(street_name)

#sets
my_set = ["fred", True, 123, "Jones", "fred"]
print(my_set)
print(set(my_set)) #turns brackets into curlies(set into list), gets rid of duplicates

my_stuff = {1,2,3}
my_stuff.add("Feed me")
print(my_stuff)

#tuple
my_tup = (1,2,3,3, "hello")
print(my_tup)

#loops
for foo in junk:
    print(f"Why do I still have {foo} in this drawer?")
    
    #slice
    my_list = [1,2,4, "hello", "monkey"]
    my_subset = my_list[0:3]
    my_subset = my_list[1:3]
    my_subset = my_list[:3]
    my_subset = my_list[2:34]
    my_subset = my_list[2:-1]