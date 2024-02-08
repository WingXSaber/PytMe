
/*
Statement(){
	String grammar;
	Token TokenList[];
	int level;
}

int level
number of level is also the number of /t
 */
import java.util.List;

enum Token{
    IDENTIFIER,
    KEYWORD,
        
    RESERVEWORD,
    NOISEWORD, 
    COMMENT,          
    
    //   Delmiters:    
    BOXLEFT,   //   [
    BOXRIGHT,  //   ]
    
    PARENLEFT,   //   (
    PARENRIGHT,  //   )
    
    CURLYL,   //   {
    CURLYR,  //   }
    
    SEMICOLON(), //   ,
    
    //SINGLECOMMENTLEFT(), //   //
    //MULTICOMMENTLEFT(),  //   /*
    //MULTICOMMENTRIGHT(), //   */
    
    //   Arithmetic Operators
    ADD(),       //   +
    SUBTRACT(),  //   -
    MULTIPLY(),  //   *
    DIVIDE(),    //   /
    MODULO(),    //   %
    EXPONENT(),  //   **
    DIVFLOOR(),  //   /_
    
    //   Boolean Operators    
    GREAT(),           //   >
    LESS(),              //   <
    GREATQ(),      //   <=
    LESSEQ(),         //   >=
    NOTEQUAL(),          //   !=
    EQUAL(),      
    //   ==
    AND(),               //   &&
    OR(),                //   ||
    NOT(),               //   !
    
    //   Other Operators
    DOT(),               //   .
    
    //   Assignment Operators
    ASSIGN,        //   =
    ASSIGNADD(),     //   +=
    ASSIGNSUB(),     //   -=
    ASSIGNMULT(),    //   *=
    ASSIGNDIV(),     //   /=
    ASSIGNMOD(),     //   %=
    
    //   Unary Operators
    UNARYMINUS(),//   -
    INCREMENT(), //   ++
    DECREMENT(), //   --

    //   Constants
    STRING(),     //    PARTY(),           
    INTEGER,      //    POINT(), 
    FLOAT(),      //    FIGURE(),     
    BOOLEAN(),    //    TRUTH(), 
    CHAR(),       //    AVATAR(),      
     
    // newline
    NEWLINE(),  
        
    //   Not a valid Lexeme    
    INVALID(), 
}

public class GrammarRule{
    String name;
    Token [] tokenList;
         

    public GrammarRule(String name, Token[] tokenList){
        this.name = name;
        this.tokenList = tokenList;
    }

    public boolean checkToRule(Token [] input){        
        if(input.length <= tokenList.length){
            for(int x=0; x<input.length; x++){
                if(input[x]!=tokenList[x]) 
                    if(){
                        
                    }else
                        return false;   //not match
            }
            return true;  // match found
        }          
        return false;  //not match, bigger than rule
    }

    public abstract void check();

    public void showError(int inputIndex){
        System.out.println("Error (Line:"+lineNumber+"): Expecting "+tokenList[inputIndex]);
    }
}



public class Parser{
    

    //public Parser(){
        //define rules
        //put rules in a Grammar Rule Array
        //lexemeList = readSymbolTable()
        
    //}
    GrammarRule [] grammarRules = {    
                                    new GrammarRule("DEFINITION" , {Token.STRING , Token.IDENTIFIER, Token.ASSIGN, Token.INTEGER, Token.SEMICOLON} ),
                                    new GrammarRule("DEFINITION" , {Token.INTEGER, Token.IDENTIFIER, Token.ASSIGN, Token.INTEGER, Token.SEMICOLON} ),
                                    new GrammarRule("DEFINITION" , {Token.FLOAT  , Token.IDENTIFIER, Token.ASSIGN, Token.INTEGER, Token.SEMICOLON} ),
                                    new GrammarRule("DEFINITION" , {Token.BOOLEAN, Token.IDENTIFIER, Token.ASSIGN, Token.INTEGER, Token.SEMICOLON} ),
                                    new GrammarRule("DEFINITION" , {Token.CHAR   , Token.IDENTIFIER, Token.ASSIGN, Token.INTEGER, Token.SEMICOLON} ),
                                    new GrammarRule("DEFINITION" , {Token.STRING, Token.IDENTIFIER, Token.SEMICOLON} )
                                  };
    //readSymbolTable(){
    //}

    //run(){
        //GrammarRule.checkToRule(CurrentTokenList);
    //    List TokenList = <STRING>;



        //.append()
        //.remove()

        //loop through each symbols in lexemeList
        //check each rules defined
        //If one of the rules meet, valid
        //if none of the rules meet, get the most recent valid rule,
        //       then print the error/expected token/missing token
        //if all symbols are read, then print success and end program
    //}

    public static void main(String[]args){
        //Parser p = new Parser();
        //p.run();

        Token [] currentTokenStream = {Token.ASSIGN, Token.INTEGER, Token.SEMICOLON};
        //System.out.println(Token.ASSIGN);
        //for(int x=0; x<current.length; x++)
        //    System.out.println(current[x]);
        System.out.println(checkToRule(currentTokenStream));
        
    }   
    
    public static boolean checkToRule(Token [] input){        
        Token [] tokenList = {Token.ASSIGN, Token.INTEGER, Token.SEMICOLON};
        
        if(input.length <= tokenList.length){
            for(int x=0; x<input.length; x++){
                if(input[x]!=tokenList[x]) 
                    return false;   //not match
            }
        }          
        return true;  
    }
   
   
}