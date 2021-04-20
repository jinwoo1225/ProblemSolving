
#include <iostream>
#include <string>
using namespace std;

int main(void) {
    string line;

    getline(cin, line);
    string ascending = "1 2 3 4 5 6 7 8";
    string descending = "8 7 6 5 4 3 2 1";
    if (line == ascending) {
        cout << "ascending" << '\n';
    } else if (line == descending) {
        cout << "descending" << '\n';
    } else {
        cout << "mixed" << '\n';
    }

    // for (int i = 0; i < 8; i++) {
    //     scanf("%d", a + i);
    // }
}
/*
    for (int i = 0; i < 7; i++) {
        if (a[i + 1] - a[i] != 1)
            {
                printf("mixed");
                exit();
            }
    }
    if (a[0] == 8)
        printf("descending");
    if (a[0] == 1)
        printf("descending");
}*/