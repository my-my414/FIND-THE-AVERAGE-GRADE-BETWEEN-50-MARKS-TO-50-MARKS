#include<stdio.h>
int main()
{
    double mark;
    printf("Enter your marks :");
    scanf("%lf",&mark);
    if(mark<=100 && mark>=80)
    {
        printf("Your grade is :A+\n");
    }
    else if(mark<80 && mark>=70)
    {
        printf("Your grade is A");
    }
    else if(mark<70 && mark>=60)
    {
        printf("Your grade is B");
    }
    else if(mark<60 && mark>=50)
    {
        printf("Your grade is C");
    }
    
}
