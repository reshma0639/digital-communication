#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"


int  main(void) //main function begins
{

//Gaussian random numbers
gaussian("gau.dat", 1000000);

//Mean and variance of Gaussian 
printf("GAUSSIAN:\n");
printf("MEAN: %lf\n",mean("gau.dat"));
printf("VARIANCE: %lf\n",variance("gau.dat"));
return 0;
}
