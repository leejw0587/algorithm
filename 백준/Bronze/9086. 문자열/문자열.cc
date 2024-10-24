#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {
	int T = 0;
	int i = 0;
	char string[1001];

	scanf("%d", &T);
	
	for(i = 0; i < T; i++){
		scanf("%s", string);
		printf("%c%c\n", string[0], string[strlen(string) - 1]);
	}

	return 0;
}