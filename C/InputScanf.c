#include<stdio.h>

void InputScanf(){
    char charVal;
    unsigned char ucharVal;
    printf("Enter a character and Unsigned character using scanf(): \n");
    scanf("%c %c",&charVal, &ucharVal); // space দিলে newline skip হয়
    printf("Single Character: %c and another: %c \n\n",charVal,ucharVal); // for character data type-> %c
}
int main (){
    
    printf("hello world!\n");
    
    InputScanf();
    return 0;
}
