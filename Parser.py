from Lexer import Token


class GrammarRule():    
    def __init__(self, name, tokenList):  
        self.name = name;
        self.tokenList = tokenList;
    
    def check(self, index, token):        
        if (index>=len(self.tokenList)):
            return False;
        elif(str(self.tokenList[index]) is str(token)):            
            return True;
        else:
            return False;
        
class Parser():
    def __init__(self):
        self.grammarRuleList = [];        
        
        self.grammarRuleList.append(  GrammarRule("ASSIGNMENT", [Token.KEYWORD,Token.IDENTIFIER,Token.ASSIGN, Token.STRING, Token.SEMICOLON]) ) ;
        self.grammarRuleList.append(  GrammarRule("DECLARATION", [Token.KEYWORD,Token.IDENTIFIER, Token.SEMICOLON]) ) ;
        self.grammarRuleList.append(  GrammarRule("DECLARATION", [Token.KEYWORD,Token.IDENTIFIER, Token.SEMICOLON]) ) ;
        self.grammarRuleList.append(  GrammarRule("DECLARATION", [Token.KEYWORD,Token.IDENTIFIER, Token.KEYWORD,Token.IDENTIFIER, Token.PARENLEFT, Token.PARENRIGHT, Token.CURLYL]) ) ;
        
        self.expressionList = [];
        
    
    def parseSymbolTable(self, lexemeList):          
        currentIndex = 0;
        currentRule = None;

        for symbol in lexemeList:            
            lexeme,line,col,token = symbol;
            
            #print(currentIndex, " ", token)
            
            if(token is str(Token.INVALID)):
                #Invalid Token Found
                print("Error: Invalid Token found at Line:" + str(line) + " Col:" + str(col) );
                return;            
            
            ruleMatch = 0;
            for rule in self.grammarRuleList:
                if(rule.check(currentIndex, token)):
                    currentRule = rule;
                    ruleMatch+=1;            
            
                
            if(ruleMatch==0 and currentRule is not None):
                #none of the rules match
                print("Error: Expecting Token: " + str(currentRule.tokenList[currentIndex]) + "at Line:" + str(line) + " Col:" + str(col));
                return;
            elif(currentRule is not None and currentIndex+1 == len(currentRule.tokenList)):
                #epression is found
                self.expressionList.append(currentRule);
                currentIndex = 0;
            else:
                currentIndex +=1;
                
        if(currentRule is None):
            print("Error: No");
        else:
            print("Success: Syntax Analysis Complete. Found "+len(self.expressionList)+" syntaxes.");