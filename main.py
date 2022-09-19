import pygame
import random

from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Nyonde")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

mixer.music.load("background.mp3")
mixer.music.play(-1)

bird_img = pygame.image.load("nyonde.png")
bird_x = 35
bird_y = 280
bird_y_change = 0

obstacle_img = pygame.image.load("obstacle.png")
obstacle_x = 300
obstacle_y = random.randint(0, 536)
obstacle_x_change = 0.5
diff_two_obstacles = 280

obstacle_img_2 = pygame.image.load("obstacle.png")
obstacle_x_2 = 580
obstacle_y_2 = random.randint(0, 536)
obstacle_x_change_2 = 0.5

obstacle_img_3 = pygame.image.load("obstacle.png")
obstacle_x_3 = 860
obstacle_y_3 = random.randint(0, 536)
obstacle_x_change_3 = 0.5


#
# obstacle_img = []
# obstacle_x = []
# obstacle_y = []
# obstacle_x_change = []
# no_of_obstacles = 3
# ob_x = 0
#
# for i in range(no_of_obstacles):
#     obstacle_img.append(pygame.image.load("obstacle.png"))
#     ob_x += 30
#     obstacle_x.append(ob_x)
#     obstacle_y.append(random.randint(0, 536))
#     obstacle_x_change.append(0.1)


def nyonde(x, y):
    screen.blit(bird_img, (x, y))


def obstacle(x, y, bird_x_val, score_value):
    screen.blit(obstacle_img, (x, y))
    screen.blit(obstacle_img, (x, y + 250))
    screen.blit(obstacle_img, (x, y - 250))
    if bird_x_val == x:
        score_value = score_value + 1
    if score_value != 0:
        print(score_value)


def obstacle2(x, y):
    screen.blit(obstacle_img, (x, y))
    screen.blit(obstacle_img, (x, y + 250))
    screen.blit(obstacle_img, (x, y - 250))


def obstacle3(x, y):
    screen.blit(obstacle_img, (x, y))
    screen.blit(obstacle_img, (x, y + 250))
    screen.blit(obstacle_img, (x, y - 250))


def show_score(x, y):
    score = font.render(f"Score : {score_value}", True, (0, 0, 0))
    screen.blit(score, (x, y))


def has_crashed(bird_x_pos, bird_y_pos, obstacle_y_pos, obstacle_x_pos):
    obstacle_start = obstacle_y_pos
    obstacle_end = obstacle_y_pos + 64
    if obstacle_x_pos == bird_x_pos:
        if bird_y_pos >= obstacle_start or bird_y <= obstacle_end:
            print("Has crashed")
            return True
        else:
            print("Has not crashed")
            return False


score_value = 0
font = pygame.font.Font("blackParadeFont.otf", 50)
text_x = 10
text_y = 10

running = True
while running:
    screen.fill((0, 255, 255))

    bird_y += 0.5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = 3
                flap_sound = mixer.Sound("flap.mp3")
                flap_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 0

    if bird_y < 0:
        bird_y = 0
    elif bird_y > 536:
        bird_y = 536

    obstacle_x -= obstacle_x_change
    obstacle_x_2 -= obstacle_x_change_2
    obstacle_x_3 -= obstacle_x_change_3

    obstacle(obstacle_x, obstacle_y, bird_x, score_value)
    obstacle2(obstacle_x_2, obstacle_y_2)
    obstacle3(obstacle_x_3, obstacle_y_3)
    # obstacle(obstacle_x + diff_two_obstacles, obstacle_y)

    if obstacle_x <= 0:
        obstacle_x = 750
    if obstacle_x_2 <= 0:
        obstacle_x_2 = 750
    if obstacle_x_3 <= 0:
        obstacle_x_3 = 750

    has_crashed(bird_x, bird_y, obstacle_y, obstacle_x)
    bird_y -= bird_y_change
    show_score(text_x, text_y)
    nyonde(bird_x, bird_y)
    pygame.display.update()
