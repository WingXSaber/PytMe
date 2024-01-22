from enum import Enum, auto;

       
class Token(Enum):
    """An enum class for defining Tokens and accessed through its attributes. 
    
    It is accessed as:  Token.<token name>
    
    Returns:
        __str__: name of token.
    """
        
    #Token type List:
    #   Format: <State Name> = auto()     
    #   Legend:
    #      <State Name> = name of state
    #      auto()       = built in function of enum used for auto-count instead
    #                     of manually defining each state attribute by counting.
    IDENTIFIER = auto();
    KEYWORD = auto();
        #NEED BA NA IDENTIFY ANONG KEYWORD
    RESERVEWORD = auto();
    NOISEWORD = auto(); #????????????????????
    COMMENT = auto();          
    
    #   Delmiters:    
    BRACKETLEFT = auto();   #   {
    BRACKETRIGHT = auto();  #   }
    
    PARENTHESISLEFT = auto();   #   (
    PARENTHESISRIGHT = auto();  #   )
    
    SEMICOLON = auto(); #   ;
    
    SINGLECOMMENTLEFT = auto(); #   //
    MULTICOMMENTLEFT = auto();  #   /*
    MULTICOMMENTRIGHT = auto(); #   */
    
    #   Arithmetic Operators
    ADD = auto();       #   +
    SUBTRACT = auto();  #   -
    MULTIPLY = auto();  #   *
    DIVIDE = auto();    #   /
    MODULO = auto();    #   %
    EXPONENT = auto();  #   **
    DIVFLOOR = auto();  #   /_
    
    #   Boolean Operators    
    GREATER = auto();           #   >
    LESS = auto();              #   <
    GREATEREQUAL = auto();      #   <=
    LESSEQUAL = auto();         #   >=
    NOTEQUAL = auto();          #   !=
    EQUAL = auto();             #   ==
    AND = auto();               #   &&
    OR = auto();                #   ||
    NOT = auto();               #   !
    
    #   Other Operators
    DOT = auto();               #   .
    
    #   Assignment Operators
    ASSIGN = auto();            #   =
    ASSIGNADD = auto();         #   +=
    ASSIGNSUBTRACT = auto();    #   -=
    ASSIGNMULTIPLY = auto();    #   *=
    ASSIGNDIVIDE = auto();      #   /=
    ASSIGNMODULO = auto();      #   %=
    
    #   Unary Operators
    UNARYMINUS = auto();#   -
    INCREMENT = auto(); #   ++
    DECREMENT = auto(); #   --

    #   Constants
    STRING = auto();    #????????????????????????????????????????????????????????   
    FIGURE = auto();
    FLOAT = auto();
    BOOLEAN = auto();
    AVATAR = auto(); 
        
    #   Not a valid Lexeme    
    INVALID = auto(); 
        
                
    def __str__(self):
        """Function called if state is used as string such as in print()
        """
        return self.name;    
    
    
class lexeme:
    """A lexeme instance.
    
    Args:
         value (str): the instance/value of this lexeme
         token (Token): the oken type
         lineNumber (int): row / y-coordinate 
         columnNumber (int): column / x-coordinate
    """    
    
    #Constructor
    def __init__(self, value: str, token: Token, lineNumber: int, columnNumber: int):        
        self.value = value;
        self.token = token;
        self.lineNumber = lineNumber;
        self.columnNumber = columnNumber;
    
    def __str__(self):
        """Function called if state is used as string such as in print()
        """        
        return (str(self.token)
                +" \t"+str(self.lineNumber)
                +"\t"+str(self.columnNumber)
                +"\t"+str(self.value)
               );  


class State(Enum):
    """An enum class for defining States and accessed through its attributes.
    
    It is accessed as:  State.<state name>
    
    Each state has a unique set of actions and transitions given the conditions. 
    
    Returns:
        __str__: name of state.
    """
        
    #State type List:
    #   Format: <State Name> = auto()     
    #   Legend:
    #      <State Name> = name of state
    #      auto()       = built in function of enum used for auto-count instead
    #                     of manually defining each state attribute by counting.
    initialized = auto(); 
    activated = auto(); 
    
    character = auto();
    string = auto();   
    number = auto();
    float = auto();
    comment = auto();
    space = auto();
    operator = auto();
    logicalOperator = auto();
    semicolon = auto();
    stringLiteral = auto();
    
    curly = auto();
    bracket = auto();
    boxBracket = auto();
    
    endOfLine = auto();
    endOfFile = auto();
    processed = auto();
                
                
    def __str__(self):
        """Function called if state is used as string such as in print()
        """
        return self.name;    


class Lexer():
    """The Lexical Analyzer class.
    
    Attributes:
        state : the current State
        symbolTable [] : list containing all lexemes detected. 
    """
    
    #Constructor
    def __init__(self):        
        self.state = State.initialized;
        self.symbolTable = []; 
        self.lineNumber = 0;       
        
       #TODO
        self.keywordList = ["supreme","synchronized","this","toggle ","twin","unarmed","unstable","while"]
    
    def checkToken(self, lexeme):
        #state
        return "token";
                   
    def processText(self, inputText):
        #TODO check if inputText is valid ===================
                        
        operatorList = ["+","-","*","/","%",  ">","<","!",   "=","."];
        logicalOpList = ["&", "|", "!"];
        
        lexemeList = [];        
        lexeme = "";
        
        print(inputText);
        while(self.state != State.endOfFile):
            inputLine = inputText[self.lineNumber];                                    
                                    
            colNumber = 0;
            
            #For multi-line
            if(self.state == State.endOfLine):
                self.state = State.comment;
                if(lexeme == ""):  #comment has ended
                    self.state = State.character;                                        
            else:
                self.state = State.character;                                    
            
            while(self.state != State.endOfLine):
                charCurrent = inputLine[colNumber];                 
                
                #Display Debug                             
                if(charCurrent == '\n'):
                    print('\\n'+" col: "+str(colNumber)+" - Lexeme:"+repr(lexeme)+"  linelen:"+str(len(inputLine)), end = "") #TODO
                else:
                    print(charCurrent+" col: "+str(colNumber)+" - Lexeme:"+repr(lexeme)+"  linelen:"+str(len(inputLine)), end = "") #TODO                
                
               
                if(self.state == State.space): 
                    if(charCurrent in operatorList):                                                
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.operator;
                    elif(charCurrent in logicalOpList):                                                
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.logicalOperator;                         
                    elif(charCurrent.isnumeric()):
                        lexeme = lexeme + charCurrent;
                        self.state = State.number; 
                    elif(not charCurrent.isspace()):
                        lexeme = lexeme + charCurrent;
                        self.state = State.character;                    
                    else:
                        pass; #do nothing if space
                    
                elif(self.state == State.semicolon):
                    lexemeList.append(lexeme) #add the lexeme to list
                    lexeme = ""               #clear lexeme
                    lexeme = lexeme + charCurrent;
                    if(charCurrent in operatorList):                                                
                        self.state = State.operator;
                    elif(charCurrent in logicalOpList):                                                
                        self.state = State.logicalOperator;                         
                    elif(charCurrent.isnumeric()):
                        self.state = State.number; 
                    elif(charCurrent.isspace()):
                        self.state = State.space;   
                    else:
                        self.state = State.character;   
                        
                elif(self.state == State.curly):
                    lexemeList.append(lexeme) #add the lexeme to list
                    lexeme = ""               #clear lexeme
                    lexeme = lexeme + charCurrent;
                    if(charCurrent in operatorList):                                                
                        self.state = State.operator;
                    elif(charCurrent in logicalOpList):                                                
                        self.state = State.logicalOperator;                         
                    elif(charCurrent.isnumeric()):
                        self.state = State.number; 
                    elif(charCurrent.isspace()):
                        self.state = State.space;   
                    else:
                        self.state = State.character; 
                        
                elif(self.state == State.bracket):
                    lexemeList.append(lexeme) #add the lexeme to list
                    lexeme = ""               #clear lexeme
                    lexeme = lexeme + charCurrent;
                    if(charCurrent in operatorList):                                                
                        self.state = State.operator;
                    elif(charCurrent in logicalOpList):                                                
                        self.state = State.logicalOperator;                         
                    elif(charCurrent.isnumeric()):
                        self.state = State.number; 
                    elif(charCurrent.isspace()):
                        self.state = State.space;   
                    else:
                        self.state = State.character; 
                
                elif(self.state == State.boxBracket):
                    lexemeList.append(lexeme) #add the lexeme to list
                    lexeme = ""               #clear lexeme
                    lexeme = lexeme + charCurrent;
                    if(charCurrent in operatorList):                                                
                        self.state = State.operator;
                    elif(charCurrent in logicalOpList):                                                
                        self.state = State.logicalOperator;                         
                    elif(charCurrent.isnumeric()):
                        self.state = State.number; 
                    elif(charCurrent.isspace()):
                        self.state = State.space;   
                    else:
                        self.state = State.character;         
                    
                elif(self.state == State.string):
                    #identifier
                    #keyword
                    #noiseword                    
                    if(charCurrent.isalpha() or charCurrent.isnumeric() ):                        
                        lexeme = lexeme + charCurrent;
                    elif(charCurrent.isspace()):
                        lexemeList.append(lexeme) #add the lexeme to list
                        lexeme = ""               #clear lexeme                        
                        self.state = State.space;
                    elif(charCurrent in operatorList):                                                
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.operator;
                    elif(charCurrent in logicalOpList):                                                
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.logicalOperator; 
                    else:                        
                        if(len(lexeme)>0): #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme                        
                        lexeme = lexeme + charCurrent;                        
                        self.state = State.character;                    

                elif(self.state == State.number):                      
                    if(charCurrent.isnumeric()):
                        lexeme = lexeme + charCurrent;
                    elif(charCurrent == "."):   
                        lexeme = lexeme + charCurrent;                           
                        self.state = State.float;    
                    elif(charCurrent in operatorList):                                                
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.operator;
                    elif(charCurrent in logicalOpList):                                                
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.logicalOperator;                      
                    else:                             
                        lexemeList.append(lexeme) #add the lexeme to list
                        lexeme = ""               #clear lexeme                        
                        self.state = State.character;
                        
                elif(self.state == State.float):
                    if(charCurrent.isnumeric()):
                        lexeme = lexeme + charCurrent;
                    elif(charCurrent in operatorList):                                                
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.operator;
                    elif(charCurrent in logicalOpList):                                                
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.logicalOperator;    
                    else:                             
                        lexemeList.append(lexeme) #add the lexeme to list
                        lexeme = ""               #clear lexeme                        
                        self.state = State.character;
                        
                        
                elif(self.state == State.stringLiteral):
                    #escape character                    
                    if(lexeme[0] == '"' or lexeme[0] == "'"):   #if start is ' or "
                        lexeme = lexeme + charCurrent;
                    if(lexeme[0] == lexeme[-1]):                #if end
                        print("TRACER ROUND")
                        lexemeList.append(lexeme) #add the lexeme to list
                        lexeme = ""               #clear lexeme                        
                        self.state = State.character;
                       
                
                elif(self.state == State.comment):                    
                    if(lexeme[0]+lexeme[1] == "//"):    #if single comment
                        if(charCurrent != '\n'):    #if comment is not yet ending
                            lexeme = lexeme + charCurrent;
                        else:                       #Comment has ended
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme                        
                            self.state = State.character;
                            
                    elif(lexeme[0]+lexeme[1] == "/*"):  #if multiline comment
                        if(lexeme[-2]+lexeme[-1] == "*/"):  #comment has ended
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme                        
                            self.state = State.character;
                        else:
                            lexeme = lexeme + charCurrent;                            
                    
                
                elif(self.state == State.operator):
                    #dot operator
                    if(lexeme in ["+", "-", "*","/", "%"]):
                        if(charCurrent == "/" or charCurrent == "*"):
                            lexeme = lexeme + charCurrent;      
                            self.state = State.comment;
                        else:
                            if(charCurrent == "=" or lexeme == '/' and charCurrent == "_" ):
                                lexeme = lexeme + charCurrent;      
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                            self.state = State.character;                          
                            
                    elif(charCurrent == "."): #if new operator
                        lexemeList.append(lexeme) #add the lexeme to list
                        lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;      
                        #dot operator 
                        self.state = State.operator
                        
                    elif(lexeme == '.'and charCurrent.isnumeric()):
                        lexeme = lexeme + charCurrent;       
                        self.state = State.float;
                    elif(charCurrent.isspace()):
                        lexemeList.append(lexeme) #add the lexeme to list
                        lexeme = ""               #clear lexeme                        
                        self.state = State.space;
                    elif(len(lexeme)>0):  #true means the end of a lexeme
                        lexemeList.append(lexeme) #add the lexeme to list
                        lexeme = ""               #clear lexeme
                        self.state = State.character;    
                        
                        
                elif(self.state == State.logicalOperator):   
                    if(lexeme == "!"):
                        lexemeList.append(lexeme) #add the lexeme to list
                        lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;   
                    elif(charCurrent == lexeme):
                        lexeme = lexeme + charCurrent;   
                        lexemeList.append(lexeme) #add the lexeme to list
                        lexeme = ""               #clear lexeme
                    elif(charCurrent in operatorList):                                                
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.operator; 
                    else:
                        lexemeList.append(lexeme) #add the lexeme to list
                        lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;   
                    self.state = State.character;    
                        
                
                elif(self.state == State.character):                                         
                    if(lexeme == "'" or lexeme == '"' or charCurrent == "'" or charCurrent == '"'):                        
                        if(len(lexeme)>0 and not(lexeme == "'" or lexeme == '"')):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.stringLiteral;
                        
                    elif(charCurrent == ";"):
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.semicolon;
                        
                    elif(charCurrent == "{" or charCurrent == "}"):
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.curly;
                        
                    elif(charCurrent == "(" or charCurrent == ")"):
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.bracket;
                        
                    elif(charCurrent == "[" or charCurrent == "]"):
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.boxBracket;
                        
                    elif(charCurrent in operatorList):                                                
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.operator;

                    elif(charCurrent in logicalOpList):
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme
                        lexeme = lexeme + charCurrent;
                        self.state = State.logicalOperator;
                        
                    elif(charCurrent.isnumeric()):    #if char is  number                        
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme                                                         
                        lexeme = lexeme + charCurrent;                         
                        self.state = State.number;        
                        
                    elif(charCurrent.isalpha()):
                        lexeme = lexeme + charCurrent;
                        if(lexeme.isalpha()):
                            self.state = State.string;                                                        
                            
                    elif(charCurrent.isspace()):                              
                        if(len(lexeme)>0):  #true means the end of a lexeme
                            lexemeList.append(lexeme) #add the lexeme to list
                            lexeme = ""               #clear lexeme                            
                        #else means nothing to append    
                        self.state = State.space;
                        
                    else:
                        lexeme = lexeme + charCurrent; 
                 
                #if(charCurrent == '\n'):
                if(colNumber+1 >= len(inputLine)):
                    if(self.state == State.comment and lexeme[0]+lexeme[1] == "/*"):   #Multiline Comment
                        pass;                        
                    elif(len(lexeme)>0):  #true means the end of a lexeme
                        lexemeList.append(lexeme) #add the lexeme to list
                        lexeme = ""               #clear lexeme                            
                    self.state = State.endOfLine;
                     
                colNumber+=1;
                
                print(" ", self.state);
                #if (text in self.keywordList):
                #    token = KEYWORD.                
            
            
            if(self.lineNumber+1 >= len(inputText)):   
                self.state = State.endOfFile
            else:
                self.lineNumber+=1;   
            
            
        #print(inputText )
        for i in inputText:
            print(i, end="");
        print(lexemeList);
        self.state = State.activated;
    
        
    def show(self):        
        if(self.symbolTable == []): #if symbolTable is empty
            print("No symbols found.");
        else:           
            print("============== SYMBOL TABLE =================================");
            #add condition here 
            # if comment, convert all \n to \\n
            print("Token     "
                        +" \t"+"Line #"
                        +"\t"+"Col #"
                        +"\t"+"Lexeme"
                        );  
            print("-------------------------------------------------------------");
            for symbol in self.symbolTable:
                print(symbol);
        #return textSymbolTablem    
    

#test = Lexer();
#test.loadFile('myfile.txt');

#lex = lexeme(">", Token.GREATER, 0,0);
##print(lex)
#
#test.symbolTable.append(lex);
#test.show()

#test.processText();