#include <stdio.h>

int greatest_number(int len, int* arry) {
    int num = 0;
    for (int i=0;i<len;i++) {
        if (arry[i] > num)
            num = arry[i];
    }
    return num;
}

int main(int argc, char* argv[]) {
    int len = 10;
    int arry[10] = {1, 19, 90, 89, 70, 46, 57, 66, 45, 50};
    printf("greatest number is : %d\n", greatest_number(len, arry));

   return 0;
}
