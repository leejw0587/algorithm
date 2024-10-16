#include <stdio.h>
#include <string.h>

int main(void){
    int T = 0;
    int i = 0;
    char string[1000] = {0};

    scanf("%d", &T);
    for(i = 0; i < T; i++){
        scanf(" %s", &string[0]);
        printf("%c%c\n", string[0], string[strlen(string) - 1]);

        memset(string, '\0', sizeof(string));
    }

    return 0;
}