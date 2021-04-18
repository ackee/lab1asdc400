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
    primet = []
    eeat = []
    phit = []
    invt = []

    with open('testcases.txt', mode='r', encoding='UTF8') as reader:
        a = reader.readlines()
        for line in a:
            try:
                if line[0] == '#':
                    continue
                v = line.split(',')
                if v[0] == 'eea':
                    l = list(map(lambda x : int(x),v[1:4]))
                    eeat.append(l)
                elif v[0] == 'phi':
                    l = list(map(lambda x: int(x), v[1:3]))
                    phit.append(l)
                elif v[0] == 'inverse':
                    l = list(map(lambda x: int(x), v[1:4]))
                    invt.append(l)
                elif v[0] == 'prime':
                    p = int(v[1])
                    b = v[2].lower().strip()
                    # If b string is "true", res evaluates boolean value true, otherwise false.
                    res = (b == 'true')
                    primet.append([p, res])
            except ValueError:
                print(f"Format error, skipping line: {line}")
    return primet, eeat, phit, invt

"""
Task 1
The code below represents a loop of finding out if the given integer "num" is a prime number or not.
Given the integer, the code if-statement checks if the "num" is greater then 1, if it is, it checks if it is a prime number.
Source description: https://en.wikipedia.org/wiki/Primality_test
"""
def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num <= 1 or num % 2 == 0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if (num % i) == 0:
            return False
    return True

"""
Task 2
The code below represents a function to check if the two values are relatively prime.
Source description: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
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
Source description: https://en.wikipedia.org/wiki/Euler%27s_totient_function
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
Source description: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Computing_multiplicative_inverses_in_modular_structures
"""

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
    n_errors = 0
    #menu()
    primetests, eeatests ,phitests, invtests = testcases()

    #Test prime
    print("Testing primality test - tests should pass")
    for p in primetests:
        # p has format [int,bool] where int is the prime value
        # and the bool is the expected boolean value.
        evald = is_prime(p[0])
        if evald == p[1]:
            print(f"PASSED - is_prime({p[0]})={evald}.")
        else:
            n_errors += 1
            print(f"FAILED - is_prime({p[0]})={evald} should be {p[1]}.")

    #Test EEA
    print("\nTesting EEA algorithm - tests should pass:")
    for t in eeatests:
        evald = EEA(t[0],t[1])
        if evald == t[2]:
            print(f"PASSED - EEA({t[0]},{t[1]})={evald}")
          
        else:
            n_errors += 1
            print(f"FAILED - EEA({t[0]},{t[1]})={evald} expected {t[2]}")
    
    #Test Phi
    print("\nTesting Phi algorithm - tests should pass:")
    for t in phitests:
        evald = phi(t[0])
        if evald == t[1]:
            print(f"PASSED - phi({t[0]})={evald}")
        else:
            n_errors += 1
            print(f"FAILED - phi({t[0]})={evald} expected {t[1]}")
            
    #Test Inverse
    print("\nTesting Inverse algorithm - tests should pass:")
    for t in invtests:
        evald = modular_inverse(t[0], t[1])
        if evald == t[2]:
            print(f"PASSED - inverse({t[0]},{t[1]})={evald}")
        else:
            n_errors += 1
            print(f"FAILED - inverse({t[0]},{t[1]})={evald} expected {t[2]}")

    if n_errors >= 1:
        print(f"Got {n_errors} failed tests.")
    else:
        print("All tests passed!")
            
    print("Tests are finished running - press any key to go back to menu.")
    input()

def menu():
    option = 0
    while option != -1:
        print("------------------ Lab 1: RSA toolbox ----------------------------")
        print("[1] Task 1 - Prime numbers")
        print("[2] Task 2 - EEA")
        print("[3] Task 3 - phi")
        print("[4] Task 4 - inverse")
        print("[5] Task 5 - automated tests")
        print("------------------------------------------------------------------")

        try:
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
            elif option == -1:
                print("Good bye.")
            else:
                print("Invalid choice - pick again.")
        except ValueError:
            print("Not a valid input, only numbers allowed!") 

if __name__ == "__main__":
    menu()

############################## Questions ###################################################################################
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

Answer:     We have tested for negative values which in general should not work and also checked for
            known values which we know the answer to.
"""