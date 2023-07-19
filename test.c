#include <stdio.h>
#include <stdbool.h>

int main() {
        int num1 = 0;
        int num2 = 0;
        int hap = 0;

        while (true) {
                printf("숫자1: ");
                num1 = scanf("%d", &num1);
                printf("숫자2: ");
                num2 = scanf("%d", &num2);
                hap = num1 + num2;
                printf("%d + %d = %d", &num1, &num2, &hap);
        }
}