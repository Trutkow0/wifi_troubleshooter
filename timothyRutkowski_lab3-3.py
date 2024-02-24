# Timothy Rutkowski 02/12/2024 timothyRutkowski_lab3-3.py

# This program will help a user troubleshoot a bad wifi connection through a
# series of prompts.

# Define repetitive responses as constants
end = '\nGlad to be of service'
question = 'Did that fix the problem? (yes/no): '

# The main program
print('\nReboot the computer and try to connect')
response = input(question)
if response == 'yes':
    print(end)
    
else:
    print('\nReboot the router and try to connect')
    response = input(question)
    if response == 'yes':
        print(end)
        
    else:
        print('\nMake sure the cables between the router and the modem are plugged in firmly')
        response = input(question)
        if response =='yes':
            print(end)
    
        else:
            print('\nMove the router to a new location and try to connect')
            response = input(question)
            if response == 'yes':
                print(end)
    
            else:
                print('\nGet a new router')