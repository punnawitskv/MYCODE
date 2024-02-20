#include <stdio.h>

int countLeapYears(int startYear, int endYear) {
    int count = 0;

    // Adjusting the startYear if it includes the year 0
    if (startYear <= 0)
        startYear = 1;

    // Adjusting the endYear if it is less than the startYear
    if (endYear < startYear)
        return count;

    // Counting the number of leap years
    int leapYears = (endYear / 4) - (endYear / 100) + (endYear / 400);
    if (startYear > 0)
        leapYears -= (startYear - 1) / 4 - (startYear - 1) / 100 + (startYear - 1) / 400;

    count = leapYears;

    // Adjusting the count if the range includes the year 0
    if (startYear <= 0 && endYear >= 0 && (startYear % 4 == 0 || endYear % 4 == 0))
        count++;

    return count;
}

int main() {
    int startYear, endYear;

    printf("");
    scanf("%d", &startYear);

    printf("");
    scanf("%d", &endYear);

    int leapYearCount = countLeapYears(startYear, endYear);

    printf("%d", leapYearCount);

    return 0;
}
