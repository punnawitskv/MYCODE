#include "raylib.h"
#include <vector>
#include <algorithm>

int main() {
    // Initialize Raylib
    InitWindow(800, 600, "Number Sorting Program");

    // Create a vector to store ten numbers
    std::vector<int> numbers;

    // Receive ten numbers from the user
    for (int i = 0; i < 10; i++) {
        int num;
        char prompt[256];
        sprintf(prompt, "Enter number %d:", i + 1);
        num = GetRandomValue(1, 100);  // For testing, you can use GetRandomValue to generate random numbers
        numbers.push_back(num);
    }

    // Open a file for writing the numbers
    FILE* file = fopen("numbers.txt", "w");
    if (file == NULL) {
        TraceLog(LOG_ERROR, "Error opening the file");
        CloseWindow();
        return 1;
    }

    // Write the numbers to the file
    for (int num : numbers) {
        fprintf(file, "%d\n", num);
    }

    // Close the file
    fclose(file);

    // Open the file for reading and sorting
    file = fopen("numbers.txt", "r");
    if (file == NULL) {
        TraceLog(LOG_ERROR, "Error opening the file");
        CloseWindow();
        return 1;
    }

    // Read the numbers from the file and store in a list
    std::vector<int> readNumbers;
    int num;
    while (fscanf(file, "%d", &num) == 1) {
        readNumbers.push_back(num);
    }

    // Sort the numbers in ascending order
    std::sort(readNumbers.begin(), readNumbers.end());

    // Close the file
    fclose(file);

    // Close Raylib
    CloseWindow();

    // Display the sorted numbers
    for (int num : readNumbers) {
        printf("%d ", num);
    }
    printf("\n");

    return 0;
}
