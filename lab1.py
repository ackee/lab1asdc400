#!/usr/bin/env python3

def parse_EEA():
    pass

def parse_phi():
    pass

def parse_inverse():
    pass

def testcases():
    eeapass = []
    phipass = []
    invpass = []
    eeafail = []
    phifail = []
    invfail = []
    with open('testcases.txt', mode='r', encoding='UTF8') as reader:
        a = reader.readlines()
        for line in a:
            if line[0] == '#':
                continue
            v = line.split(',')
            if v[0] == 'eea':
                l = list(map(lambda x : int(x),v[2:5]))
                if v[1] == 'pass':
                    eeapass.append(l)
                elif v[1] == 'fail':
                    eeafail.append(l)
            elif v[0] == 'phi':
                l = list(map(lambda x: int(x), v[2:4]))
                if v[1] == 'pass':
                    phipass.append(l)
                elif v[1] == 'fail':
                    phifail.append(l)
            elif v[0] == 'inverse':
                l = list(map(lambda x: int(x), v[2:5]))
                if v[1] == 'pass':
                    invpass.append(l)
                elif v[1] == 'fail':
                    invfail.append(l)
            
    return eeapass, phipass, invpass, eeafail, phifail, invfail
            




"""
Task 1
The code below represents a loop of finding out if the given integer "num" is a prime number or not.
Given the integer, the code if-statement checks if the "num" is greater then 1, if it is, it checks if it is a prime number.
"""

def checking_if_prime(num):
 

    if num > 1:  
         for i in range(2,num):  
            if (num % i) == 0:  
                return False
                
            else:  
                return True
                        
    else:  
        return False

"""
Task 2
"""

def EEA(a,b):
    old_r, r = a,b
    old_s, s = 1,0
    old_t, t = 0,1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t

    return old_r


"""
Task 3

"""
def phi(n):
    r = 0
    for i in range(n):
        if(EEA(n, i) == 1):
            r += 1
    
    return r 


"""
Task 4
"""

def big_first(a,b):
    if a > b:
        return a,b
    else:
        return b,a


def modular_inverse(a,n):
    t, newt = 0,1
    r, newr = n,a

    while newr != 0:
        q = r // newr
        t, newt = newt, t - q*newt
        r, newr = newr, r - q*newr

    if t < 0:
        t = t + n
    return t   
    
        
"""


def menu():
    print("[1] Task 1")
    print("[2] Task 2")
    print("[3] Task 3")
    print("[4] Task 4")
    print("[5] Task 5")

    option = int(input("Pick a task: "))
    while option != 0:
        if option == 1:
            checking_if_prime()
        elif option == 2:
            EEA()
        elif option == 3:
            phi()
        else:
            modular_inverse()
           

"""



if __name__ == "__main__":
    #menu()
    eeapass ,phipass, invpass, eeafail, phifail, invfail = testcases()
    #Test EEA
    print("Testing EEA algorithm - tests should pass:")
    for t in eeapass:
        evald = EEA(t[0],t[1])
        if evald == t[2]:
            print(f"PASSED - EEA({t[0]},{t[1]})={evald}")
        else:
            print(f"FAILED - EEA({t[0]},{t[1]})={evald} expected {t[2]}")

    print("\nTesting EEA algorithm - tests should fail:")
    for t in eeafail:
        evald = EEA(t[0],t[1])
        if evald == t[2]:
            print(f"FAILED - EEA({t[0]},{t[1]})={t[2]} function gave {evald}")
        else:
            print(f"PASSED - EEA({t[0]},{t[1]})={t[2]} function gave {evald}")

    #Test Phi
    print("\nTesting Phi algorithm - tests should pass:")
    for t in phipass:
        evald = phi(t[0])
        if evald == t[1]:
            print(f"PASSED - phi({t[0]})={evald}")
        else:
            print(f"FAILED - phi({t[0]})={evald} expected {t[1]}")
            
    print("\nTesting Phi algorithm - tests should fail:")
    for t in phifail:
        evald = phi(t[0])
        if evald == t[1]:
            print(f"FAILED - phi({t[0]})={t[1]} function gave {evald}")
        else:
            print(f"PASSED - phi({t[0]})={t[1]} function gave {evald}")

    #Test Inverse
    print("\nTesting Inverse algorithm - tests should pass:")
    for t in invpass:
        evald = modular_inverse(t[0], t[1])
        if evald == t[2]:
            print(f"PASSED - inverse({t[0]},{t[1]})={evald}")
        else:
            print(f"FAILED - inverse({t[0]},{t[1]})={evald} expected {t[2]}")
            
    print("\nTesting Inverse algorithm - tests should fail:")
    for t in invfail:
        evald = modular_inverse(t[0], t[1])
        if evald == t[2]:
            print(f"FAILED - inverse({t[0]},{t[1]})={t[2]} function gave {t[2]}")
        else:
            print(f"PASSED - inverse({t[0]},{t[1]})={t[2]} function gave {t[2]}")