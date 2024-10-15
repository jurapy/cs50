#include <cs50.h>
#include <stdio.h>

int sum1(long n);
int sum2(long n);
int number_lenght(long n);
int first_number(long n);

int main(void)
{
    int checksum;
    int lenght;
    int first;
    long n;

    do
    {
    n = get_long("Enter credit card number: ");
    }
    while(n < 0);

    checksum = sum1(n) + sum2(n);
    lenght = number_lenght(n);
    first = first_number(n);

    if(checksum % 10 == 0 && lenght == 15 && (first == 34 || first == 37))
    {
    printf ("AMEX\n");
    }

    else if(checksum % 10 == 0 && lenght == 16 && (first > 50 && first < 56))
    {
    printf ("MASTERCARD\n");
    }

    else if(checksum % 10 == 0 && (lenght == 13 || lenght == 16) && (first > 39 && first < 50))
    {
    printf ("VISA\n");
    }

    else
    {
        printf ("INVALID\n");
    }
}

// checksum function first part
int sum1(long n)
{
    int sum=0;

     while(n > 1)
    {
    sum = n % 10 + sum;
    n = n / 100;
    }
    return sum;
}


// checksum function second part
int sum2(long n)
{
    int broj;
    int sum;
    int dvoznamenka;
    n = n / 10;

    while(n > 1)
    {
    broj = n % 10;
    if(broj < 5)
    {
        sum = broj * 2 + sum;
    }
    else
    {
        dvoznamenka = broj * 2;
        sum = dvoznamenka / 10 + sum;
        sum = dvoznamenka % 10 + sum;
    }
    n = n / 100;
    }

    return sum;
}

int number_lenght(long n)
{
    int lenght = 0;

    while(n > 1)
    {
    n = n / 10;
    lenght++;
    }
    return lenght;
}

int first_number(long n)
{
    while(n >= 100)
    {
        n = n / 10;
    }
    return n;
}
