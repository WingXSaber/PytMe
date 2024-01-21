import sys;
import os;
from Lexer import Lexer;

print(sys.argv);
dir_path = os.path.dirname(os.path.realpath(__file__));  #Initialize path of the system

def loadFile(address):              
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
            #print(lines);
            #print(type(lines));            
            #for line in lines:
            #    print(line, end = "");
            lexer = Lexer();
            lexer.processText(lines);
            
       
        #Lexer.processtext(self, inputText):    
        
        
loadFile("myfile.txt");