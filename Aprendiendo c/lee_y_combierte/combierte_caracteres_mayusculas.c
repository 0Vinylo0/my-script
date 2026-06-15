#include <stdio.h>
#include <ctype.h>

int main () {
    char minusc, mayusc;

    minusc = getchar();
    mayusc = toupper(minusc);
    putchar(mayusc);
}