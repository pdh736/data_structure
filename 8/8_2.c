#include <stdio.h>
#include <string.h>

char get_dup_char(char* str) {
    char tmp[26] = {0, };
    for(int i = 0; i < strlen(str); i++) {
        if(tmp[str[i]-97])
            return str[i];
        tmp[str[i]-97] = 1;
    }
    return '\0';
}

int main(int argc, char* argv[]) {
    printf("dup char : %c\n", get_dup_char("abcdciop"));
    return 0;
}

