// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include "dictionary.h"
#include <stdlib.h>
#include <string.h>

#include <cs50.h>
#include <strings.h>

#include <math.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 676;


// Hash table
node *table[N];

// Counter for words in dictionary
int counter = -1;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO

    int index = hash(word);

    node *trav;

    trav = table[index];

    while(trav != NULL)
    {
        if(strcasecmp(trav -> word, word) == 0)
        {
            return true;
        }

        else
        trav = trav -> next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function

    char prvo = word[0];
    char drugo = word[1];

    if (prvo == '\'')
        prvo = 'A';

    if (drugo == '\'')
        drugo = 'A';

    // Bolja hash funkcija koja uzima u obzir cijeli raspon slova, by ChatGPT
    return ((toupper(prvo) - 'A') * 26 + (toupper(drugo) - 'A')) % N;

/*
    char prvo = word[0];
    char drugo = word[1];

    if(prvo == '\'')
    prvo = 'A';

    if(drugo == '\'')
    drugo = 'A';

    return (toupper(prvo) - 'A') * 26 + (toupper(drugo) - 'A');

    //return toupper(word[0]) - 'A';*/
}

    // Posible math hash function
/*
    int sum = 0;

    for(int i = 0, n = strlen(word); i < n; i++)
    {
        sum += word[i];
    }

    return sum % N;
    printf("proslo\n")
*/



// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //TODO

    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    return false;

    while(!feof(file))
    {
        counter++;
        char buffer[LENGTH + 1];
        fscanf(file, "%s", buffer);

        unsigned int hashed_value = hash(buffer);

        node *new = malloc(sizeof(node));
        strcpy(new -> word, buffer);
        new -> next = NULL;

        if(table[hashed_value] == NULL)
        table[hashed_value] = new;
        else
        {
            new -> next = table[hashed_value];
            table[hashed_value] = new;
        }
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO

    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO

    for(int i = 0; i < N; i++)
    {
        node *cursor = table[i];

        while(cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor -> next;
            free(tmp);
        }
    }

    return true;
    //return false;
}
