
#include <stdio.h>
#include "stats.h"

/* Size of the Data Set */
#define SIZE (40)

void main()
{

  unsigned char test[SIZE] = { 34, 201, 190, 154,   8, 194,   2,   6,
                              114, 88,   45,  76, 123,  87,  25,  23,
                              200, 122, 150, 90,   92,  87, 177, 244,
                              201,   6,  12,  60,   8,   2,   5,  67,
                                7,  87, 250, 230,  99,   3, 100,  90};
  /* Statistics and Printing Functions Go Here */

}
/*
  *  print_array - function that prints all the data in an array
  * @array: variable that contain the array
  * @length: variable that stores the length of the array
  * return : returns void

**/
void print_array (unsigned char *array, unsigned int length)
{
  for (int i = 0; i < length; i++)
  {
    printf("%u", array[i]);
  }
  printf("\n");
}

unsigned char find_median(unsigned char *array, unsigned int length)
{
  // to find the median
  int median = length / 2;
  unsigned char value;
  value = array[median];
  return (value);
}

int find_mean(unsigned char *array, unsigned int length)
{
  //to find the mean(average)
  unsigned int total = 0;
  for (int i = 0; i < length; i++)
  {
    total += array[i];
  }
  float mean;
  mean = total / length;
  return (mean);
}

unsigned char maximum(unsigned char *array, unsigned int length)
{
  unsigned char max;
  for (int i = 0; i < length; i++)
  {
    if (array[i + 1] > array[i])
      max = array[i+1];
    else
      continue;
  }
  return max;
}

unsigned char minumum(unsigned char *array, unsigned int length)
{
  unsigned char min;
  for (int i = 0; i < length; i++)
  {
    if (array[i + 1] < array[i])
    {
      min = array[i + 1];
    }
    else
    {
      continue;
    }
  }
  return min;
}

void sort_array (unsigned char *array, unsigned int length)
{
  // to sort the array

}