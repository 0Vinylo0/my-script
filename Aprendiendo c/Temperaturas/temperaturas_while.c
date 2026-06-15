#include <stdio.h>
/* imprime la tabla de Faherenheit-Celcius*/
int main()
{
    float fahr, celcius;
    int lower, upper, step;
    lower = 0; /* limite inferior */
    upper = 300; /* limite superior */
    step = 20; /* tamano del incremento */
    celcius = lower;
    printf ("Celsius\t      -       \tFahrenheit\n");
    while (celcius <= upper)
    { 
        fahr = (9.0/5.0) * celcius + 32;
        printf("  C %3.0f\t       -       \tF %6.2f\n", celcius, fahr);
        celcius = celcius + step;
    }
}