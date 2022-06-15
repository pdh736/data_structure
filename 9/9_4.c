#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _simple_stack_t {
    char* stack;
    int size;
    int sp;
} simple_stack_t;

simple_stack_t* init_stack(int size) {
    simple_stack_t* s = (simple_stack_t*)malloc(sizeof(simple_stack_t));
    s->stack = (char*)malloc(size);
    memset(s->stack, 0x00, size);
    s->size = size;
    s->sp = 0;

    return s;
}

void free_stack(simple_stack_t* s) {
    if (s){
        if (s->stack)
            free(s->stack);

        free(s);
    }
}

int push_stack(simple_stack_t* s, char item) {
    if (s->sp == s->size)
        return -1;

    s->stack[s->sp] = item;
    s->sp++;

    return 0;
}

char pop_stack(simple_stack_t* s) {
    if (s->sp == 0)
        return '\0';

    s->sp--;
    char c = s->stack[s->sp];
    s->stack[s->sp] = 0;

    return c;
}

char* reverse_string(char* src) {
    int str_len = strlen(src);

    if (str_len == 0)
        return NULL; 

    char* str = (char*)malloc(str_len);
    memset(str, 0x00, str_len);

    simple_stack_t* stack = init_stack(10);

    for (int i=0; i<str_len; i++) {
        push_stack(stack, src[i]);
    }

    char c;
    int index = 0;

    while(1) {
        c = pop_stack(stack);
        if (c == '\0')
            break;
        str[index] = c;
        index++;
    }

    free_stack(stack);

    return str;
}

int main(int argc, char* argv[]) {
    char* str = reverse_string("abcde");
    if (str) {
        printf("%s\n", str);
        free(str);
    }

    return 0;
}
