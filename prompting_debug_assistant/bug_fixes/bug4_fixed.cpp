// bug4_fixed.cpp
// Category: Off-by-One / Loop Logic Issues

#include <iostream>
using namespace std;

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int sum = 0;

    // Fix: start at 0 and stop at i < 5 to avoid skipping arr[0] and accessing arr[5]
    for (int i = 0; i < 5; i++) {
        sum += arr[i];
    }

    cout << "Sum: " << sum << endl;

    // Tests (basic runtime checks)
    if (sum != 15) {
        cerr << "Test failed: expected 15, got " << sum << endl;
        return 1;
    }

    return 0;
}
