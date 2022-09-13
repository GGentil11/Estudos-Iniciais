#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char c = get_char("Você concorda com os Termos? (Respostas: S ou N)\n");
    if (c == 's' || c == 'S')
    {
        printf("Termos aceitos\n");
    }
    else if (c == 'n'|| c == 'N')
    {
        printf("Termos negados\n");
    }
}