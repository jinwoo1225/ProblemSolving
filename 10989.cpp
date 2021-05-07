#include <iostream>

int main(void) {
    int N;

    scanf("%d", &N);

    int arr[10001] = {0};

    int num;
    while (N--) {
        scanf("%d", &num);
        arr[num]++;
    }

    for (int i = 1; i < 10001; i++) {
        for (int j = 0; j < arr[i]; j++) {
            printf("%d\n", i);
        }
    }
}