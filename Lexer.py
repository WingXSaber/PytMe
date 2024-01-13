from enum import Enum, auto;


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
    start = auto();
    stop = auto();   
                
                
    def __str__(self):
        """Function called if state is used as string such as in print()
        """
        return self.name;    
    
    
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
    RESERVEWORD = auto();
    NOISEWORD = auto(); #????????????????????
    COMMENT = auto();          
    
    #   Delmiters:    
    BRACKETLEFT = auto();
    BRACKETRIGHT = auto();
    
    PARENTHESISLEFT = auto();
    PARENTHESISRIGHT = auto();    
    
    SEMICOLON = auto();
    
    SINGLECOMMENTLEFT = auto();
    MULTCOMMENTLEFT = auto();
    MULTCOMMENTRIGHT = auto();    
    
    #   Arithmetic Operators
    ADD = auto();
    SUBTRACT = auto();
    MULTIPLY = auto();
    DIVIDE = auto();
    MODULO = auto();
    EXPONENT = auto();    
    #WHAT 7th?? = auto(); 
    
    #   Boolean Operators
    GREATER = auto();
    LESS = auto();
    EQUAL = auto();
    GREATEREQUAL = auto();
    LESSEQUAL = auto();
    
    #   Constants
#IS THIS RIGHT CHAT????????????????????????????????????????????????????????   
    AVATAR = auto(); #IS THIS RIGHT CHAT????????????????????????????????????????????????????????   
    FIGURE = auto();#IS THIS RIGHT CHAT????????????????????????????????????????????????????????   
    FLOAT = auto();
    BOOLEAN = auto();
    CHAR = auto();
    
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

class Lexer:
    """The Lexical Analyzer class.
    
    Attributes:
        state : the current State
        symbolTable [] : list containing all lexemes detected. 
    """
    
    #Constructor
    def __init__(self):        
        self.state = State.start;
        self.symbolTable = [];        
    
    def loadFile(self, address):
        """
        if(addressNotValid == True):
            raise NotADirectoryError
        if(FILENOTFOUND == True):    
            raise FileNotFoundError
        if(FILENOTSPYC == true):
            raise TypeError;
            """
        pass
        
    print("RUNNING THE LEXER");
    

test = Lexer();
print(test.state)
print(test.symbolTable);

    
    