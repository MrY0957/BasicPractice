#include <stdio.h>
#include <math.h> 

int main() {
    double x, y, root, inv, power,maxVal,minVal;
int choice;
    printf("Choose an option:\n"); 
    printf("1. Square Root\n"); 
    printf("2. Power (x^y)\n"); 
    printf("3. Inverse (1/x)\n"); 
    printf("4. Max & Min\n"); 
    printf("Enter your choice (1-4): ");
    scanf("%d",&choice);
    switch(choice){
        case 1:
            printf("Enter Number for Square root: ");
                scanf("%lf",&x);
                        root = sqrt(x);
                    printf("Root: %lf\n", root);
                    break;
        case 2:
            printf("Enter base and power number:");
                scanf("%lf %lf",&x,&y);
                        power = pow(x, y);
                    printf("Power: %lf\n", power);
                    break;
        case 3:
            printf("Enter Number for Inverse (reciprocal): ");
                scanf("%lf",&x);
                if(x!=0){
                        inv = 1.0 / x;
                    printf("Inverse: %lf\n", inv);
                }else{
                    printf("Error: Division by Zero!\n");
                }break;
        case 4:
            printf("Enter numbers:");
                scanf("%lf %lf",&x,&y);
                    maxVal = fmax(x, y);
                    minVal = fmin(x, y);
                printf("Max: %lf, Min: %lf\n", maxVal, minVal);
                    break;
        default:
                printf("Invalid Choice!\n");
                }
    return 0;
}
