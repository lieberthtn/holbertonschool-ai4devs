#include <stdio.h>

int main() {
    int numbers[5] = {1, 2, 3, 4, 5};
    
    // Dövr düzəldildi: i < 5
    for (int i = 0; i < 5; i++) {
        printf("Rəqəm: %d\n", numbers[i]);
    }

    int x = 10;
    int y = 2; // Sıfıra bölmə düzəldildi
    if (y != 0) {
        int z = x / y;
        printf("Nəticə: %d\n", z);
    }

    return 0;
}
