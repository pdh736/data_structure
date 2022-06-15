#include <stdio.h>

int sum(int low, int high) {
    if (high == low)
        return low;

    return high + sum(low, high-1);
}

int main(int argc, char* argv[]) {
    printf("%d\n", sum(1,10));

    return 0;
}
