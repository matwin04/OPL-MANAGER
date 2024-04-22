#include "raylib.h"
#include <iostream>
using namespace std;
int main() {
    const int screenWidth = 800;
    const int screenHeight = 450;

    InitWindow(screenWidth, screenHeight, "TapeMaser");

    SetTargetFPS(60);
    while (!WindowShouldClose()) {
        BeginDrawing();
            ClearBackground(RAYWHITE);
            DrawText("OPL MANAGER", 190, 200, 20, BLACK);
            DrawText("PS2 game collection database", 190, 250, 20, BLACK);
            DrawText("By Frostie Studios", 190,300,15, BLACK);
        EndDrawing();
    }
    CloseWindow();
    return 0;
}