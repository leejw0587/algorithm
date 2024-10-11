#include <stdio.h>

int main(void){
    int nowH, nowM, time, resH, resM;

    nowH = 0;
    nowM = 0;
    time = 0;

    scanf("%d %d", &nowH, &nowM);
    scanf("%d", &time);

    resH = nowH;
    resM = nowM + time;

    while(resM >= 60){
        resH += 1;
        resM -= 60;

        if(resH >= 24){
            resH -= 24;
        }
    }

    printf("%d %d\n", resH, resM);
    return 0;
}