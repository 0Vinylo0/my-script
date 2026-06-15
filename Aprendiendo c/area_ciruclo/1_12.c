#include <stdio.h>

#define PI 3.14159

float procesar(float radio);

int main () {
    
    int n, i = 0;

    float radio[100],
          area[100];
    
    printf ("Para PARAR introduzca 0 en el valor del radio\n");
    printf ("Radio = ?\n");
    scanf ("%f", &radio[i]);

    while (radio[i]) {
        if (radio[i] < 0) {
            area[i] = 0;
        }
        else {
            area[i] = procesar(radio[i]);
        }
        printf("Radio = ?\n");
        scanf("%f", &radio[++i]);
    }
    n = --i;

    printf("\nRelacion de resultados\n\n");
    for (i = 0; i <= n; ++i) {
        printf("Radio = %f\t Area = %f\n", radio[i], area[i]);
    }
    
}

float procesar(float r) {
    float a;
    a = PI * r * r;
    return(a);
}