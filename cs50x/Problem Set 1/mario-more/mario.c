#include <cs50.h>
#include <stdio.h>

int main(void)
{
   int n;
   do
      {
      n = get_int ("how tall? ");
      }
   while (n<1 || n>8);

   //rows
   for (int i=0; i<n; i++)
   {

      //left collums
      for (int j=n-1; j>i; j--)
      {
         printf(" ");
      }

      for (int z=-1; z<i; z++)
      {
         printf("#");
      }

      //space between piramides
      printf("  ");

      //right piramide

      //right collums
      for (int z=-1; z<i; z++)
      {
         printf("#");
      }

   printf("\n");
   }
}
