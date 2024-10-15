#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int calculate_letters(string text);
int calculate_words(string text);
int calculate_sentences(string text);

int main(void)
{
    string text = get_string("Enter text: ");

    float letters = calculate_letters(text);
    float words = calculate_words(text);
    float sentences = calculate_sentences(text);

    float L = letters / words * 100;
    float S = sentences / words * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", (int) round(index));
    }
}

int calculate_letters(string text)
{
    int letters = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }
    return letters;
}

int calculate_words(string text)
{
    int spaces = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isspace(text[i]))
        {
            spaces++;
        }
    }
    return spaces + 1;
}

int calculate_sentences(string text)
{
    int punctuations = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == 46 || text[i] == 33 || text[i] == 63)
        {
            punctuations++;
        }
    }
    return punctuations;
}
