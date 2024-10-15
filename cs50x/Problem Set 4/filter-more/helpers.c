#include <math.h>

#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i=0; i < height; i++) //for row
    {
        for(int j=0; j < width; j++) //for pixel
        {
            int avg = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for(int i=0; i < height; i++) //for row
    {
        for(int j=0; j < width; j++) //for pixel
        {
            copy[i][j] = image[i][j];
        }
    }

    for(int a=0; a < height; a++) //for row
    {
        int copy_width = width;
        for(int b=0; b < width; b++) //for pixel
        {
            image[a][b] = copy[a][copy_width - 1];
            copy_width--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for(int i=0; i < height; i++) //for image row
    {
        for(int j=0; j < width; j++) //for image pixel
        {

            //variable inicialization and reset
            float avgR = 0;
            float avgG = 0;
            float avgB = 0;
            float brojac = 0;

            int c = (i == 0) ? 0 : -1;
            int d = (i == height - 1) ? 0 : 1;
            int e = (j == 0) ? 0 : -1;
            int f = (j == width - 1) ? 0 : 1;

            for(int a = c; a <= d; a++) //for row around selected pixel
            {

                for(int b = e; b <= f; b++) //for column around selected pixel
                {
                    //sum of values
                    avgR += image[i + a][j + b].rgbtRed;
                    avgG += image[i + a][j + b].rgbtGreen;
                    avgB += image[i + a][j + b].rgbtBlue;

                    //checks how much pixels are around selected pixel
                    brojac++;
                }
            }

            //setting average color values in output image
            copy[i][j].rgbtRed = round( avgR / brojac);
            copy[i][j].rgbtGreen = round( avgG / brojac);
            copy[i][j].rgbtBlue = round( avgB / brojac);
        }
    }

    //from copy to image
    for(int i=0; i < height; i++) //for row
    {
        for(int j=0; j < width; j++) //for pixel
        {
            image[i][j] = copy[i][j];
        }
    }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    //izrada kopije
    RGBTRIPLE copy[height][width];

    for(int i=0; i < height; i++) //for row
    {
        for(int j=0; j < width; j++) //for pixel
        {
            copy[i][j] = image[i][j];
        }
    }

    int sobelFilterX[3][3] = {
        {-1, 0, 1},
        {-2, 0, 2},
        {-1, 0, 1}
    };

    int sobelFilterY[3][3] = {
        {-1, -2, -1},
        {0, 0, 0},
        {1, 2, 1}
    };

    for(int i=0; i < height; i++) //row
    {
        for(int j=0; j < width; j++) //pixel
        {
            //pixels around selected pixel
            float gxR = 0;
            float gxG = 0;
            float gxB = 0;
            float gyR = 0;
            float gyG = 0;
            float gyB = 0;
            int sobelR = 0;
            int sobelG = 0;
            int sobelB = 0;

            for(int a = -1; a <= 1; a++) //iterate rows around the selected pixel
            {
                for(int b = -1; b <= 1; b++) //iterate columns around the selected pixel
                {
                    int row = i + a;
                    int col = j + b;

                    //check if the current row and column are within bounds
                    if (row >= 0 && row < height && col >= 0 && col < width)
                    {
                        int factorX = sobelFilterX[a + 1][b + 1];
                        int factorY = sobelFilterY[a + 1][b + 1];

                        gxR += factorX * copy[row][col].rgbtRed;
                        gxG += factorX * copy[row][col].rgbtGreen;
                        gxB += factorX * copy[row][col].rgbtBlue;

                        gyR += factorY * copy[row][col].rgbtRed;
                        gyG += factorY * copy[row][col].rgbtGreen;
                        gyB += factorY * copy[row][col].rgbtBlue;
                    }
                }
            }

            sobelR = round(sqrt(gxR * gxR + gyR * gyR));
            sobelG = round(sqrt(gxG * gxG + gyG * gyG));
            sobelB = round(sqrt(gxB * gxB + gyB * gyB));

            image[i][j].rgbtRed = (sobelR > 255) ? 255 : sobelR;
            image[i][j].rgbtGreen = (sobelG > 255) ? 255 : sobelG;
            image[i][j].rgbtBlue = (sobelB > 255) ? 255 : sobelB;
        }

    }

    return;
}
