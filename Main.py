
#To Do:
#&&
#==
#||    

#Number
#float number

def split_into_lexemes(inputText):
    inputText = inputText.lstrip();  #Remove Whitespaces at start
    inputText = inputText.rstrip();  #Remove Whitespaces at end
    print(inputText);
    
    lexemeList = [];    #contains all the lexemes detected
    lexeme = "";        #current lexeme storage, gets cleared every succesful detection
    index = 0;          #used for the loop    
    
    isString = False;  #flag used to mark if we are detecting a string value i.e: "value" or 'value'
    isSingleQuote = False;  #if detected string is started with '
    isDoubleQuote = False;  #if detected string is started with "
    
    isNumeric
    
    isCommentSingle = False;   #flag used to mark if we are detecting a single-line comment
    isCommentMultiple = False; #flag used to mark if we are detecting a multi-line comment
    
    print("char\tlexeme\tlexemeList");
    
    #we use char as the current character in the text we iterate over
    for char in inputText:  
        print(char +"\t", end = "");
        
        if(isString):
            lexeme = lexeme + char
            #check also for escape characters
            if((isSingleQuote and char == "\'") or (isDoubleQuote and char == "\"")):
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme
                isString      = False;
                isSingleQuote = False;
                isDoubleQuote = False;
            
        elif(char.isspace()):                                     #if whitespace
            if(len(lexeme)>0):  #true means the end of a lexeme
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme
            #else means nothing to append
        elif(char.isalpha()):                                   #if letter  
            lexeme = lexeme + char
        elif(char.isnumeric() and len(lexeme)>0):               #if whitespace
            lexeme = lexeme + char        
        elif(char in ["+","-","*","/","%",  ">","<","!"] or char == "=" != lexeme):   #if operator or equal operator
            if(len(lexeme)>0):  #true means the end of a lexeme
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme
            lexeme = lexeme + char
        elif(char == "=" and lexeme in ["+","-","*","/","%",  ">","<","!","="]):  #if operator that is followed by equals ie. += , *=
            lexeme = lexeme + char
            lexemeList.append(lexeme) #add the lexeme to list
            lexeme = ""               #clear lexeme       
        elif(char == "\'" or char == "\""):                     #if string / left quote
            if(len(lexeme)>0):  #true means the end of a lexeme
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""  
            lexeme = lexeme + char                           
            if(char == "\'"):          
                isString = True
                isSingleQuote = True
            else: #char == "\""
                isString = True
                isDoubleQuote = True            
        else:                                                   #if anything else
            if(len(lexeme)>0): #true means the end of a lexeme 
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme                          
            lexemeList.append(char)                      #####inspired by Sean's ask of printf("Yawn");###########
            
        print(lexeme+"\t", end="");
        print(lexemeList);
        index+=1;   #loop iteration
        #end of loop
    
    if(len(lexeme)>0):   #If lexeme still contains anything after the loops
        lexemeList.append(lexeme);
    
    #return lexemeList, tokenList;
    return lexemeList; 



def main():
    print("Enter syntax:");
    inputText = input();
    
    lexemeList = split_into_lexemes(inputText);
    #print(lexemeList);
    
    #for i in range(0, len(lexemeList), i):
        
    print("\nLEXEMES:");
    for a in lexemeList:
        print(a);
        
    print("Lexeme Count: "+str(len(lexemeList)));
        

main();






