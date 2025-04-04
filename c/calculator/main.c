#include <stdio.h>
#define SEPARATOR "-----------------------------" 

double result(double first_number, char operator, double second_number) {
    double result;
    switch (operator) {
        case '+': 
            return first_number + second_number;
        case '-': 
            return first_number - second_number;
        case '/':    
		    return first_number / second_number;
        case '*': 
            return first_number * second_number;
        default:
            printf("Somthing goes wrong... enter only valid operator (+, *, / or +)!\n");
            return 0;
        }
}

int main() {
    printf("%s\n", SEPARATOR);
    printf("| An simple Calculator in C\n");
    printf("%s\n", SEPARATOR);

    double first_number;
    char operator;
    double second_number;

    printf("\nWhat is your fist number: ");
    scanf("%lf", &first_number);

    printf("Your operator: ");
    scanf(" %c", &operator); // The space before %c skips any leftover whitespace or newline chaaracters in the input 
    printf("What is your secend number: ");
    scanf("%lf", &second_number);

    double calc_result = result(first_number, operator, second_number);
    printf("The result is:\n%.2lf\n", calc_result); 

    return 0;
}
