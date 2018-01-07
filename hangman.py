import random
val = random.randint(1,4)
vocab = { 1 : "cerebrum",
          2 : "atrocius",
          3 : "spectrum",
          4 : "rendezvous"}
word = [i for i in vocab[val]]
ans = ['-' for x in range(len(word))]
tries = 3
flag=0
count=0

print "HANGMAN"
print (str('-')*len(word))

while (tries!=0):
    flag=0
    ch = raw_input("Guess character : ")
    for i in range(len(word)):
        if ch==word[i]:
            ans[i]=ch
            flag=1
            count=count+1

    print "".join(ans)

    if count==len(word):
        break
    elif (flag==1):
        print "%s characters found!"%(count)
        print "%s attempt(s) left!"%(tries)
    else:
        tries=tries-1
        print "%s tries left!"%(tries)

if (tries==0):
    print "Game Over"
    print "Answer is :" + " ".join(word)
else:
    print "You Won!"

