/*programa para carcular el area de un circulo*/

#include <stdio.h>  /* Acceso a la biblioteca de entarda */

#define PI 3.14159 /* Declaracion de definicion PI */

float procesar(float radio); /*Prototipo de funcion*/

int main () {   /* Cabecera de la funcion */
    float radio, area;  /* Definicion de variables */

    printf("Radio = ? "); /* Instrucciones de salida */
    scanf("%f", &radio);    /* Instrucciones de entrada */

    area = procesar(radio); /* Instruccion de asignacion */
    printf("Area es = %f", area); /* Instruccion de salida */
}

float procesar(float r) { /* Define la funcion */

    float a; /* Declaracion de variable local */

    a = PI * r * r;
    return(a);
}