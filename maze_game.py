import pygame
import sys
from pygame.math import Vector2
from enum import Enum
import os

# Inisialisasi Pygame
pygame.init()

# Konstanta
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
CELL_SIZE = 40
BG_COLOR = (255, 203, 203)
PLAYER_COLOR = (22, 121, 171)
EXIT_COLOR = (255, 177, 55)
OBSTACLE_COLOR = (16, 44, 87)
MENU_COLOR = (255, 0, 0)
WIN_COLOR = (0, 255, 0)

# Enum untuk status game
class GameState(Enum):
    RUNNING = 1
    WIN = 2
    MENU = 3

# Kelas karakter (Player)
class Player:
    def __init__(self, pos):
        self.pos = pos

    def move(self, direction):
        new_pos = self.pos + direction
        if self.is_valid_move(new_pos):
            self.pos = new_pos
            return False
        return True

    def is_valid_move(self, new_pos):
        if new_pos.x < 0 or new_pos.x >= SCREEN_WIDTH // CELL_SIZE or new_pos.y < 0 or new_pos.y >= SCREEN_HEIGHT // CELL_SIZE:
            return False
        for obstacle in obstacles:
            if obstacle.colliderect(pygame.Rect(new_pos.x * CELL_SIZE, new_pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)):
                return False
        return True

# Kelas pintu keluar (Exit)
class Exit:
    def __init__(self, pos):
        self.pos = pos

# Kelas utama game (Maze Game dengan FSA)
class MazeGameFSA:
    def __init__(self):
        self.player = Player(Vector2(1, 1))
        self.exit = Exit(Vector2(9, 9))  
        self.current_state = GameState.RUNNING
        self.font = pygame.font.SysFont('Arial', 36)
        print("Current State:", self.current_state)




    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            pygame.display.flip()
            pygame.time.delay(1000 // FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if self.current_state == GameState.RUNNING:
                    if event.key == pygame.K_UP:
                        if self.player.move(Vector2(0, -1)):
                            self.current_state = GameState.MENU
                    elif event.key == pygame.K_DOWN:
                        if self.player.move(Vector2(0, 1)):
                            self.current_state = GameState.MENU
                    elif event.key == pygame.K_LEFT:
                        if self.player.move(Vector2(-1, 0)):
                            self.current_state = GameState.MENU
                    elif event.key == pygame.K_RIGHT:
                        if self.player.move(Vector2(1, 0)):
                            self.current_state = GameState.MENU

    def update(self):
        if self.current_state == GameState.RUNNING:
            if self.player.pos == self.exit.pos:
                self.current_state = GameState.WIN
                print("Current State:", self.current_state)

    def render(self):
        screen.fill(BG_COLOR)
        if self.current_state == GameState.MENU:
            screen.fill(MENU_COLOR)
            text_surface = self.font.render('Game Over!', True, (0, 0, 0))
            screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT // 2 - text_surface.get_height() // 2))
            self.current_state = GameState.MENU
            pygame.display.flip()
            pygame.time.delay(2000) 
            pygame.quit()
            os.system('python .\\main.py')  
            sys.exit()
        elif self.current_state == GameState.WIN:
            screen.fill(WIN_COLOR)
            text_surface = self.font.render('You Win!', True, (0, 0, 0))
            screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT // 2 - text_surface.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            os.system('python .\\main.py') 
            sys.exit()
        else:
            pygame.draw.rect(screen, PLAYER_COLOR, (self.player.pos.x * CELL_SIZE, self.player.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, EXIT_COLOR, (self.exit.pos.x * CELL_SIZE, self.exit.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            for obstacle in obstacles:
                pygame.draw.rect(screen, OBSTACLE_COLOR, obstacle)

# Inisialisasi layar Pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Raioniee Maze Game")
clock = pygame.time.Clock()

# Tambahkan beberapa rintangan
obstacles = [
    pygame.Rect(3 * CELL_SIZE, 0 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(4 * CELL_SIZE, 0 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(5 * CELL_SIZE, 0 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(5 * CELL_SIZE, 1 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(7 * CELL_SIZE, 1 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(9 * CELL_SIZE, 1 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(10 * CELL_SIZE, 1 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(11 * CELL_SIZE, 1 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(12 * CELL_SIZE, 1 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(3 * CELL_SIZE, 2 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(7 * CELL_SIZE, 2 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(9 * CELL_SIZE, 2 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(12 * CELL_SIZE, 2 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 1* CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect(2 * CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 3* CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 4* CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 6* CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 7* CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 9* CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 4* CELL_SIZE, 4 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 6* CELL_SIZE, 4 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 9* CELL_SIZE, 4 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 10* CELL_SIZE, 4 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 11* CELL_SIZE, 4 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 13* CELL_SIZE, 4 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 14* CELL_SIZE, 4 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 2* CELL_SIZE, 5 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 6* CELL_SIZE, 5 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 8* CELL_SIZE, 5 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 9* CELL_SIZE, 5 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 11* CELL_SIZE, 5 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 0* CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 1* CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 2* CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 3* CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 4* CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 5* CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 6* CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 11* CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 12* CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 9* CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 10* CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 11 * CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 1* CELL_SIZE, 8 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 2* CELL_SIZE, 8 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 3* CELL_SIZE, 8 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 4* CELL_SIZE, 8 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 5* CELL_SIZE, 8 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 6* CELL_SIZE, 8 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 7* CELL_SIZE, 8 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 8* CELL_SIZE, 8 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 9* CELL_SIZE, 8 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 11* CELL_SIZE, 9 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 12* CELL_SIZE, 9 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 13* CELL_SIZE, 9 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 14* CELL_SIZE, 9 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 3* CELL_SIZE, 9 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 0* CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 1* CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 3* CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 4* CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 5* CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 6* CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 7* CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 9* CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 10* CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 11* CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 12* CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 14* CELL_SIZE,  1* CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 14* CELL_SIZE,  2* CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 14* CELL_SIZE,  3* CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 14* CELL_SIZE,  6* CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 14* CELL_SIZE,  7* CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 14* CELL_SIZE,  8* CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 14* CELL_SIZE,  10* CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 14* CELL_SIZE,  11* CELL_SIZE, CELL_SIZE, CELL_SIZE),
    pygame.Rect( 5* CELL_SIZE,  11* CELL_SIZE, CELL_SIZE, CELL_SIZE),






    # pygame.Rect(0 * CELL_SIZE, 1 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(4 * CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(5 * CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(6 * CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(7 * CELL_SIZE, 3 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(3 * CELL_SIZE, 4 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(3 * CELL_SIZE, 5 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(3 * CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(7 * CELL_SIZE, 4 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(7 * CELL_SIZE, 5 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(7 * CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(4 * CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(5 * CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    # pygame.Rect(0 * CELL_SIZE, 6 * CELL_SIZE, CELL_SIZE, CELL_SIZE),
]

# Main program
if __name__ == "__main__":
    game = MazeGameFSA()
    game.run()