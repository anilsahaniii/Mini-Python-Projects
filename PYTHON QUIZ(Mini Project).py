playing = input("If you want to play this Python quiz, Please enter'yes': ")


if playing.lower() == 'yes':
    print("Welcome to Python Quiz")
else:
    quit()

score = 0
    
answer = input('In which year python 3 was released?: ')
if answer == '2008':
    print('Correct answer')
    score += 1
else:
    print("Wrong answer")
    

    
answer = input('Guido van Rossum developed PYTHON programimng language. Is it true or false: ')
if answer.lower() == 'true':
    print('Correct answer')
    score += 1
else:
    print("Wrong answer")
    
    
    
answer = input("Which one of the following is immutable, 'tuples' or 'listses'?: ")
if answer.lower() == 'tuples':
    print('Correct answer')
    score += 1
else:
    print("Wrong answer")
    
    
    
answer = input('Which one of the following is the correct example of an integer?(Enter the option)\n1)3  2)2.8 3)2E2 4)7e2 ')
if answer == '1':
    print('Correct answer')
    score += 1
else:
    print("Wrong answer")
    
    
answer = input("if a = 'Python'\na[3] = ? : ")
if answer == 'h':
    print('Correct answer')
    score += 1
else:
    print("Wrong answer")
    
print("You got " + str(score) + " questions correct")
print("You got " + str((score/4)*100) + "%")
