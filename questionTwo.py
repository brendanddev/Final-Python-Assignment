#I Brendan Dileo, 000879513, certify's that this work is my own effort and that I have not allowed anybody else to copy from it.

# ----------------- Question 2  -----------------

def sieveOfE(largestValue): #Defines the function 'sieveOfE', which takes 'largestValue' as a parameter. This function will check if the numbers up to a given limit are prime, and then will list the prime numbers by eliminating non primes one by one.
   
    primes = [True] * ( largestValue + 1 ) #The variable 'primes' is assigned to a list where all variables will be considered True, and the length of this list will be the value of ' 'largestValue' + 1 '. Here is where we assume that ALL prime numbers up to a certain point will be True.
    primes[0] = False #As the list initially sets all values of the list to True(prime), we can set the list elements at index of '[0]' and '[1]' to False, as we know 0 and 1 will not be prime numbers.
    primes[1] = False #Sets list element at index [1] to false, refer to previous line.

    #The part of code which occurs beneath this point will find prime numbers up to the value assigned to 'largestValue' + 1

    for i in range(2, int(largestValue**0.5) + 1): #This outer loop will iterate through numbers in the list checking the multiples of each value to determine it a prime number or not. Each value the loop is checking will be assigned to 'i'. Starting at 2, and up to the square root of 'largestValue' + 1, which means it will be rounded to the nearest integer. Square root has been used because it allows for the most efficient form of 'guess and check' determining prime numbers.
        if primes[i]: #This if statement is a boolean statement, it will check the number occuring at the index of 'i' within the 'primes' list and either assign it to True or False based on the number/element at the 'i' index.
            for n in range( i * i, largestValue + 1, i ): #If the statement is True, this inner loop will check the value starting at 'i * i' as 'i' is the current prime number, going up by 'i' each iteration as any lower multiples have already been marked as prime or not prime. The loop will loop until the end point which is 'largestValue' rounded, and incrementing by 'i' checking if the multiples of the current value are prime.
                primes[n] = False #Everytime the loop iterates through, it comes to this line as the 'n' variable/value shows the a multiple of the 'i' which is a prime number. The primes list will keep track of the prime numbers found, and the place that value 'n' occurs on the index of primes will be set to False, because when 'n' comes into place, is with a non prime number, and the value at index 'n' is set to False within the 'primes' list.

    primeResult = [] #Empty list is created and named 'primeResult'
    for nums in range(2, largestValue + 1): #This for loop iterates through numbers as 'nums' between 2, and the 'largestValue' rounded up, using the range function
        if primes[nums]: #This if statement checks element/number at the 'nums' index in the 'primes' list. If the if statement is True, the next line of code is run, if not the number is not included
            primeResult.append(nums) #If the statement is True, it is added to the 'primeResult' list consising of prime numbers using append
    return primeResult #The list of prime numbers is returned

while True: #This infinite while loop is in place so even if the user enters a value less than 100, they can still have the chance to enter another number more than or equal to 100

    userValue = input( " Enter a value equal to, or greater than 100 (or 'exit' to quit): " ) #The user will input their value that must be equal to, or greater than 100

    if userValue == "exit": #If the user enters 'exit' then the following lines of code will run
        print( " Exiting " ) #The user will be prompted that the program is now exiting using the 'print' function
        break #This 'break' statement executes and ends the program if the user has entered 'exit'

    userValue = int(userValue) #If the user has not entered 'exit', the value they entered is now convereted to an integer

    if int(userValue) >= 100: #This if statement will make sure the 'userValue' which is the value the user enters is equal to, or larger than 100
        listOfPrimes = sieveOfE(userValue) #'listOfPrimes' variable is used to call upon the function 'sieveOfE' which takes 'userValue' as the argument for the function
        print ( f" The list of prime numbers up to {userValue} are: " ) #This line prints a string to the user telling them their list of prime numbers up to their value entered, which is replaced by an f-string of their entered value
        for prime in listOfPrimes: #This for loop finds all the 'prime' numbers in the 'listOfPrimes' list as all elements in this list are prime numbers
            print(prime) #This line then follows up to the previous one, printing the prime numbers in the list one per each line
    
    else: #This else statement will give the user an error if they have entered a number less than 100
        print( " Error! Number must be higher than or equal to 100 " ) #Prompts the user they have entered an icorrect value and have gotten an error via the 'print' function

#DEBGUGGING:
#Line 46: primes[0] and primes[1] == False ---> (Not working) ---> Fixed
#Line 49: print( f"{primes[0]} and {primes[1]}" ) ----> Ensure they are false to start
#Line 56: print( f"Primes after calculations: {primes}" ) --->Check to see the calculations were right.
#Line 62: print( f"Confirm final prime list: {listOfPrimes}" ) ---> Before the final list is output to the user, I confirm the calculations and the numbers in the list.
#Output: When trying to do larger numbers like 1,000,000 or 999,999,999 the program will not process/calculate these numbers