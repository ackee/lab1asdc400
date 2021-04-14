###########################
### Grupp 2_ASC400      ###
###########################    
### Alexander Norberg   ###
### Artin Nadjati-Yazdi ###
### Krister Fridström   ###
### Rickard Kutsomihas  ###
###########################
#!/usr/bin/env python3

def testcases():
    primepass = []
    eeapass = []
    phipass = []
    invpass = []
    primefail = []
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
            elif v[0] == 'prime':
                p = int(v[2])
                if v[1] == 'pass':
                    primepass.append(p)
                elif v[1] == 'fail':
                    primefail.append(p)    
    return primepass, eeapass, phipass, invpass, primefail, eeafail, phifail, invfail

"""
Task 1
The code below represents a loop of finding out if the given integer "num" is a prime number or not.
Given the integer, the code if-statement checks if the "num" is greater then 1, if it is, it checks if it is a prime number.
"""
def is_prime(num):
    if num <= 1 or num % 2 == 0:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(3,int(num**0.5),2):
        if (num % i) == 0:
            return False
    return True

"""
Task 2
The code below represents a function to check if the two values are relatively prime.
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
The code below represents the Euler phi function.
"""
def phi(n):
    r = 0
    for i in range(n):
        if(EEA(n, i) == 1):
            r += 1
    
    return r 

"""
Task 4
The code below represent the function for calculating the modular inverse
and to check if the value is invertible.
"""
def big_first(a,b):
    if a > b:
        return a,b
    else:
        return b,a

def modular_inverse(a,n):
    if (EEA(a,n) != 1):
        return -1
    t, newt = 0,1
    r, newr = n,a

    while newr != 0:
        q = r // newr
        t, newt = newt, t - q*newt
        r, newr = newr, r - q*newr

    if t < 0:
        t = t + n
    return t   
    
def run_prime():
    pnum = int(input("Insert a number to check if the number is prime: "))
    if is_prime(pnum) == True:
        print(f"{pnum} is a prime number.")
    else:
        print(f"{pnum} is not a prime number.")
    print("Press any key to go back to menu.")
    input()

def run_eea():
    a = int(input("Insert first number: "))
    b = int(input("Insert second number: "))
    result = EEA(a,b)
    if result == 1:
        print(f"{a} and {b} are relatively prime!")
    else:
        print(f"{a} and {b} are not relatively prime.")
    print("Press any key to continue...")
    input()

def run_phi():
    n = int(input("Insert number to check: "))
    r = phi(n)
    print(f"{n} has {r} relatively prime numbers.")
    print("Press the any key to go back.")
    input()

def run_inverse():
    a = int(input("Insert value to invert: "))
    n = int(input("Insert the modulo value: "))
    r = modular_inverse(a,n)
    if r == -1:
        print(f"{a} has no inverse in modulo {n}.")
    else:
        print(f"The inverse of {a} in modulo {n} is {r}.")
    print("Press any key to continue...")
    input()

def run_tests():
    #menu()
    primepass, eeapass ,phipass, invpass, primefail, eeafail, phifail, invfail = testcases()

    #Test prime
    print("Testing primality test - tests should pass")
    for p in primepass:
        evald = is_prime(p)
        if evald:
            print(f"PASSED - is_prime({p})={evald}.")
        else:
            print(f"FAILED - is_prime({p})={evald} should be True.")
    for p in primefail:
        evald = is_prime(p)
        if evald:
            print(f"FAILED - is_prime({p})={evald} - should be False.")
        else:
            print(f"PASSED - is_prime({p})={evald}.")
    #Test EEA
    print("\nTesting EEA algorithm - tests should pass:")
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
            print(f"PASSED - inverse({t[0]},{t[1]})= Inverse: not available, function gave {t[2]} ")

    print("Tests are finished running - press any key to go back to menu.")
    input()

def menu():
    option = 0
    while option != -1:
        print("------------------ Lab 1: RSA toolbox ----------------------------")
        print("[1] Task 1")
        print("[2] Task 2")
        print("[3] Task 3")
        print("[4] Task 4")
        print("[5] Task 5")
        print("------------------------------------------------------------------")

        option = int(input("Pick a task (-1 to quit): "))
        if option >= 1 and option <= 5:
            if option == 1:
                run_prime()
            elif option == 2:
                run_eea()
            elif option == 3:
                run_phi()
            elif option == 4:
                run_inverse()
            else:
                run_tests()
        else:
            print("Invalid choice - pick again.")    

if __name__ == "__main__":
    menu()

############################## Question ###################################################################################
"""
Question 1: How does the factorization problem relate to the RSA security?
            In other words, how can infeasibility of finding the prime factors of N help with the security of RSA?

Answer:     If the key is to short it can be brute forced in a short time, but if its a bigger aes-256 key even a 
            quantum computer of today cant break it within feasible time.

Question 2: How many values should be tested before deciding if n is prime or not?
            Why?

Answer:     Depends on how big the number is, if it's a 3-digit number one need to check primes up to 31
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29 and 31 (approximately, squareroot of the number divided by 2 minus 1).
            e.g.: for 100 you need to check -1+sqrt(100)/2=-1+10/2=-1+5=4 so 2,3,5 and 7 needs to be checked.

Question 3: What edge conditions have you tested using your automated test cases?

Answer:     
"""