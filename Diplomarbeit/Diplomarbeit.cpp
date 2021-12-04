#ifdef __unix__
# include <unistd.h>
#elif defined _WIN32
# include <windows.h>
#define sleep(x) Sleep(1000 * (x))
#endif
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>
#include <unistd.h>



int moveorrotate(int faktor, int block1, int block2, int block3, int block4) {
    int error = 0;
    char input;
    if (kbhit()) {
        input = getch();

    }
    if (input == 'a') {

        faktor--;
    }




    if (input == 'd') {
        /* for(int i=9;i<200;i+10){
        if(block1==i||block2==i||block3==i||block4==i){
        error=1;
        }
         }
        if(error==0){
        */
        faktor++;
        /*}*/
    }

    if (input == 's') {
        /*
        block1=block1+10;
        block2=block2+10;
        block3=block3+10;
        block4=block4+10;
        */
        faktor = faktor + 10;



    }


    return faktor;

}
void* func(void* arg) {

    pthread_detach(pthread_self());




    pthread_exit(NULL);
}

int fun(counter) {
    pthread_t ptid;


    pthread_create(&ptid, NULL, &func, NULL);

    sleep(1);
    counter++;





    return counter;
}

int main() {
    int endscreen[200] = { 1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
    int Spielfeld[200];
    char random_blocks[400];
    srand(time(NULL) % 100);
    int x_start = 3;
    int y_start = 0;
    int x = x_start;
    int y = y_start;
    int co = y * 10 + x;
    char input;
    int faktor = 0;
    int temp;
    int counter;








    for (int i = 0; i < 200; i++) {

        Spielfeld[i] = 0;
    }
    /*
    for(int i=0; i<200; i++){
        if(i%10==0){
            printf("\n");
        }
        printf("[%d]", Spielfeld[i]);
    }
    */
    /*Blockdefinition*/

    int a[4] = { co,co + 1,co + 10,co + 11 };
    int b[4] = { co,co + 1,co + 2,co + 3 };
    int c[4] = { co,co + 10,co + 11,co + 12 };
    int d[4] = { co + 10,co + 11,co + 12,co + 2 };
    int e[4] = { co + 10,co + 11,co + 1,co + 2 };
    int f[4] = { co,co + 1,co + 11,co + 12 };
    int g[4] = { co + 1,co + 10,co + 11,co + 12 };


    printf("\n");


    /*
    for(int i=0; i<200; i++){
        if(i%10==0){
            printf("\n");
        }
        if(i==g[0]||i==g[1]||i==g[2]||i==g[3]){
           printf("[1]");
        }
        else{
        printf("[%d]", Spielfeld[i]);
        }
    }
    */

    for (int u = 0; u < 400; u++) {
        random_blocks[u] = "abcdefg"[rand() % 7];

    }

    int i;
    int u = 0;
    int v;
    int n = 0;



    while (n != 1) {

        u++;
        v = 0;

        int stop = 0;
        faktor = 0;

       /* printf("%c", random_blocks[u]);*/
        switch (random_blocks[u])


        case 'a':
            while (n != 1) {

                system("cls");



                for (int i = 0; i < 200; i++) {
                    if (i % 10 == 0) {
                        printf("\n");
                    }
                    if (i == a[0] + 10 * v + faktor || i == a[1] + 10 * v + faktor || i == a[2] + 10 * v + faktor || i == a[3] + 10 * v + faktor) {

                        printf("[1]");

                    }
                    else {
                        printf("[%d]", Spielfeld[i]);
                    }
                }
                counter = 0;










                if ((a[0] + 10 * v) >= 190 && (a[0] + 10 * v) <= 199 || (a[1] + 10 * v) >= 190 && (a[1] + 10 * v) <= 199 || (a[2] + 10 * v) >= 190 && (a[2] + 10 * v) <= 199 || (a[3] + 10 * v) >= 190 && (a[3] + 10 * v) <= 199) {
                    Spielfeld[a[0] + 10 * v + faktor] = 1;
                    Spielfeld[a[1] + 10 * v + faktor] = 1;
                    Spielfeld[a[2] + 10 * v + faktor] = 1;
                    Spielfeld[a[3] + 10 * v + faktor] = 1;
                    break;

                }
                if (a[0] + 10 * v + 10 + faktor <= 199 && a[1] + 10 * v + 10 + faktor <= 199 && a[2] + 10 * v + 10 + faktor <= 199 && a[3] + 10 * v + 10 + faktor <= 199) {
                    if (Spielfeld[a[0] + 10 * v + 10 + faktor] == 1, Spielfeld[a[1] + 10 * v + 10 + faktor] == 1, Spielfeld[a[2] + 10 * v + 10 + faktor] == 1, Spielfeld[a[3] + 10 * v + 10 + faktor] == 1) {
                        Spielfeld[a[0] + 10 * v + faktor] = 1;
                        Spielfeld[a[1] + 10 * v + faktor] = 1;
                        Spielfeld[a[2] + 10 * v + faktor] = 1;
                        Spielfeld[a[3] + 10 * v + faktor] = 1;
                        break;

                    }
                }
                temp = faktor;
                faktor = moveorrotate(faktor, a[0], a[1], a[2], a[3]);
                if (faktor != temp) {
                    continue;
                }
                v = fun(v);
                /*Game Over
                if(Spielfeld[3]==1||Spielfeld[4]==1){
                   for(int j=0; j<200;j++){
                    if(j%10==0){
                        printf("\n");
                    }
                    printf("[%d]",endscreen[j]);
                   }
                   n=1;
                   break;
                }
                */
                /*
                temp=faktor;
                faktor=moveorrotate(faktor);
                if(temp!=faktor){
                    printf("\n");
                    continue;
                }
                */



            }

    }
    return 0;
}
