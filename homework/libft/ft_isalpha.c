#include <stdio.h>
#include "libft.h"

int ft_isalpha() {
    char typed;

    printf("Pick your character: ");

    scanf(" %c", &typed);
    
    if ((typed >= UPPER_MIN && typed <= UPPER_MAX) || (typed >= LOWER_MIN &&  typed <= LOWER_MAX)) {
        return(1);
    }
    else {
        return(0);
    }
}

int main(void) {
    int result = ft_isalpha();
    printf("Result: %d\n", result);
}