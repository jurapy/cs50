#include "helpers.h"
#include <stdio.h>
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int i;
    int j;
    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width; j++)
        {
            int tempB = image[i][j].rgbtBlue;
            int tempG = image[i][j].rgbtGreen;
            int tempR = image[i][j].rgbtRed;
            int average = round(((float)(tempB + tempG + tempR)) / 3);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int i;
    int j;
    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width; j++)
        {
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);
            if(sepiaRed > 255)
            sepiaRed = 255;
            if(sepiaGreen > 255)
            sepiaGreen = 255;
            if(sepiaBlue > 255)
            sepiaBlue = 255;
            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtRed = sepiaRed;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int i;
    int j;
    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++) //row
    {
        for (int j = 0; j < width; j++) //pixel
        {
            int red = 0;
            int green = 0;
            int blue = 0;
            int counter = 0;

            for (int r = -1; r < 2; r++) //row of pixels around choesen pixel
            {
                    for (int c = -1; c < 2; c++) //one pixel in that row
                    {

                    if (i + r < 0 || i + r > height - 1 || j + c < 0 || j + c > width - 1)
                        {
                        continue;
                        }

                        blue += image[i + r][j + c].rgbtBlue;
                        green += image[i + r][j + c].rgbtGreen;
                        red += image[i + r][j + c].rgbtRed;
                        counter++;
                    }
            }
                copy[i][j].rgbtBlue = round((float)blue / counter);
                copy[i][j].rgbtGreen = round((float)green / counter);
                copy[i][j].rgbtRed = round((float)red / counter);
        }
    }

    //fills image with blured pixels from copy
    for (int i = 0; i < height; i++) //row
    {
        for (int j = 0; j < width; j++) //pixel
        {
            image[i][j].rgbtBlue = copy[i][j].rgbtBlue;
            image[i][j].rgbtGreen = copy[i][j].rgbtGreen;
            image[i][j].rgbtRed = copy[i][j].rgbtRed;
        }
    }
    return;
}
