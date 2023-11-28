#include <raylib.h>

int frame{};
const float updateTime{1.f / 12.f};
float runningTime{};
int velocity{};
int scale{2};

int main()
{
    const int screenWidth = 661 * scale;
    const int screenHeight = 300 * scale;

    InitWindow(screenWidth, screenHeight, "Ghost Hunt");

    Texture2D background = LoadTexture("old-dark-castle-interior-background.png");
    Texture2D ghostTexture = LoadTexture("ghost-idle.png");

    Rectangle player = {0, 0, 1, 1};

    const int maxGhosts = 20;
    Rectangle ghosts[maxGhosts];
    int ghostSpeedsX[maxGhosts];
    int ghostSpeedsY[maxGhosts];
    float ghostTimers[maxGhosts];
    const float ghostSpawnTime = 5.0f;
    const float ghostChangeDirTime = 0.75f;
    int activeGhosts = 1;
    bool ghostActive[maxGhosts]{};
    float ghostWidth = ghostTexture.width / 7;
    float ghostHeight = ghostTexture.height;

    for (int i = 0; i < maxGhosts; i++)
    {
        ghosts[i] = {GetRandomValue(0, screenWidth - 60), GetRandomValue(0, screenHeight - 120), 60, 120};
        ghostSpeedsX[i] = GetRandomValue(2, 4) * (GetRandomValue(0, 1) == 0 ? 1 : -1);
        ghostSpeedsY[i] = GetRandomValue(2, 4) * (GetRandomValue(0, 1) == 0 ? 1 : -1);
    }

    Rectangle crosshair = {0, 0, 30, 30};
    Color crosshairColor = YELLOW;

    bool gameOver = false;

    int score = 0;

    SetTargetFPS(60);

    while (!WindowShouldClose())
    {
        velocity = 0;

        if (!gameOver)
        {
            runningTime += GetFrameTime();
            if (runningTime >= updateTime)
            {
                frame++;
                runningTime = 0;
                if (frame >= 7)
                {
                    frame = 0;
                }
            }

            if (IsKeyDown(KEY_D) || IsKeyDown(KEY_RIGHT))
                player.x += 5;
            if (IsKeyDown(KEY_A) || IsKeyDown(KEY_LEFT))
                player.x -= 5;
            if (IsKeyDown(KEY_S) || IsKeyDown(KEY_DOWN))
                player.y += 5;
            if (IsKeyDown(KEY_W) || IsKeyDown(KEY_UP))
                player.y -= 5;

// Update ghost spawning and movement
for (int i = 0; i < activeGhosts; i++)
{
    if (!ghostActive[i])
    {
        ghostTimers[i] += GetFrameTime() * 1000; // Convert to milliseconds
        if (ghostTimers[i] >= ghostSpawnTime * 1000)
        {
            ghostTimers[i] = 0.0f;
            ghostActive[i] = true;
            activeGhosts++;
            ghosts[i].x = GetRandomValue(0, screenWidth - ghosts[i].width);
            ghosts[i].y = GetRandomValue(0, screenHeight - ghosts[i].height);
        }
    }
    else
    {
        ghostTimers[i] += GetFrameTime();
        if (ghostTimers[i] >= ghostChangeDirTime)
        {
            ghostTimers[i] = 0.0f;
            ghostSpeedsX[i] = GetRandomValue(-1, 1);
            ghostSpeedsY[i] = GetRandomValue(-1, 1);
        }

        ghosts[i].x += ghostSpeedsX[i];
        ghosts[i].y += ghostSpeedsY[i];
        velocity += ghostSpeedsX[i];

        if (ghosts[i].x + ghosts[i].width < 0 || ghosts[i].x > screenWidth || ghosts[i].y + ghosts[i].height < 0 || ghosts[i].y > screenHeight)
        {
            ghostActive[i] = false;
        }
        else if (ghosts[i].x + ghosts[i].width > screenWidth)
        {
            ghostSpeedsX[i] = -ghostSpeedsX[i];
            ghosts[i].x = screenWidth - ghosts[i].width;
        }
        else if (ghosts[i].x < 0)
        {
            ghostSpeedsX[i] = -ghostSpeedsX[i];
            ghosts[i].x = 0;
        }
        if (ghosts[i].y + ghosts[i].height > screenHeight)
        {
            ghostSpeedsY[i] = -ghostSpeedsY[i];
            ghosts[i].y = screenHeight - ghosts[i].height;
        }
        else if (ghosts[i].y < 0)
        {
            ghostSpeedsY[i] = -ghostSpeedsY[i];
            ghosts[i].y = 0;
        }
    }
}

        }

        crosshair.x = player.x + player.width / 2 - crosshair.width / 2;
        crosshair.y = player.y + player.height / 2 - crosshair.height / 2;

        BeginDrawing();
        ClearBackground(BLACK);

        DrawTextureEx(background, {0, 0}, 0.f, scale, WHITE);

        DrawRectangleRec(player, BLANK);

        // Draw all active ghosts
        for (int i = 0; i < activeGhosts; i++)
        {
            if (ghostActive[i])
            {
                float faceRight = -1.f;
                if (ghostSpeedsX[i] > 0)
                {
                    faceRight = -1.f;
                }
                else
                {
                    faceRight = 1.f;
                }
                Rectangle source{frame * ghostWidth, 0.f, faceRight * ghostWidth, ghostHeight};
                DrawTexturePro(ghostTexture, source, {ghosts[i].x, ghosts[i].y, ghostWidth * 2, ghostHeight * 2}, {0.f, 0.f}, 0.f, WHITE);
            }
        }

        DrawRectangle(crosshair.x - 10, crosshair.y + crosshair.height / 2 - 1, 10, 3, crosshairColor);
        DrawRectangle(crosshair.x + crosshair.width, crosshair.y + crosshair.height / 2 - 1, 10, 3, crosshairColor);

        DrawRectangle(crosshair.x + crosshair.width / 2 - 1, crosshair.y - 10, 3, 10, crosshairColor);
        DrawRectangle(crosshair.x + crosshair.width / 2 - 1, crosshair.y + crosshair.height, 3, 10, crosshairColor);

        DrawText(TextFormat("Score: %d", score), 10, 10, 20, GREEN);

        if (gameOver)
        {
            DrawText("Game Over! Press Enter to Restart.", 250, screenHeight / 2, 20, DARKGRAY);
        }
        velocity = 0;
        EndDrawing();
    }

    CloseWindow();
    return 0;
}
