#include <iostream>

int main() {
    int* ptr; // Səhv: Initialize olunmamış pointer
    *ptr = 100;
    std::cout << *ptr << std::endl;
    return 0;
}
