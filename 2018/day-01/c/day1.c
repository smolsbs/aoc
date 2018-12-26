#include <stdio.h>
#include <stdlib.h>

#ifndef MAX
#define MAX 100000
#endif

long part1(long *, int);
long part2(long *, int);

int main(int argc, char const *argv[])
{
	FILE *fp = fopen("input", "r" );
	if (fp == NULL){
		return 1;
	}
	long data[1016];
	long *pData = data;
	char *line, *ptr;
	size_t len = 0;
	int nlines = 0;

	while(getline(&line, &len, fp) != -1){
		*(pData) = strtol(line, &ptr, 10);
		pData++;
		nlines++;
	}

	printf("%li\n", part1(data, nlines));
	printf("%li\n", part2(data, nlines));
	/* clearing stuff*/
	//free(line);
	fclose(fp);
	return 0;
}

long part1(long *data, int n){
	long sum = 0;
	long *ptr = data;
	for (int i = 0; i < n; i++){
		sum += *(ptr + (long) i);
	}
	return sum;
}

long part2(long *data, int n){
	long sum = 0;
	int a = 0;
	long nums[MAX];
	long *pNums = nums;

	while(1){
		long *ptr = data;
		for (int i = 0; i < n; i++){
			sum += *(ptr + (long) i);
			for (int j = 0; j <= a; j++){
				if (sum == *(pNums + (long) j) ){
					return sum;
				}
			}
			nums[a] = sum;
			a++;
		}
	}
	return sum;
}

