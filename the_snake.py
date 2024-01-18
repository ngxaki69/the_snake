from random import choice, randint


import pygame

# Инициализация PyGame:
pygame.init()

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
all_direction = {
    (pygame.K_UP, UP): UP,
    (pygame.K_UP, LEFT): UP,
    (pygame.K_UP, RIGHT): UP,
    (pygame.K_DOWN, DOWN): DOWN,
    (pygame.K_DOWN, LEFT): DOWN,
    (pygame.K_DOWN, RIGHT): DOWN,
    (pygame.K_LEFT, LEFT): LEFT,
    (pygame.K_LEFT, UP): LEFT,
    (pygame.K_LEFT, DOWN): LEFT,
    (pygame.K_RIGHT, RIGHT): RIGHT,
    (pygame.K_RIGHT, UP): RIGHT,
    (pygame.K_RIGHT, DOWN): RIGHT,
}
# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 10

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


class GameObject:
    """Базовый класс."""

    def __init__(self):
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = None

    def draw(self):
        """Метод для отрисовки."""
        pass

    def draw_cell(self, surface, position):
        """Метод отрисовки объектов."""
        rect = (
            pygame.Rect((position[0], position[1]), (GRID_SIZE, GRID_SIZE))
        )
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(surface, BORDER_COLOR, rect, 1)


class Apple(GameObject):
    """Дочерний класс, описывающий яблоко."""

    def __init__(self):
        super().__init__()
        self.position = self.randomize_position()
        self.body_color = (255, 0, 0)

    def randomize_position(self):
        """Метод задающий рандомные координаты на поле для яблока."""
        return ((randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                randint(0, GRID_HEIGHT - 1) * GRID_SIZE))

    def draw(self, surface):
        """Метод отрисовки яблока."""
        self.draw_cell(surface, self.position)


class Snake(GameObject):
    """Дочерний класс, описывающий змею."""

    def __init__(self):
        super().__init__()
        self.positions = self.position
        self.reset()
        self.body_color = (0, 255, 0)

    def update_direction(self, direction):
        """Метод обновления направления движения змейки."""
        self.direction = direction

    def move(self):
        """Метод обновления позиции каждой секции."""
        head = self.get_head_position()
        dx, dy = self.direction
        new_head = (((head[0] + (dx * GRID_SIZE)) % SCREEN_WIDTH),
                    (head[1] + (dy * GRID_SIZE)) % SCREEN_HEIGHT)
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.last = self.positions.pop()

    def draw(self, surface):
        """Метод отрисовки змейки."""
        for position in self.positions[:-1]:
            self.draw_cell(surface, position)
# Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.body_color, head_rect)
        pygame.draw.rect(surface, BORDER_COLOR, head_rect, 1)

# Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(
                (self.last[0], self.last[1]),
                (GRID_SIZE, GRID_SIZE)
            )
            pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Метод, возвращает координаты головы змейки."""
        return self.positions[0]

    def reset(self):
        """Сбрасывание змейки в начальное состояние."""
        self.length = 1
        self.positions = [self.position]
        self.direction = choice([UP, DOWN, LEFT, RIGHT])
        screen.fill(BOARD_BACKGROUND_COLOR)


# Тут опишите все классы игры.
def handle_keys(game_object):
    """Метод обработки нажатий клавиш пользователя."""
    global SPEED
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                         and event.key == pygame.K_ESCAPE):
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_PAGEUP:
            SPEED += 10
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_PAGEDOWN:
            SPEED -= 10
        elif event.type == pygame.KEYDOWN:
            if (event.key, game_object.direction) in some_dict.keys():
                game_object.update_direction(some_dict[event.key,
                                                       game_object.direction])


def main():
    """Метод с основной логикой."""
    # Тут нужно создать экземпляры классов.
    apple = Apple()
    snake = Snake()
    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.move()
        if (len(snake.positions) > 2
                and snake.positions[0] in snake.positions[2:]):
            snake.reset()
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.position = apple.randomize_position()
        snake.draw(screen)
        apple.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
