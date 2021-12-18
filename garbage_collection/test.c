#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>



double* scanVector(int n) {
	int i;
	double* vector = NULL;
	vector = malloc(n*sizeof(double));
	for(i=0;i<n;i++) {
		vector[i] = 0;
	}
	return vector;
}

void printVector(double* vector, int n) {
	int i;
	for(i=0;i<n;i++) {
		printf("%.2f\n", vector[i]);
	}
} 

double* extendVector(double* vector, int n, int k) {
	vector = realloc(vector*sizeof(double));
	for(i=n,i<k);i++
}


int main() {
	int n;
	printf("Einlesen der Vektorlänge n = ");
	scanf("%d", &n);
	double* vector = NULL;
	vector = scanVector(n);
	printVector(vector, n);



	free(vector);
	vector = NULL;

}
