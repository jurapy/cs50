#include <cs50.h>
#include <stdio.h>

int zbroj1dio(long n);
int zbroj2dio(long n);
int duzinabroja(long n);
int prvibroj(long n);

int main(void)
{
    int checksum;
    int duzina;
    int prvi;
    long n;

    do
    {
    n = get_long("Enter credit card number: ");
    }
    while(n < 0);

    checksum = zbroj1dio(n) + zbroj2dio(n);
    duzina = duzinabroja(n);
    prvi = prvibroj(n);

    if(checksum % 10 == 0 && duzina == 15 && (prvi == 34 || prvi == 37))
    {
    printf ("AMEX\n");
    }

    else if(checksum % 10 == 0 && duzina == 16 && (prvi > 50 && prvi < 56))
    {
    printf ("MASTERCARD\n");
    }

    else if(checksum % 10 == 0 && (duzina == 13 || duzina == 16) && (prvi > 39 && prvi < 50))
    {
    printf ("VISA\n");
    }

    else
    {
        printf ("INVALID\n");
    }
}

//funkcija za checksum prvi dio
int zbroj1dio(long n)
{
    int zbroj=0;

     while(n > 1)
    {
    zbroj = n % 10 + zbroj;
    n = n / 100;
    }

    return zbroj;
}


//funkcija za checksum drugi dio
int zbroj2dio(long n)
{
    int broj;
    int zbroj;
    int dvoznamenka;

    n = n / 10;

    while(n > 1)
    {
    broj = n % 10;
    if(broj < 5)
    {
        zbroj = broj * 2 + zbroj;
    }
    else
    {
        dvoznamenka = broj * 2;
        zbroj = dvoznamenka / 10 + zbroj;
        zbroj = dvoznamenka % 10 + zbroj;
    }
    n = n / 100;
    }

    return zbroj;
}

int duzinabroja(long n)
{
    int duzina = 0;

    while(n > 1)
    {
    n = n / 10;
    duzina++;
    }

    return duzina;
}

int prvibroj(long n)
{
    while(n >= 100)
    {
        n = n / 10;
    }
    return n;
}
