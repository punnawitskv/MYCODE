#include <stdio.h>
#include <time.h>
#include <windows.h>
#define STAR_COUNT 80
#define screen_x 80
#define screen_y 25

HANDLE wHnd;
CHAR_INFO consoleBuffer[screen_x * screen_y];
COORD bufferSize = {screen_x, screen_y};
COORD characterPos = {0, 0};
SMALL_RECT windowSize = {0, 0, screen_x - 1, screen_y - 1};

HANDLE rHnd;
DWORD fdwMode;
DWORD numEvents = 0;
DWORD numEventsRead = 0;

bool play = true;
COORD star[STAR_COUNT];
const int SHIP_LENGTH = 5;
const char SHIP[SHIP_LENGTH + 1] = ">-0-<";
const int SHIP_X_PADDING = SHIP_LENGTH / 2;
COORD shipPosition;
WORD shipColor = 7;

void setMode() {
    rHnd = GetStdHandle(STD_INPUT_HANDLE);
    fdwMode = ENABLE_EXTENDED_FLAGS | ENABLE_WINDOW_INPUT | ENABLE_MOUSE_INPUT;
    SetConsoleMode(rHnd, fdwMode);
}


int setConsole(int x, int y)
{
    wHnd = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleWindowInfo(wHnd, TRUE, &windowSize);
    SetConsoleScreenBufferSize(wHnd, bufferSize);
}

void clear_buffer()
{
    for (int y = 0; y < screen_y; ++y) 
    {
        for (int x = 0; x < screen_x; ++x) 
        {
            consoleBuffer[x + screen_x * y].Char.AsciiChar = ' ';
            consoleBuffer[x + screen_x * y].Attributes = 7;
        }
    }
}

void fill_buffer_to_console()
{
    WriteConsoleOutputA(wHnd, consoleBuffer, bufferSize, characterPos, &windowSize);
}

void init_star()
{
    for (int i = 0; i < STAR_COUNT; i++) 
    {
        star[i].X = rand() % screen_x;
        star[i].Y = rand() % screen_y;
    }
}

void star_fall()
{
    for (int i = 0; i < STAR_COUNT; i++) 
    {
        if (star[i].Y >= screen_y - 1) 
        {
            star[i].X = (rand() % screen_x);
            star[i].Y = 1;
        } else 
        {
            star[i].Y++;
        }
    }
}

void draw_star_to_buffer() 
{
    for (int i = 0; i < STAR_COUNT; i++) {
        consoleBuffer[star[i].X + screen_x * star[i].Y].Char.AsciiChar = '*';
    }
}

void fill_star_to_buffer()
{
    for (int i = 0; i < STAR_COUNT; i++) 
    {
        consoleBuffer[star[i].X + screen_x * star[i].Y].Char.AsciiChar = '*';
    }
}

void randomShipColor() 
{
    shipColor = rand() % 65535;
}

void updateShipPosition(int x, int y) {
    if (x > (screen_x - SHIP_X_PADDING - 1)) {
        x = screen_x - SHIP_X_PADDING - 1;
    }
    else if (x < SHIP_X_PADDING) {
        x = SHIP_X_PADDING;
    }

    if (y > screen_y - 1) {
        y = screen_y - 1;
    }
    shipPosition.X = x;
    shipPosition.Y = y;
}

void drawShipToBuffer(int x, int y)
{
    int halfShipLength = SHIP_LENGTH / 2;
    for (int i = -halfShipLength; i <= halfShipLength; i++) {
        consoleBuffer[(x - i) + (screen_x * y)].Char.AsciiChar = SHIP[i + halfShipLength];
        consoleBuffer[(x - i) + (screen_x * y)].Attributes = shipColor;
    }
}

bool checkCollision() {
    int halfShipLength = SHIP_LENGTH / 2;
    bool collision = false;
    for (int i = -halfShipLength; i <= halfShipLength; i++) {
        if (consoleBuffer[(shipPosition.X - i) + ((screen_x * shipPosition.Y))].Char.AsciiChar == '*') {
            collision = true;
            break;
        }
    }
    return collision;
}

int main()
{
    bool play = true;
    DWORD numEvents = 0;
    DWORD numEventsRead = 0;
    setConsole(screen_x, screen_y);
    setMode();
    init_star();
    int hp = 10;
    int dm= 0;
    while (play)
    {
        clear_buffer();
        GetNumberOfConsoleInputEvents(rHnd, &numEvents);
        if (numEvents != 0) 
        {
            INPUT_RECORD* eventBuffer = new INPUT_RECORD[numEvents];
            ReadConsoleInput(rHnd, eventBuffer, numEvents, &numEventsRead);
            for (DWORD i = 0; i < numEventsRead; ++i) 
            {
                if (eventBuffer[i].EventType == KEY_EVENT && eventBuffer[i].Event.KeyEvent.bKeyDown == true ) 
                {
                    if (eventBuffer[i].Event.KeyEvent.wVirtualKeyCode == VK_ESCAPE) 
                    {
                        play = false;
                        //printf("press : %c\n", eventBuffer[i].Event.KeyEvent.uChar.AsciiChar);
                    }
                    else if (eventBuffer[i].Event.KeyEvent.uChar.AsciiChar == 'c') 
                    {
                        randomShipColor();
                    }
                }
                else if (eventBuffer[i].EventType == MOUSE_EVENT) 
                {
                    int posx = eventBuffer[i].Event.MouseEvent.dwMousePosition.X;
                    int posy = eventBuffer[i].Event.MouseEvent.dwMousePosition.Y;

                    if (eventBuffer[i].Event.MouseEvent.dwButtonState & FROM_LEFT_1ST_BUTTON_PRESSED) 
                    {
                        //printf("left click\n");
                    }
                    else if (eventBuffer[i].Event.MouseEvent.dwButtonState & RIGHTMOST_BUTTON_PRESSED) 
                    {
                        //printf("right click\n");
                    }
                    else if (eventBuffer[i].Event.MouseEvent.dwEventFlags & MOUSE_MOVED) 
                    {
                        updateShipPosition(posx,posy);
                        //printf("mouse position : (%d,%d)\n",posx, posy);
                    }
                }
            }
            delete[] eventBuffer;
        }
        drawShipToBuffer(shipPosition.X, shipPosition.Y);
        star_fall();
        draw_star_to_buffer();
        if(checkCollision()) 
        {
            hp--;
            if (hp <= 0) {
                play = false;
            }
        }
        fill_buffer_to_console();
        Sleep(50);
    }
    return 0;
}