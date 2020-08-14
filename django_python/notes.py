mypairs = [(1,2),(3,4),(5,6)]

# tuple unpackkig
for tup1,tup2 in mypairs:
    print(tup1)
    print(tup2)

# Lambda Expression

    # filter

mylist = [1,2,3,4,5,6,7,8,9,10]
def even_bool (num):
    return num%2 == 0

evens = filter(even_bool,mylist)
print(list(evens))

    # Lambda

evens = filter(lambda num:num%2==0,mylist)
print(list(evens))

#  use case of split built-in fun

tweet = 'Go Sports! #Sports'
tweet.split('#')
print(tweet.split('#')[1])
