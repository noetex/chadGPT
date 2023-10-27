#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>


#define ARRAYSIZE(Array) (sizeof(Array)/sizeof((Array)[0]))

float Train[][2] =
{
	{0, 2},
	{1, 5},
	{2, 8},
	{3, 11},
	{4, 14}
};


static float
random_float(void)
{
	float Result = (float)rand()/RAND_MAX * 10;
	return Result;
}

static float
the_cost(float Weight, float Bias)
{
	float Result = 0;
	for(unsigned int Index = 0; Index < ARRAYSIZE(Train); Index += 1)
	{
		float Input = Train[Index][0];
		float Expected = Train[Index][1];
		float Estimate = Input * Weight + Bias;
		float Error = (Expected - Estimate);
		Result += Error * Error;
	}
	return Result/ARRAYSIZE(Train);
}

#define ERROR_MIN 0.00001


// neuron: weight, bias

float sigmoidf(float Value)
{
	float Result = (1 / (1 + expf(-Value)));
	return Result;
}


int main(void)
{
	srand(time(0));
	float Weight = random_float();
	float Bias = random_float();
	float Epsilon = 0.001;
	float Rate = 0.1;
	int Iterations = 0;
	for(;;)
	{
		printf("Weight: %f, Bias: %f\n", Weight, Bias);
		float F = the_cost(Weight, Bias);
		if(F < ERROR_MIN) break;
		float dW = (the_cost((Weight + Epsilon), Bias) - F)/Epsilon;
		float dB = (the_cost(Weight, (Bias + Epsilon)) - F)/Epsilon;
		Weight -= Rate * dW;
		Bias -= Rate * dB;
		Iterations += 1;
		//getchar();
	}
	printf("\nIterations: %i\n", Iterations);
	return 0;
}
