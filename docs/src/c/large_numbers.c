#include <stdio.h>
#include <gmp.h>

void factorial(mpz_t result, unsigned long n) {
    mpz_t temp;
    mpz_init_set_ui(result, 1);
    mpz_init_set_ui(temp, 1);

    for (unsigned long i = 2; i <= n; i++) {
        mpz_mul_ui(temp, temp, i);
        mpz_set(result, temp);
    }

    mpz_clear(temp);
}

int main(void) {
    mpz_t large_factorial;
    mpz_init(large_factorial);

    factorial(large_factorial, 100);
    gmp_printf("The factorial of 100 is: %Zd\n", large_factorial);

    mpz_clear(large_factorial);
    return 0;
}
