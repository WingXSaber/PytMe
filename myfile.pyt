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