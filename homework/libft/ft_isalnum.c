#include <stdio.h>
#include "libft.h"

int ft_isalnum() {
    char typed;

    printf("Pick your character: ");

    scanf(" %c", &typed);
    
    if ((typed >= UPPER_MIN && typed <= UPPER_MAX) || (typed >= LOWER_MIN &&  typed <= LOWER_MAX) || (typed >= DIGIT_MIN && typed <= DIGIT_MAX)) {
        return(1);
    }
    else {
        return(0);
    }
}

int main(void) {
    int result = ft_isalnum();
    printf("Result: %d\n", result);
}