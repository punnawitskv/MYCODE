#include<stdio.h>
#include<windows.h>
#include<time.h>
#include<conio.h>

void setcursor(bool visible);
char cursor(int x, int y) ;
void gotoxy(int x, int y);
void draw_ship(int x, int y);
void draw_bullet(int x, int y);
void clear(int x, int y);
void draw_star();
void draw_score(int score);

int main()
{
    setcursor(false);

	//random
	srand(time(NULL));
	for (int i = 0; i < 20; ++i) {
		draw_star();
	}

	//score
	int score = 0;

	//logic
	char ch = '\0';
	int x = 38, y = 20;
	int bx, by, i;
	int bullet = 0;
	draw_ship(x, y);
	do {
		if (_kbhit()) {
			ch = _getch();
			if (ch == 'a') { draw_ship(--x, y); }
			if (ch == 's') { draw_ship(++x, y); }
			if (bullet != 1 && ch == ' ') { bullet = 1; bx = x + 3; by = y - 1; }
			fflush(stdin);
		}
		if (bullet == 1) {
			clear(bx, by);
			if (by == 2) { bullet = 0; }
			else { 
				if (cursor(bx, by - 1) == '*') {
					Beep(1000, 200);
					clear(bx, by - 1);
					score++;
					draw_star();
				}
				draw_bullet(bx, --by); 
			}
		}
		draw_score(score);
		Sleep(50);
	} while (ch != 'x');
	return 0;
}

void setcursor(bool visible) {
    HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_CURSOR_INFO lpCursor;
    lpCursor.bVisible = visible;
    lpCursor.dwSize = 20;
    SetConsoleCursorInfo(console, &lpCursor);
}

char cursor(int x, int y) 
{
	HANDLE hStd = GetStdHandle(STD_OUTPUT_HANDLE);
	char buf[2]; COORD c = { x,y }; DWORD num_read;
	if (!ReadConsoleOutputCharacter(hStd, (LPTSTR)buf, 1, c, (LPDWORD)&num_read))
		return '\0';
	else
		return buf[0];
}

void gotoxy(int x, int y)
{
	COORD c = { x, y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
}

void draw_ship(int x, int y)
{
	gotoxy(x, y); printf(" <-0-> ");
}

void draw_bullet(int x, int y)
{
	gotoxy(x, y); printf("|");
}

void clear(int x, int y)
{
	gotoxy(x, y); printf(" ");
}

void draw_star()
{
	int x = rand() % 61 + 10;
	int y = rand() % 4 + 2;
	gotoxy(x, y); printf("*");
}

void draw_score(int score)
{
	gotoxy(68, 1); printf("score: %d", score);
}