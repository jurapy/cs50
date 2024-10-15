#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>



string key_check(string key);
bool key_repeat(string key);
string chipertext(string plaintext, string key);



char alphabet[] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
char alphabet2[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};


int main(int argc, string argv[])
{

    string key = argv[1];

    if ( argc != 2 )
    {
        printf("Usage: ./substitution KEY\n");
        return 1;
    }
    else if ( strlen(key) != 26 )
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    else if ( key_check(key) == 0 )
    {
        printf("Key must only contain alphabetic characters.\n");
        return 1;
    }
    else if ( key_repeat(key) == 1 )
    {
        printf("Key must not contain repeated characters.\n");
        return 1;
    }

    string plaintext = get_string("plaintext: ");
    printf("ciphertext: %s\n", chipertext(plaintext, key));

return 0;
}



string key_check(string key)
{
    int n = strlen(key);
    for (int i = 0; i < n; i++)
    {
        if( isalpha (key[i]) == 0)
        {
            return 0;
        }
    }
    return key;
}



bool key_repeat(string key)
{
    int n = strlen(key);
    for(int i = 0; i < n; i++)
    {
        for(int j = i + 1; j < n; j++)
        {
        if(key[i] == key[j])
        {
            return 1;
        }
        }

    }
    return 0;
}



string chipertext(string plaintext, string key)
{

   int n = strlen(plaintext);
   int m = strlen(key);

    for (int i = 0; i < n; i++)
    {
        if(isalpha(plaintext[i]))
        {
            for (int j = 0; j < m; j++)
            {
                if(isupper(plaintext[i]))
                {
                    if(plaintext[i] == alphabet[j])
                    {
                        plaintext[i] = toupper(key[j]);
                        break;
                    }
                }
                else
                {
                    if(plaintext[i] == alphabet2[j])
                    {
                        plaintext[i] = tolower(key[j]);
                        break;
                    }
                }
            }
        }
    }

    return plaintext;
}
