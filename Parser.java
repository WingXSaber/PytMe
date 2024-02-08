

/*




Statement(){
	String grammar;
	Token TokenList[];
	int level;
}

int level
number of level is also the number of /t




 */

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
    INTEGER,    //    POINT(), 
    FLOAT(),      //    FIGURE(),     
    BOOLEAN(),    //    TRUTH(), 
    CHAR(),       //    AVATAR(),      
     
    // newline
    NEWLINE(),  
        
    //   Not a valid Lexeme    
    INVALID(), 
}

public abstract class GrammarRule{
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
        lineNumber = 0;
        System.out.println("Error (Line:"+lineNumber+"): Expecting "+tokenList[tokenList]);
    }
}

public class Parser{
    

    //public Parser(){
        
    //}

    //readSymbolTable(){
    //}

    public static void main(String[]args){
        Token [] current = {Token.ASSIGN, Token.INTEGER, Token.ASSIGN};
        System.out.println(Token.ASSIGN);
        for(int x=0; x<current.length; x++)
            System.out.println(current[x]);
        System.out.println(checkToRule(current));
        
    }   
    
    public static boolean checkToRule(Token [] input){        
        Token [] tokenList = {Token.ASSIGN, Token.INTEGER, Token.SEMICOLON};
        
        if(input.length <= tokenList.length){
            for(int x=0; x<input.length; x++){
                if(input[x]!=tokenList[x]) 
                    return false;   //not match
            }
            System.out.println("AA");
        }          
        return true;  
    }
   
   
}