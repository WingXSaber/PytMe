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
    #WHAT 7th?? = auto(); 
    
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
    identifier = auto();   
    number = auto();
    comment = auto();
    
    endOfLine = auto();
    endOfFile = auto();
    processed = auto();
                
                
    def __str__(self):
        """Function called if state is used as string such as in print()
        """
        return self.name;    


class Lexer:
    """The Lexical Analyzer class.
    
    Attributes:
        state : the current State
        symbolTable [] : list containing all lexemes detected. 
    """
    
    #Constructor
    def __init__(self):        
        self.state = State.initialized;
        self.symbolTable = []; 
        self.lineNumber = -1;       
        
        self.operatorList = ["+","-","*","/","%", ">","<","!"];
        self.keywordList = ["supreme","synchronized","this","toggle ","twin","unarmed","unstable","while"]
        
        
    
    def loadFile(self, address):              
        """
        if(addressNotValid == True):
            raise NotADirectoryError
        if(FILENOTFOUND == True):    
            raise FileNotFoundError
        if(FILENOTSPYC == true):
            raise TypeError;
        """                    
              
        with open(address, 'r') as myfile:
            lines = myfile.readlines()
            for line in lines:
                print(line, end = "");
       
        #processtext(self, inputText):        
    
               
    def processText(self, inputText):
        self.state = State.character;
        inputLine = inputText;
        self.lineNumber+=1;
        
        charIndex = 0;  #colNumber = 0;        
        while(self.state != State.endOfFile):
            charCurrent = inputLine[charIndex];
            
            print(charCurrent);
                
            charIndex+=1;
            self.state = State.endOfFile
            
            #if (text in self.keywordList):
            #    token = KEYWORD.
            
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
    
    print("RUNNING THE LEXER");
    

test = Lexer();
#test.loadFile('myfile.txt');

lex = lexeme(">", Token.GREATER, 0,0);
#print(lex)

test.symbolTable.append(lex);
test.show()

