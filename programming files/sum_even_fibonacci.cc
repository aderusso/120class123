#include <iostream>

// Bugs Introduced: DML

int main()
{
    int a = 0, b = 1;
    int sum_even = 0;
    // fibonacci sequence stops at 4 million
    while (b < 4000000) {
        // if the current number is even, add it to the sum_even
        if (b % 2 == 0) {
            sum_even += b;
        }
        int temp = b;
        b = a + b;
        a = temp;
    }
    std::cout << sum_even << std::endl;

    return 0;
}

// answer should be 4613732
