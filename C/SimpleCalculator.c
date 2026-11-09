#include<stdio.h>

int main(){
    int a,b;
    printf("Simple CalCulator Project\nEnter Two Numbers: "); 
    scanf("%d \n %d",&a,&b);
    //program
  
        if(a>b || a<b){
      //Addition
      int sum=a+b;
    //Multiplication
      int mul=a*b;
      printf("sum=%d\nmultiplication=%d\n", sum,mul);
    //Subtraction
      int dif=a-b;
    //division
      float div=(float)a/(float)b;
      printf("difference=%d\ndivision=%0.2f\n", dif, div);
    }
    return 0;
}
