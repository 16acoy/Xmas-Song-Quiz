#Reset Scores
#scores=open('scores.txt','w')
#scores.write('emily_hurcomb\n' + '0\n')
#scores.close()

#Could add how close their answer was?, show top scores when only 0?

#making the logins list
print('Welcome to the Christmas Song Quiz!')
loginss=[['',''], ['', ''], ['', ''], ['', '']]
loginss[0]=['emily_hurcomb', 'm4tt16']
loginss[1] = ['emily_hayden', 'hat3econ0mic5']
loginss[2] = ['ellie_soave', 'h0rs3gir1']
loginss[3] = ['gabi_akinfaderin', 'i<3joll0f'] 

#entering username
userValid='false'
currentUser = input('Please enter your username: ')

#checking if username is in list
for i in range (0,4):
    if currentUser == loginss[i][0]:
        userValid='true'
        userNumber=i
    elif currentUser != loginss[i][0] and userValid !='true':
        userValid='false'
        
#denying access/entering password
if userValid == 'false':
    print('Username invalid')
elif userValid=='true' :
    currentPassword=input('Please input your password: ')
    
#checking if password is correct
for i in range (0,2):
    if currentPassword != loginss[userNumber][1]:
        currentPassword=input('Incorrect password. Try again: ')
        
#displaying entry message 
if currentPassword == loginss[userNumber][1]:
    print('Entry allowed. Let’s play!')
    import random
else:
    print('Incorrect password. Access denied')

#writing songs to the text file
songs=open('songs.txt', 'w')
songs.write('Sparkle and Shine - The Nativity Cast\n')
songs.write('Santa Baby - Ariana Grande\n')
songs.write('Merry Christmas Everyone - Shakin\' Stevens\n')
songs.write('I Saw Mommy Kissing Santa Claus - The Jackson 5\n')
songs.write('All I Want for Christmas is You - Mariah Carey\n')
songs.write('Maybe This Christmas - Ron Sexsmith\n')
songs.close()

#generating random number and song
songNumber = random.randint(0,5)
with open('songs.txt', 'r') as songs:
    songsList=(songs.readlines())
song=(songsList[songNumber])
songNames=['','','','','','','','','']
songInitials=[]
#creating song initials and artist variables
songName= ((song.split(" - ", 1))[0])
artistName = ((song.split(" - ", 1))[1])
songNames=(songName.split(" ",100))
for i in range (0,(len(songNames))):
    songInitials.append(songNames[i][0])
#printing the clues for guessing
print('The first letters of the song title are: ')
print(', '.join(songInitials))
print('And the song is by: ' +artistName)

#entering first guess
score =0
guess = input('Please input your guess: ')
if guess.lower() == ((' '.join(songNames)).lower()):
    print('Correct!')
    score = 2
else:
    guess = input('Incorrect. Please input next guess: ')

#entering second guess
if guess.lower() == ((' '.join(songNames)).lower()) and score != 2:
    print ('Correct!')
    score = 1
elif guess.lower() == ((' '.join(songNames)).lower()) and score != 2:
    print('Incorrect')

#printing score
print('Your score is ' + str(score))


#opening score file and determining whether the user is returning or new
with open('scores.txt', 'r') as scores:
    scores=(scores.readlines())
    length=len(scores)
    for x in range (0,length):
        if currentUser+'\n' == scores[x] and int(scores[x+1])<score:
            repeatPlayer='true'
            break
        elif currentUser+'\n' == scores[x] and int(scores[x+1])>=score:
            repeatPlayer = 'no'
            break
        else:
            repeatPlayer = 'false'

#adding/replacing the user's score into the list
if repeatPlayer=='false':
    scores.append(currentUser+'\n')
    scores.append(str(score)+'\n')
elif repeatPlayer == 'true':
    scores[x+1]=(str(score)+'\n')

#rewriting the list into the score file
length=len(scores)
with open('scores.txt', 'w') as newScores:
    for y in range (0,length):
        newScores.write(scores[y])
newScores.close()

#making a list with the user and their individual score combined
print('')
with open('scores.txt', 'r') as scores:
    scoresList=scores.readlines()
    for i in range (0,len(scoresList)):
        scoresList[i]=scoresList[i].strip()
list = []
for i in range(0, len(scoresList), 2):
    list.append(scoresList[i] + scoresList[i+1])

#making a list with only the scores in to find max    
values=[]
for i in range (0,len(list)):
        number=(list[i][-1])
        values.append(int(number))
max=max(values)+1

#function to find the right user for the top score
def highScore(list,max):
    people=[]
    for i in range (0,len(list)):
        if (list[i])[-1] ==str(max):
            people.append(list[i][:-1])
    return people, max

#calling the function 3 times to find the 3 top scores and their users
for i in range (0,3):
    max=max-1
    people, newMax=highScore(list,max)
    if newMax> 0 and max > 0 and people!= []:
        print('The number '+str(i+1)+' scorer(s) are: ')
        print(people)
        print('with a score of:')
        print(str(newMax))
    else:
        break
        


