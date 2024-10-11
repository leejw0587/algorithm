#include <stdio.h>

int main(void){
    int N, iteration, i;

    N = 0;
    i = 0;
    
    scanf("%d", &N);
    iteration = N / 4;
    
    for(i = 0; i < iteration; i++){
        printf("long ");
    }
    printf("int");
    return 0;
}