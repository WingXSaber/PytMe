
point x; 
<Declaration>
<KEYWORD> <IDENTIFIER> <SEMICOL>

point x = 10;
<ASSIGNMENT>
<COMMENT>
<INVALID> Either invalid token, or invalid rule


Rules = []
RulesCheckList = []

for x in len(Rules):
    Rule = Rules[x];
    for subRule in len(Rule):
        if(sub

RulesCheckList  1          1            1           1           1
RULES[x]        <KEYWORD> <IDENTIFIER> <ASSIGN>     <INTEGER>   <SEMICOL>
                                                                ^ - end of line or len(RULE) -1
                                                                Once in end of line, then  
                                                                check if all in checklist are true.
                                                                If all true, then stop
                                                                
RulesCheckList  


1           1           0
<KEYWORD> <IDENTIFIER> <SEMICOL>

0            0          0           0
<IDENTIFIER> <ASSIGN> <INTEGER> <SEMICOL>






plaza static abyss message(){
    display("Hello World");
}

plaza static abyss sum( point a , point b){
    display( 'Sum of' + a + 'and + b +' + '+ a+b' );
}

plaza point max(point x, point y) {
    if (x > y) {
        dispatch x;
    } else {
        dispatch y;
    }
}

message();
sum(1, 3);
display(max(10, 20));