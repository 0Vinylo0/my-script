#include <stdio.h>

int main() {
    int entero = 10; /* variable cargada con un valor entero*/
    float flotante = 3.14; /* variable cargada con un valor de punto flotante*/
    char caracter = 'A'; /* variable cargada con un valor de caracter*/
    double flotante_doble = 3.141592653589793; /* variable cargada con un valor de punto flotante de doble precision*/
    printf("entero = %d\ncaracter = %c\ncoma flotante = %f\ncoma flotante dloble = %f\n", entero, caracter, flotante, flotante_doble);
    printf("\n%lu, %lu, %lu, %lu, %lu, %lu", sizeof entero, sizeof flotante, sizeof caracter, sizeof flotante_doble, sizeof(short int), sizeof(long int));
}