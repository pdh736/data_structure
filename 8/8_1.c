#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* get_intersection (int* ary1, int ary1_len, int* ary2, int ary2_len, int* inter_size) {
    int tmp[10] = {0,};
    
    for (int i = 0; i < ary1_len; i++) {
        tmp[ary1[i]] = 1;
    }

    int cnt = 0;
    int* intersection = (int*)malloc(sizeof(int)*ary1_len);
    memset(intersection, 0x00, sizeof(int)*ary1_len);
    for (int i = 0; i < ary2_len; i++) {
        if (tmp[ary2[i]]) {
            intersection[cnt] = ary2[i];
            cnt++;
        }
    }

    *inter_size = cnt;

    if (!cnt) {
        free(intersection);
        return NULL;
    }

    return intersection;
}

int main (int argc, char* argv[]) {
    int ary1[5] = {1, 2, 3, 4, 5};
    int ary1_len = 5;
    int ary2[5] = {0, 2, 4, 6, 8};
    int ary2_len = 5;
    
    int size = 0;
    int* intersection = get_intersection(ary1, ary1_len, ary2, ary2_len, &size);
    if (intersection) {
        for (int i = 0; i < size; i++) {
            printf("%d ", intersection[i]);
        }
        printf("\n");
        free(intersection);
    }
    else {
        printf("there are no intersection\n");
    }

    return 0;
}
