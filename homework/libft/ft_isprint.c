#include <stdio.h>
#include "libft.h"

int ft_isprint() {
    char typed;

    printf("Pick your character: ");

    scanf(" %c", &typed);
    
    if (typed >= PRINT_MIN && typed <= PRINTR_MAX) {
        return(1);
    }
    else {
        return(0);
    }
}

int main(void) {
    int result = ft_isprint();
    printf("Result: %d\n", result);
}