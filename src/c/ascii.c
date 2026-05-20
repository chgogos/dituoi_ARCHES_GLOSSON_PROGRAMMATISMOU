#include <stdio.h>

int main() {
    char ch;

    // Print ASCII values for characters A-Z and a-z
    printf("Character    ASCII Value\n");
    printf("------------------------\n");
    
    for (ch = 'A'; ch <= 'Z'; ch++) {
        printf("    %c          %d\n", ch, ch);
    }

    printf("\n");

    for (ch = 'a'; ch <= 'z'; ch++) {
        printf("    %c          %d\n", ch, ch);
    }

    // Demonstrate ASCII values for digits and special characters
    printf("\nAdditional ASCII characters:\n");
    printf("Space: ASCII %d\n", ' ');
    printf("0: ASCII %d\n", '0');
    printf("9: ASCII %d\n", '9');
    printf("!: ASCII %d\n", '!');
    printf("@: ASCII %d\n", '@');
    printf("#: ASCII %d\n", '#');

    return 0;
}
