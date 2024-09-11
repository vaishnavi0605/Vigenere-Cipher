#importing the libraries
import string
import random

def textstrip(filename):
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letters!
    '''
    #opening the file
    f = open("english_random.txt",'r')
    #reading the file
    s = f.read()
    l='abcdefghijklmnopqrstuvwxyz'
    #initializing the string
    clean=""
    #iterating through the string
    for i in s:
        #checking if the letter is a space
        if i in l:
            #making the string
            clean=clean+i
#returning the string
    return clean

def letter_distribution(s):
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''
    #creating the dictionary
    distribution={}
    #creating the list
    l='abcdefghijklmnopqrstuvwxyz'
    #initializing the dictionary
    for i in l:
        distribution[i]=0
    #iterating through the string
    for i in s:
        #counting the number of occurences of each letter
        distribution[i]=distribution[i]+1
#returning the dictionary
    return distribution

#create a dictionary of substitutions
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b=[]
sub_to={}
for i in l:
    while True:
        rand = random.randint(0,25)
        if l[rand] not in b:
            b.append(l[rand])
            sub_to[i]=l[rand]
            break

def substitution_encrypt(s,d):
    '''encrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    #initializing the string
    t='' 
    #iterating through the string
    for i in s:
        #checking if the letter is a space
        if i in sub_to:
            #making the encrypted string
           t=t+sub_to[i]
#returning the encrypted string
    return t


def substitution_decrypt(s,d):
    '''decrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    #initializing the string
    t=''
    #iterating through the string
    for i in s:
        #checking if the letter is a space
        for j in d:
            #making the decrypted string
            if d[j]==i:
                t=t+j
    #returning the decrypted string
    return t


def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, predict the d'''
    #sorting the dictionary
    sorted_list=sorted(letter_distribution(s),key=letter_distribution(s).get)
    sorted_list.reverse()
    #creating the frequency list
    freq_list=['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']
    #creating the dictionary with matching frequency
    d={}
    for i in range(26):
        d[sorted_list[i]]=freq_list[i]
#returning the dictionary
    return d
    

def vigenere_encrypt(s,password):
    '''Encrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    t=''
    store=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    p=0
#iterating through the string
    for i in s:
#checking if the letter is a space
        if i=='':
            t=t+i
#checking if the letter is not a space
        else:
            alpha=store.index(i)
            beta=store.index(password[p])
#finding the encrypted letter
            t=t+store[(alpha+beta+1)%26]
            p=p+1
#checking if p is equal to the length of password
            if p==len(password):
                p=0
#returning the encrypted string
    return t


def vigenere_decrypt(s,password):
    '''Decrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    t=''
    #creating the store list
    store=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#initializing p to 0
    p=0
#iterating through the string
    for i in s:
#checking if the letter is a space
        if i=='':
            t=t+i
#checking if the letter is not a space
        else:
            alpha=store.index(i)
            beta=store.index(password[p])
#finding the decrypted letter
            t=t+store[(alpha-beta-1)%26]
            p=p+1
#checking if p is equal to the length of password
            if p==len(password):
                p=0


def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''
    #rotating the string
    t=s[r:]+s[:r]
    #setting count to 0
    count=0
    #iterating through the string
    for i in range(len(s)):
        if s[i]==t[i]:
            #counting the number of collisions
            count=count+1
    #returning the probability of collision
    return count/len(s)

def cryptanalyse_vigenere_afterlength(s,k):
    '''Given the string s which is known to be vigenere encrypted with a
    password of length k, find out what is the password'''
    #creating the frequency list
    freq_list=['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']
    #creating the store list
    store=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #initializing string
    password=''
    #iterating through the string
    for i in range(k):
        #creating empty list and dictionary
        stock=[]
        d={}
        #iterating through the string with step size k
        for j in s[i::k]:
            #checking if the letter is already in the list
            if j not in stock:
                stock.append(j)
                d[j]=1
            #if the letter is already in the list
            else:
                d[j]=d[j]+1
        #sorting the dictionary
        sorted_list=sorted(d,key=d.get)
        #reversing the list
        sorted_list.reverse()
        #finding index of letter with maximum frequency
        alpha=store.index(sorted_list[i])
        beta=store.index(freq_list[i])
        #finding the letters of password 
        password=password + store[(alpha-beta-1)%26]
#returning the password
    return password

            


def cryptanalyse_vigenere_findlength(s):
    '''Given just the string s, find out the length of the password using which
    some text has resulted in the string s. We just need to return the number
    k'''
#iterating through the string to find the probability of collision
    for k in range(1,len(s)):
#calling function for finding probability of collision
        prob=rotate_compare(s,k)
#checking if the probability is greater than 0.062
        if prob>0.062:
#returning the value of k
            return k




def cryptanalyse_vigenere(s):
    '''Given the string s cryptanalyse vigenere, output the password as well as
    the plaintext'''
#calling function for finding password length
    password_length= cryptanalyse_vigenere_findlength(s)
#calling function for finding password
    password= cryptanalyse_vigenere_afterlength(s,password_length)
#calling function for finding plaintext
    plaintext=vigenere_decrypt(s,password)
#returnimg the plaintext and password
    return plaintext,password


#executing the functions
code = input("Enter the code: ")
encrypted_text=vigenere_encrypt(textstrip("english_random.txt"),code)
plain,generated_code=cryptanalyse_vigenere(encrypted_text)
print("your password is: ",generated_code)

