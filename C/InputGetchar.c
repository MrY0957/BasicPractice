#include<stdio.h>
void InputGetchar(){
    char charVal;
    unsigned char ucharVal;
    // newline skip করার জন্য
    printf("Enter two characters (back to back): \n"); 
    charVal = getchar(); 
    while(charVal == ' ' || charVal == '\n') { 
    charVal = getchar(); 
    }
    ucharVal = getchar();
    while(ucharVal == ' ' || ucharVal == '\n') { 
        ucharVal = getchar(); 
    }   
    printf("Character: %c\n", charVal);
    printf("Unsigned Character: %c\n", ucharVal);
    
}
int main (){
    
    printf("hello world!\n");
    
    InputGetchar();

    return 0;
}
