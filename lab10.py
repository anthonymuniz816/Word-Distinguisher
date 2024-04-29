#Anthony Muniz
#Program 10
#CS 101 Lab

#Problem: Need to develop a program that will take a user input and output the 10 most used words in the file inputted.

#ALGORITHM:
#START
#Create While loop
#Create empty list
#Ask user to input file name
#If user inputs incorrect file name ask again
#If user inputs correct file name go to try statement
#Open file and make all the words in the file into one big list
#Create for loop that will remove any periods, exclamation marks and commas if in the word
#Create for loop that will every word in the list into lower case
#Create for loop that removes any word in the list that is less than three characters long
#Create for loop that will add to the first list created in step 3
#Create for loop that orders the list from greatest to least
#Create for loop that counts the number of words that only appear once in the file
#Create for loop that counts the number of unique words in the file
#Create for loop that displays the 10 most used words in the file along with their frequency
#Print the number of words that apper only once in the file
#Print the number of unique words in the file
#END

while True:
    letter_num = []
    user_file = input('Enter the name of the file to open ')
    try:
        file = open(user_file)
        file_lines= file.read()
        file_lst = file_lines.split()
        
        for i in file_lst[:]:#Gets rid of any punctuation in the end
            if i[-1] == '.' or i[-1] == '!' or i[-1]==',':
                new=i.replace(i[-1],'')
                file_lst.remove(i)
                file_lst.append(new)
                
        for i in file_lst[:]: #Turns every word into lower case
            low=i.lower()
            file_lst.remove(i)
            file_lst.append(low)
            
        for i in file_lst[:]:#Removes any word less than 3 characters long
            if len(i) <= 3:
                file_lst.remove(i)

        
        for x in list(dict.fromkeys(file_lst)):#Adds the word and frequency to the letter_num list
             l=file_lst.count(x)
             letter_num.append([x,l])
             
        t = 0
        for i in range(0,len(letter_num)):#Sorts letter_num from greatest to least
            for j in range(i+1,len(letter_num)):
                if letter_num[i][1] < letter_num[j][1]:
                    t = letter_num[i]
                    letter_num[i] = letter_num[j]
                    letter_num[j] = t
                    
        num=0
        once=0
        unique = len(list(dict.fromkeys(file_lst)))
                   
        for x in list(dict.fromkeys(file_lst)): #Counts for the once variable
                t=file_lst.count(x)
                if t == 1:
                    once+=1
                    
        print('{:>2}{:>15}{:>22}'.format('#','Word','Freq.'))
        print('='*39)         
        while num <= 10: #Displays infromation
            for x in letter_num:
                num += 1
                if num<=10:
                    
                    print('{:>2}{:>15}{:>22}'.format(num,x[0],x[1]))
            
            break
        print()
        print('There are {} words that occcur only once'.format(once))
        print('There are {} unique words in the document'.format(unique))
        file.close()
        break
    
    except FileNotFoundError:
        print('Please Try again')
        




