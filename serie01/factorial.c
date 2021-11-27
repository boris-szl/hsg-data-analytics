#include <stdio.h>



int mulitplication1(int x,int y);
int factorial(int n);




int main() {

}


int mulitplication1(int x, int y) {
	int count, sum = 0;
	while (count<y) {
		sum += x;
		count++;
	}
	return sum;
}

int factorial(int n) {
	int res = 1;
	for (int i=0;i<n;i++) {
		res = res * (n-i);
	}
	return res;
}	
