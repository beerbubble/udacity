print 299792458 * 100 * 1.0/1000000000

print 299792458 * 100 * 1/1000000000


s = "<any string>"

print s[3]
print s[1+1+1]

print (s+s)[0]

print s[0] + s[1]

print s[0+1]

s = "任意字符串"

print s.find(s)

print 's'.find('s')

print s.find('')

print s.find('s')

print '3. 练习：Strings'

s=''

#print ('a' + s)[1:]

#print s[0] + s[1:]

print s + ''

print s[0:]

def is_friend(s):
    start = s[0:1]
    
    if (start == "D" or start == "N" ):
        return True
    return False


print is_friend('Diane')
#>>> True

print is_friend('Fred')


def biggest(n1,n2,n3):
    if (n1>=n2 and n1>=n3):
        return n1
    elif (n2 >= n3):
        return n2
    else:
        return n3


    from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    # your code here
    if work == "NOUN":
        return random_noun()
    elif work == "VERB":
        return random_verb()
    else:
        return work[0]


p =[1,2]
q = [3,4]
p.append(q)
print len(p)