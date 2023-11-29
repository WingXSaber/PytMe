import sys

print(sys.argv);

#To Do:
#comments
#single line comment //     /n
#multi line comment  /*      */

#dot operator
# example: class.object.variable = 'class', '.', 'object', '.', 'variable'

#dot but decimal points: 
#  0.623
#  .07

#escape string character
#signed numeric / negative values

#bugs:
# +b
#0..5

#illegal characters
# example ~
# basically anything that is not detected
# cha

#multiline/text file input
#   line number count
#   use args as getter for txtfile address
#   example python Main.py path/to/file/txtfile.txt

#output in a text file
#    bascially put the print into a text file as well
#    Format: 
#    TOKEN/t/tLINE/t/tLEXEME
#    TOKEN/t/tLINE/t/tLEXEME
#       
#    TOKEN      LINE    LEXEME   
#    SEMICOLON  1       ;              
#


a = +-1;
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
    
    isNumeric = False; #flag used to mark if we are detecting number (assuming we didnt detect letter before)
    isDecimal = False;
    
    isCommentSingle = False;   #flag used to mark if we are detecting a single-line comment
    isCommentMultiple = False; #flag used to mark if we are detecting a multi-line comment
    
    print("char\tlexeme\tlexemeList");
    
    #we use char as the current character in the text we iterate over
    
    operatorList = ["+","-","*","/","%", ">","<","!"];
    
    for char in inputText:  
        print(char +"\t", end = "");
        
        if(isString):                                            #if String literal
            lexeme = lexeme + char            
            #check also for escape characters
            if((isSingleQuote and char == "\'") or (isDoubleQuote and char == "\"")):
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme
                isString      = False
                isSingleQuote = False
                isDoubleQuote = False
        elif(isNumeric):                                        #if char is integer or float literal
            #if numeric, or if decimal point (only once)            
            if( char.isnumeric() or (char == "." and not isDecimal)):   
                lexeme = lexeme + char
            else:
                isNumeric = False
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme
                lexeme = lexeme + char
                        
        elif(char.isspace()):                                   #if char is whitespace
            if(len(lexeme)>0):  #true means the end of a lexeme
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme
            #else means nothing to append    
                                    
        elif(char.isalpha()):                                   #if char is letter  
            lexeme = lexeme + char
        elif(char.isnumeric()):                                 #if char is  number               
            if(lexeme.isnumeric() or lexeme == "."):
                isNumeric = True;         
            elif(len(lexeme)>0):  #true means the end of a lexeme
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""            
            lexeme = lexeme + char   
            
        elif(char=="."):                                        #if char is dot            
            if(lexeme.isnumeric()):
                isNumeric = True;    
            elif(len(lexeme)>0): #true means the end of a lexeme 
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme   
            lexeme = lexeme + char     
                  
        elif(char in operatorList):                             #if char is operator 
            if(len(lexeme)>0):  #true means the end of a lexeme
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme
            lexeme = lexeme + char   
        elif(char == "="):                                      #if char is assignment operator              
            if(lexeme in operatorList or lexeme == "="): 
                #if combination i.e. +=, <=, ==
                lexeme = lexeme + char;
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme
            else:                                       
                #if just equals
                if(len(lexeme)>0):  #true means the end of a lexeme
                    lexemeList.append(lexeme) #add the lexeme to list
                    lexeme = ""               #clear lexeme
                lexeme = lexeme + char    
        elif(char in ["&", "|"]):                               #if char is  relational operators AND and OR
            if(char == lexeme):   #true means it's && or ||
                lexeme = lexeme + char                            
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme                           
            elif(len(lexeme)>0):  #true means the end of a lexeme
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme                           
                lexeme = lexeme + char                            
            else:
                lexeme = lexeme + char                     
        elif(char == "\'" or char == "\""):                     #if char is string literal            
            if(len(lexeme)>0):  #true means the end of a lexeme
                lexemeList.append(lexeme) #add the lexeme to list
                lexeme = ""               #clear lexeme 
            lexeme = lexeme + char                           
            if(char == "\'"):   #is single quote string  
                isString = True
                isSingleQuote = True
            else: #char == "\"" #is double quote string
                isString = True
                isDoubleQuote = True                
                             
        else:                                                   #if char is anything else
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


def identify_tokens_from(lexemeList):
    tokenList = []    
    return tokenList;
    

def main():
    print("Enter syntax:");
    inputText = input();
    
    lexemeList = split_into_lexemes(inputText);
    #print(lexemeList);
    
    #for i in range(0, len(lexemeList), i):
        
    print("\nLEXEMES:\n-----------------------------");
    for a in lexemeList:
        print("-> "+a);
        
    print("Lexeme Count: "+str(len(lexemeList)));
        

main();






