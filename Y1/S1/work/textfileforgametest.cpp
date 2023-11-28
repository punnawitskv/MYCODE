#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int main() {
    // Create a variable to store ten numbers.
    std::vector<int> numbers;

    // Receive ten numbers from the user.
    for (int i = 0; i < 10; i++) {
        int num;
        std::cout << "Enter number " << i + 1 << ": ";
        std::cin >> num;
        numbers.push_back(num);
    }

    // Open a file for writing the numbers.
    std::ofstream outputFile("numbers.txt");
    if (!outputFile.is_open()) {
        std::cerr << "Error opening the file." << std::endl;
        return 1;
    }

    // Write the numbers to the file.
    for (int num : numbers) {
        outputFile << num << std::endl;
    }

    // Close the file.
    outputFile.close();

    // Open the file for reading and sorting.
    std::ifstream inputFile("numbers.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Error opening the file." << std::endl;
        return 1;
    }

    // Read the numbers from the file and store in a list.
    std::vector<int> readNumbers;
    int num;
    while (inputFile >> num) {
        readNumbers.push_back(num);
    }

    // Sort the numbers in ascending order.
    std::sort(readNumbers.begin(), readNumbers.end());

    // Display the sorted numbers.
    std::cout << "Numbers sorted in ascending order:" << std::endl;
    for (int num : readNumbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Close the file.
    inputFile.close();

    return 0;
}
