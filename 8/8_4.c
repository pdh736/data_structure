#include <stdio.h>
#include <string.h>

char get_no_dup_char(char* str) {
    char tmp[26] = {0, };
    for(int i = 0; i < strlen(str); i++) {
        if(str[i] < 'a' && str[i] > 'z')
            continue;

        tmp[str[i]-97]++;
    }

    for(int i =0; i < 26; i++) {
        if(tmp[i] == 1) {
            return i+97;
        }
    }
    return '\0';
}

int main(int argc, char* argv[]) {
    printf("no dup char : %c\n", get_no_dup_char("minimum"));
    return 0;
}

