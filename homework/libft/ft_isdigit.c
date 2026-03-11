#include <stdio.h>
#include "libft.h"

int ft_isdigit() {
    char typed;

    printf("Pick your character: ");

    scanf(" %c", &typed);
    
    if (typed >= DIGIT_MIN && typed <= DIGIT_MAX) {
        return(1);
    }
    else {
        return(0);
    }
}

int main(void) {
    int result = ft_isdigit();
    printf("Result: %d\n", result);
}