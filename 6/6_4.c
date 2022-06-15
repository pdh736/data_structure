#include <stdio.h>
#include <string.h>

int contains_X(char* str) {
    int found = 0;

    for (int i=0;i<strlen(str);i++) {
        if (str[i] == 'X')
            return 1;
    }
    return 0;
}



int main (int argc, char* argv[]) {
    char* str = "hahahaX";

    if (contains_X(str)) {
        printf("contain\n");
    }
    else {
        printf("no contain\n");
    }

    return 0;
}
