#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>
#include <stdint.h>

typedef uint8_t BYTE;
#define blockSize 512

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        printf("Usage ./recover IMAGE\n");
        return 1;
    }

    FILE *image = fopen(argv[1], "r");

    if (image == NULL) {
        perror("Error while opening image!");
        return 1;
    }

    BYTE buffer[blockSize];
    char filename[8];
    int counter = 0;
    FILE *datafile = NULL;

    while(fread(buffer, sizeof(BYTE), blockSize, image))
    {
        if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] >= 0xe0 && buffer[3] < 0xf0 )
        {
            if(datafile != NULL)
            {fclose(datafile);}

            sprintf(filename,"%03d.jpg", counter);
            datafile = fopen(filename,"w");
            counter++;
        }

        if (datafile != NULL)
        {
        fwrite(buffer, sizeof(BYTE), blockSize, datafile);
        }
    }
    fclose(datafile);
    fclose(image);
    return 0;
}
