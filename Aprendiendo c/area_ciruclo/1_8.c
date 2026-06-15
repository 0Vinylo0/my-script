/* programa para carcular el area de un circulo con comprobaciones de errores*/
#include <stdio.h>

#define PI 3.14159

float procesar(float radio);

int main () {
    float area, radio;
    printf("Radio = ?");
    scanf("%f", &radio);

    if (radio < 0)
        area = 0;
    else
        area = procesar(radio);
        printf("Area = %f", area);
}

float procesar(float r) {
    float a;
    a = PI * r * r;
    return(a);
}