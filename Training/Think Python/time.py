import time
def days_since_epoch(t , ct):
    t = time.time()
    ct = time.localtime()
    print (t - ct)



def current_time():
    if time.time() == time.ctime():
       print ("It's EPOCH time ")
    else:
         print ("It's CURRENT time ")


print (time.time() - time.localtime())

def automated_check_fermat():
    prompt = input("How much is A ?\n")
    a = int(input(prompt))

    prompt = input("How much is B ?\n")
    b = int(input(prompt))

    prompt = input("How much is C ?\n")
    c = int(input(prompt))

    prompt = input("How much is N ?\n")
    n = int(input(prompt))

automated_check_fermat
