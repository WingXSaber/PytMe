


def split_into_lexemes(inputText):
    inputText = inputText.lstrip();  #Remove Whitespaces at start
    inputText = inputText.rstrip();  #Remove Whitespaces at end
    print(inputText);
    
    lexemeList = [];    #contains all the lexemes detected
    lexeme = "";        #current lexeme storage, gets cleared every succesful detection
    index = 0;          #used for the loop    
    
    #we use char as the current character in the text we iterate over
    for char in inputText:  
        if(char.isspace()):                                     #if whitespace
            if(len(lexeme)>0):  #true means the end of a lexeme
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme
            #else means nothing to append
        elif(char.isalpha()):                                   #if letter
            lexeme = lexeme + char
        elif(char.isnumeric() and len(lexeme)>0):               #if whitespace
            lexeme = lexeme + char        
        elif(char in ["+","-","*","/","%"]):                    #if operator
            if(len(lexeme)>0):  #true means the end of a lexeme
                lexemeList.append(lexeme)#add the lexeme to list
                lexeme = ""              #clear lexeme
            lexeme = lexeme + char
        elif(char == "=" and lexeme in ["+","-","*","/","%"]):  #if assignment operator ie. += , *=
            lexeme = lexeme + char
            lexemeList.append(lexeme)   #add the lexeme to list
            lexeme = ""                 #clear lexeme
        else:                                                   #if anything else
            if(len(lexeme)>0): #true means the end of a lexeme 
                lexemeList.append(lexeme)   #add the lexeme to list
                lexeme = ""                 #clear lexeme
            else:              #if it's single char lexeme
                lexemeList.append(char)      
        index+=1;   #loop iteration
        #end of loop
    
    if(len(lexeme)>0):   #If lexeme still contains anything after the loops
        lexemeList.append(lexeme);
    
    return lexemeList;



def main():
    print("Enter syntax:");
    inputText = input();
    
    lexemeList = split_into_lexemes(inputText);
    print(lexemeList);

main();






