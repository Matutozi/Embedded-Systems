/**
 * File: stats.h
 * author : Emmanuel 
 * Date: 02/02/2024
 * Description: Implementation of statistical functions for analyzing arrays.
 **/

#ifndef __STATS_H__
#define __STATS_H__

#include <stdio.h>
#include <stdlib.h>

//FUNCTIONS PROTOTYPES

void print_statistics (unsigned char minimum, unsigned char maximum, float mean, unsigned char median);
void print_array (unsigned char *array, unsigned int length);
unsigned char find_median(unsigned char *array, unsigned int length);

int find_mean(unsigned char *array, unsigned int length); //  Given an array of data and a length, returns the mean

unsigned char maximum(unsigned char *array, unsigned int length); //  Given an array of data and a length, returns the maximum

unsigned char minimum(unsigned char *array, unsigned int length); //  Given an array of data and a length, returns the minumum


void sort_array();

#endif /* __STATS_H__ */
