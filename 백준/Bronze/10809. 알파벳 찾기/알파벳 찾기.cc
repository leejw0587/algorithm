#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {
	int count[26] = { 0, };
	int i = 0;
	char string[101];

	scanf("%s", string);

	for (i = 0; i < strlen(string); i++) {
		if (count[string[i] - 'a'] == 0) {
			count[string[i] - 'a'] = i + 1;
		}
	}

	for (i = 0; i < 26; i++) {
		if (count[i] == 0) {
			printf("-1 ");
		}
		else{
			printf("%d ", count[i] - 1);
		}
	}

	return 0;
}