#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"


int  main(void) //main function begins
{
 
//Uniform random numbers
uniform("uni.dat", 1000000);


//Mean and variance of uniform
printf("UNIFORM:\n");
printf("MEAN: %lf \n",mean("uni.dat"));
printf("VARIANCE: %lf\n",variance("uni.dat"));
return 0;
}


