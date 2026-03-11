#include <stdio.h>
#include "libft.h"

int ft_isascii() {
    char typed;

    printf("Pick your character: ");

    scanf(" %c", &typed);
    
    if (typed >= ASCII_MIN && typed <= ASCII_MAX) {
        return(1);
    }
    else {
        return(0);
    }
}

int main(void) {
    int result = ft_isascii();
    printf("Result: %d\n", result);
}