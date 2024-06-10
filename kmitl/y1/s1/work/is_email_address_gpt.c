#include <stdio.h>
#include <string.h>

int validateEmail(const char *email) {
    int length = strlen(email);
    int hasAtSymbol = 0;
    int hasDot = 0;

    // Check for minimum email length
    if (length < 3) {
        return 0;
    }

    // Check for valid characters and position of '@' and '.'
    for (int i = 0; i < length; i++) {
        char c = email[i];

        // Check for valid characters
        if (!((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9') || c == '_' || c == '-' || c == '.' || c == '@')) {
            return 0;
        }

        if (c == '@') {
            if (hasAtSymbol || i == 0 || i == length - 1) {
                return 0;
            }

            hasAtSymbol = 1;
        }

        if (c == '.' && i != 0 && i != length - 1 && email[i - 1] != '@') {
            hasDot = 1;
        }
    }

    // Check if both '@' and '.' are present in the email
    return (hasAtSymbol && hasDot);
}

int main() {
    char email[100];

    printf("Enter an email address: ");
    fgets(email, sizeof(email), stdin);

    int length = strlen(email);
    if (email[length - 1] == '\n') {
        email[length - 1] = '\0';  // Remove the trailing newline character
    }

    if (validateEmail(email)) {
        printf("The email is valid.\n");
    } else {
        printf("The email is invalid.\n");
    }

    return 0;
}
