#include <SFML/Graphics.hpp>
#include <iostream>
#include <vector>

const int GRID_SIZE = 20;
const int GRID_WIDTH = 30;
const int GRID_HEIGHT = 20;
const int WINDOW_WIDTH = GRID_WIDTH * GRID_SIZE;
const int WINDOW_HEIGHT = GRID_HEIGHT * GRID_SIZE;

enum class Direction { UP, DOWN, LEFT, RIGHT };

struct SnakeSegment {
    int x, y;
    SnakeSegment(int xPos, int yPos) : x(xPos), y(yPos) {}
};

class SnakeGame {
private:
    sf::RenderWindow window;
    std::vector<SnakeSegment> snake;
    Direction currentDirection;
    int fruitX, fruitY;
    bool gameOver;

    void generateFruit() {
        fruitX = rand() % GRID_WIDTH;
        fruitY = rand() % GRID_HEIGHT;
    }

    void handleInput() {
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::W) && currentDirection != Direction::DOWN)
            currentDirection = Direction::UP;
        else if (sf::Keyboard::isKeyPressed(sf::Keyboard::S) && currentDirection != Direction::UP)
            currentDirection = Direction::DOWN;
        else if (sf::Keyboard::isKeyPressed(sf::Keyboard::A) && currentDirection != Direction::RIGHT)
            currentDirection = Direction::LEFT;
        else if (sf::Keyboard::isKeyPressed(sf::Keyboard::D) && currentDirection != Direction::LEFT)
            currentDirection = Direction::RIGHT;
    }

    void moveSnake() {
        SnakeSegment head = snake.front();

        switch (currentDirection) {
        case Direction::UP:
            head.y--;
            break;
        case Direction::DOWN:
            head.y++;
            break;
        case Direction::LEFT:
            head.x--;
            break;
        case Direction::RIGHT:
            head.x++;
            break;
        }

        snake.insert(snake.begin(), head);

        if (head.x == fruitX && head.y == fruitY) {
            generateFruit();
        }
        else {
            snake.pop_back();
        }
    }

    bool checkCollision() {
        SnakeSegment head = snake.front();
        for (size_t i = 1; i < snake.size(); ++i) {
            if (snake[i].x == head.x && snake[i].y == head.y)
                return true;
        }

        return head.x < 0 || head.x >= GRID_WIDTH || head.y < 0 || head.y >= GRID_HEIGHT;
    }

    void draw() {
        window.clear();
        sf::RectangleShape cell(sf::Vector2f(GRID_SIZE, GRID_SIZE));
        for (const auto& segment : snake) {
            cell.setPosition(segment.x * GRID_SIZE, segment.y * GRID_SIZE);
            window.draw(cell);
        }

        cell.setFillColor(sf::Color::Red);
        cell.setPosition(fruitX * GRID_SIZE, fruitY * GRID_SIZE);
        window.draw(cell);

        window.display();
    }

public:
    SnakeGame() : window(sf::VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), "Snake Game"), gameOver(false) {
        snake.push_back(SnakeSegment(GRID_WIDTH / 2, GRID_HEIGHT / 2));
        currentDirection = Direction::UP;
        generateFruit();
    }

    void run() {
        while (!gameOver) {
            sf::Event event;
            while (window.pollEvent(event)) {
                if (event.type == sf::Event::Closed)
                    window.close();
            }

            handleInput();

            if (checkCollision())
                gameOver = true;

            moveSnake();
            draw();
        }
    }
};

int main() {
    srand(time(nullptr)); // Initialize random seed

    SnakeGame game;
    game.run();

    return 0;
}
