#include <stdio.h>
#include <windows.h>
#include <conio.h>

void setcursor(bool visible);
void gotoxy(int x, int y);
void draw_ship(int x, int y);
void erase_ship(int x, int y);
void setcolor(int fg, int bg);
void draw_bullet(int x, int y);
void erase_bullet(int x, int y);

const int SHIP_LENGTH = 7;
const int SHIP_WIDTH = 1;
const int SCREEN_WIDTH = 80;
const int SCREEN_HEIGHT = 24;
const int MAX_BULLETS = 5;

int main() {
    // clear screen
    system("cls");

    // hide cursor
    setcursor(false);

    // Set initial color to green (foreground: green, background: black)
    setcolor(0, 0);

    char ch = '\0';
    char lastPressed = ch;
    int x = 37, y = 20;

    int bulletsX[MAX_BULLETS], bulletsY[MAX_BULLETS];
    for (int i = 0; i < MAX_BULLETS; i++) {
        bulletsX[i] = -1;
        bulletsY[i] = -1;
    }
    int bulletsInFlight = 0;

    draw_ship(x, y);

    // move ship
    do {
        //
        if (_kbhit()) {
            ch = _getch();
            if (ch == 'a' || ch == 'd' || ch == 'x' || ch == 'w') lastPressed = ch;
            if (ch == 's') lastPressed = '\0';
            if (ch == ' ' && bulletsInFlight <= MAX_BULLETS) {
                bulletsInFlight++;
                for (int i = 0; i < MAX_BULLETS; i++) {
                    if (bulletsX[i] == -1 && bulletsY[i] == -1) {
                        bulletsX[i] = x + (SHIP_LENGTH / 2);
                        bulletsY[i] = y - 1;
                        break;
                    }
                }
            }
            fflush(stdin);
        }

        // update frame
        if (bulletsInFlight > 0) {
            for (int i = 0; i < MAX_BULLETS; i++) {
                if (bulletsX[i] != -1 && bulletsY[i] != -1) {
                    erase_bullet(bulletsX[i], bulletsY[i]);
                    bulletsY[i]--;
                    draw_bullet(bulletsX[i], bulletsY[i]);
                }

                if (bulletsY[i] == 0) {
                    erase_bullet(bulletsX[i], bulletsY[i]);
                    bulletsX[i] = -1;
                    bulletsY[i] = -1;
                    bulletsInFlight--;
                }
            }
        }
        
        if (lastPressed == 'a') {
                if (x > 0) {
                    erase_ship(x, y);
                    draw_ship(--x, y);
                }
            }
    
        if (lastPressed == 'd') {
            if (x < 73) {
                erase_ship(x, y);
                draw_ship(++x, y);
            }
        }

        if (lastPressed == 'w') {
            if (y > 0) {
                erase_ship(x, y);
                draw_ship(x, --y);
            }
        }

        if (lastPressed == 'x') {
            if (y <= 23) {
                erase_ship(x, y);
                draw_ship(x, ++y);
            }
        }

        Sleep(50); // Adjust the delay for smoother movement
        // exit
    } while (ch != 'z');
    return 0;
}

void gotoxy(int x, int y) {
    COORD c = {(short)x, (short)y};
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
}

void draw_ship(int x, int y)
{
    gotoxy(x, y);
    setcolor(2, 4);
    printf(" <-0-> ");
}

void erase_ship(int x, int y)
{
    setcolor(0,0);
    gotoxy(x, y);
    printf("       ");
}

void setcolor(int fg, int bg)
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, bg * 16 + fg);
}

void setcursor(bool visible) {
    HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_CURSOR_INFO lpCursor;
    lpCursor.bVisible = visible;
    lpCursor.dwSize = 20;
    SetConsoleCursorInfo(console, &lpCursor);
}

void draw_bullet(int x, int y) {
    setcolor(9, 0);
    gotoxy(x, y);
    printf("o");
}

void erase_bullet(int x, int y) {
    setcolor(0, 0);
    gotoxy(x, y);
    printf(" ");
}