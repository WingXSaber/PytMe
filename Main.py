


def split_into_lexemes(inputText):
    inputText = inputText.lstrip();  #Remove Whitespaces at start and end
    print(inputText);
    
    lexemeList = [];
    
    index = 0;
    lexeme = "";
    
    for char in inputText:
        if(char.isspace()):         #IF whitespace            
            if(len(lexeme)>0):      #If lexeme contains anything
                lexemeList.append(lexeme)
                lexeme = ""            
        elif(char.isalpha()):
            lexeme = lexeme + char
        elif(char.isnumeric() and len(lexeme)>0):  
            lexeme = lexeme + char        
        elif(char in ["+","-","*","/","%"]):
            if(len(lexeme)>0):  
                lexemeList.append(lexeme)
                lexeme = ""
            lexeme = lexeme + char
        elif(char == "=" and lexeme in ["+","-","*","/","%"]):
            lexeme = lexeme + char
            lexemeList.append(lexeme)
            lexeme = ""
        else:
            if(len(lexeme)>0):  
                lexemeList.append(lexeme)
                lexeme = ""
            else:
                lexemeList.append(char)                                         
        
        
        index+=1;
    
    if(len(lexeme)>0):      #If lexeme contains anything
        lexemeList.append(lexeme);
    
    return lexemeList;

def main():
    print("Enter syntax:");
    inputText = input();    
    #print(inputText);
    
    lexemeList = split_into_lexemes(inputText);
    print(lexemeList);

main();






