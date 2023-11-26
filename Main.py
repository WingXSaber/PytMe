


def split_into_tokens(inputText):
    tokenList = inputText.split()
    return tokenList;

def main():
    print("Enter syntax:");
    inputText = input();
    
    print(inputText);
    tokenList = split_into_tokens(inputText);
    print(tokenList);

main();






