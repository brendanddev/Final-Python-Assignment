#@author: Brendan Dileo.

# ----------------- Question 1  -----------------

def songLyrics(animalInfo): #Defines the function 'songLyrics' which will take one parameter 'animalInfo' which is used to finish a set of song lyrics 
    
    animal, sound = animalInfo #This is taking two variables entered by the user and assigning them into a two element one dimension list where 'animal' will be the first element and 'sound' will be the second element

    lyrics = " Old Macdonald had a farm, E I E I O " #The variable 'lyrics' is assigned to a string, which is the first line of lyrics
    lyrics = lyrics + " \n " #Within the 'lyrics' variable, we are adding a new line to the 'lyrics' making them more readable
    lyrics = lyrics + f" On his farm he had a {animal}, E I E I O " #The 'lyrics' are now added with a f-string where 'animal' is the users input and the rest of the string is the second line of the song lyrics
    lyrics = lyrics + " \n " #Adding a new line to the 'lyrics' for readability and clearness
    lyrics = lyrics + f" With a {sound} {sound} here, and a {sound} {sound} there" #This represents the third line of the 'lyrics' and uses a f-string, where sound is the sound that the user input for the animal
    lyrics = lyrics + " \n "
    lyrics = lyrics + f" Here a {sound}, there a {sound}, everywhere a {sound}, {sound} "
    lyrics = lyrics + " \n "
    lyrics = lyrics + " Old Macdonald had a farm, E I E I O " #This is the last line of the 'lyrics', combined with the rest of our 'lyrics' to this point
    print (lyrics) #This will now print the variable 'lyrics' which has been assigned to the string/f-string of lyrics that has been created with user input
    return lyrics

animalList = [] #The variable 'animalList' is assigned to an empty list which will be used for storing the lists of 'animal' and 'sound' chosen by the user

while True: #This infinite while loop is being used to let the user enter an infinite number of 'animal''s and 'sound''s which in turn will print the 'lyrics' the number of times the pair is entered
    
    animal = input( " Please enter an animal name (or '-1' to quit): " ) #The user is prompted with a string asking them to enter the animal name, or to quit. The animal name is being saved into/assigned to the variable 'animal'

    if animal == "-1": #This if statement within the while loop checks if the user has entered '-1' instead of the animal name with the intention of quitting the program
        print( " Exiting " )  #The user will be prompted that the program is now exiting using the 'print' function
        break #If the user has entered '-1' this 'break' statement within the if statement will execute quitting the program

    sound = input ( f" Enter the sound the {animal} makes (or '-1' to quit) : " ) #The user is prompted with an f-string asking them to enter the sound the animal makes, or to quit. 'animal' is the the string the user input, and they can see this as I have used an f-string. The sound the animal makes is saved into the variable 'sound'

    if sound == "-1": #This if statement within the while loop checks if the user has entered '-1' instead of the sound the animal makes with the intention of quitting the program
        break #If the user has entered '-1' this 'break' statement within the if statement will execute quitting the program

    animalList.append([animal, sound]) #This list method adds the sublist which is '[animal, sound]' to the main list which is 'animalList'

for animalAndSound in animalList: #This for loop will iterate through every 'animalAndSound' in the main list 'animalList'. Where each element within the list will be a sublist consisting of an animal name and animal sound as 'animal' and 'sound' and is dependent on what the user enters
    print( animalAndSound ) #This will print every element of the 'animalList' the for loop finds to show the nested list to show the nested lists

for animalAndSound in animalList: #This for loop will iterate through every element/'animalAndSound' in 'animalList' -
    songLyrics(animalAndSound) # - This line calls upon the function 'songLyrics' and passes the argument 'animalAndSound' to the function for each iteration it finds 'animalAndSound' and this is passed as an iterable with two elements

#DEBUGGING:
#Line 3: print( f"Animal is: {animal} and Sound is: {sound} " ) ---> Checking what has been assigned to what variable
#Line 5: print(animalInfo) ---> At first my code kept giving me an error
#Line 16: print( f"Animal List is: {animalList} " ) ---> Makes sure animalList is assigned to empty list
#Line 28: print( f"Animal is: {animal} and Sound is: {sound} " ) ---> Checks what variables will be put into the list before its added into the list
#Line 31: print( f"Animal and Sound List(so far) is: {animalAndSound} " ) ---> Checks what sub list is being added into the main list
