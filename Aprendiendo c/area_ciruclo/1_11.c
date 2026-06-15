#include <stdio.h>

#define PI 3.14159

float radio, area;

float procesar(float radio);
void preguntar();


int main () {

    printf("Para PARAR, introduce 0 en el valor del radio\n");
    
    preguntar();

    while (radio != 0) {
        if (radio < 0)
            area = 0;
        else
            area = procesar(radio);
        printf("Area = %f", area);
        
        preguntar();
    }
}

float procesar (float r) {
    float a;

    a = PI * r * r;
    return(a);
}

void preguntar () {
    printf("\nRadio = ? ");
    scanf("%f", &radio);
}