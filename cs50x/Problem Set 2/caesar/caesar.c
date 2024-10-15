#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

string ciphertext(string plaintext, int keyisdigit);
int calculate_key(string key);

int main(int argc, string argv[])
{
    string key = argv[1];
    if ( argc != 2 || calculate_key(key) == 0 )
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        string plaintext = get_string("plaintext: ");
        int keyisdigit = calculate_key(key);
        printf("ciphertext: %s\n", ciphertext(plaintext, keyisdigit));
    }
    return 0;
}

int calculate_key(string key)
{
    int n = strlen(key);
    for (int i = 0; i < n; i++)
    {
        if (isdigit(key[i]) == 0)
        return false;
    }
    return atoi(key);
}

string ciphertext(string plaintext, int keyisdigit)
{
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (isalpha(plaintext[i]))
        {
            if (plaintext[i] < 91)
            {
                int varijabla = plaintext[i] + keyisdigit;
                while (plaintext[i] > 90)
                {
                    varijabla -= 26;
                }
                plaintext[i] = (char)varijabla;
            }
            else
            {
                int varijabla = plaintext[i] + keyisdigit;
                while (varijabla > 122)
                {
                    varijabla -= 26;
                }
                plaintext[i] = (char)varijabla;
            }
        }
    }
    return plaintext;
}
