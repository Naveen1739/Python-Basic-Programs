def add(s1,s2):
    return s1+' '+s2;
s1=input("Enter string one:")
s2=input("Enter string two:")
concat=add(s1,s2)
print("Concat of Two String is:",concat)
print()
def sumofdigit():
    num=int(input("Enter the range:"))
    sum=0
    for i in range(1,num):
        n=input("Enter Number "+str(i)+":")
        sum=sum+int(n)
    print("Som of Digit:",sum)
sumofdigit()
print()     
def vowels(str,count):
    vowel="aeiouAEIOU"
    for i in str:
        if i in vowel:
            count=count+1
    print("No.of.vowels:",count)
str=input("Enter a string:")
count=0
vowels(str,count)





















