#include <stdio.h>

#define PI 3.14159

float procesar(float radio);
int iteraccion(void);

float radio, area;

int main () {
    int cont;

    printf("Para PARAR, introduce 0 en el valor del radio\n");
    iteraccion();

    for (cont = 1; radio != 0; ++cont) {
        if (radio < 0)
            area = 0;
        else
            area = procesar(radio);
        
        printf("Area = %f", area);
        iteraccion();
    }   
}

float procesar(float r) {
    float a;
    a = PI * r * r;
    return(a);
}
int iteraccion(void) {
    printf("\nRadio = ? ");
    scanf("%f", &radio);
}