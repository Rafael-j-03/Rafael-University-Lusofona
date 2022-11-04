lorem = open('lorem.txt' , 'r') #Read lorem.txt

loremIpsum = open('loremIpsum.txt', 'w') #Create loremIpsum.txt and use it for writing

loremLines = lorem.readlines() #Read all lorem.txt file

loremIpsum.writelines(loremLines) #Write the text from lorem.txt to loremIpsum.txt

print('You have copy lorem.txt to loremIpsum.txt!') #Warning message