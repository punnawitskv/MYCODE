#include <stdio.h>
#include <windows.h>
#include<conio.h>

void gotoxy(int x, int y) {

    COORD c = { x, y };
    SetConsoleCursorPosition(
    GetStdHandle(STD_OUTPUT_HANDLE) , c);

}

void draw_ship(int x, int y) {
    printf(" <-0-> ");
}

int main() {
    gotoxy(10,15);
    draw_ship();
    scanf("%d");
    return 0;
}