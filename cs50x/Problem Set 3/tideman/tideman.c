#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool lock_check (int winner, int loser);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// TODO Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO
        for(int i=0; i < candidate_count; i++)
    {
        if(!strcmp(candidates[i], name))
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // TODO
    for(int i=0; i < candidate_count; i++)
    {
        for(int j=i+1; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]]++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO
    int n = -1;
    for(int i=0; i < candidate_count; i++)
    {
        for(int j=i+1; j < candidate_count; j++)
        {
            if(preferences[i][j] > preferences[j][i])
            {
                pair_count++;
                n++;
                pairs[n].winner = i;
                pairs[n].loser = j;
            }
            else if(preferences[i][j] < preferences[j][i])
            {
                pair_count++;
                n++;
                pairs[n].winner = j;
                pairs[n].loser = i;
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
        int pairs_pomocna[pair_count];
    for(int i=0; i < pair_count; i++)
    {
        int win = pairs[i].winner;
        int los = pairs[i].loser;
        int razlika = preferences[win][los] - preferences[los][win];
        pairs_pomocna[i] = razlika;
    }

    int me = 0;
    pair me_glavna;
    for(int i=0; i < pair_count; i++)
    {
        for(int j=i+1; j < pair_count; j++)
        {
            if(pairs_pomocna[j] > pairs_pomocna[i])
            {
                me = pairs_pomocna[i];
                pairs_pomocna[i] = pairs_pomocna[j];
                pairs_pomocna[j] = me;

                me_glavna = pairs[i];
                pairs[i] = pairs[j];
                pairs[j] = me_glavna;
            }
        }
    }
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    for (int i = 0; i < pair_count; i++)
    {
        int winner = pairs[i].winner;
        int loser = pairs[i].loser;
        locked[winner][loser] = true;

        if (lock_check(winner, loser))
        {
            locked[winner][loser] = false;
        }
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    for(int i=0; i < pair_count; i++)
    {
        int n=0;

        for(int j=0; j < pair_count; j++)
        {
            if(locked[j][i] == true)
            {
                n++;
            }
        }

        if(n == 0)
        {
            printf("%s\n", candidates[i]);
            break;
        }
    }
    return;
}

bool lock_check (int winner, int loser)
{
    // one candidate case
    if (candidate_count == 1)
    return false;

    // lock check
   if (winner == loser)
        return true;

    for (int i = 0; i < candidate_count; i++)
    {
        // is there already pair
        if (locked[loser][i] == true)
        {
            // loser points to
            if (lock_check(winner, i))
            return true;
        }
    }

    return false;
}
