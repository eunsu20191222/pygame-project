import pygame
import random

pygame.init()

screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Ayden Game")

clock = pygame.time.Clock()

background = pygame.image.load("image/background.png")
gameover = pygame.image.load("image/gameover.png")
finish = pygame.image.load("image/finish.png")

character = pygame.image.load("image/character.png")
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
character_speed = 25
character_move = 0
character_move_y = 0

weapon = pygame.image.load("image/weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_x_pos = 0
weapon_y_pos = random.randint(0, screen_height - weapon_height)
weapon_speed = 10

weapon2 = pygame.image.load("image/weapon2.png")
weapon2_size = weapon2.get_rect().size
weapon2_width = weapon2_size[0]
weapon2_height = weapon2_size[1]
weapon2_x_pos = 0
weapon2_y_pos = random.randint(0, (screen_height / 2) - weapon2_height)
weapon2_speed = 10

weapon4 = pygame.image.load("image/weapon4.png")
weapon4_size = weapon4.get_rect().size
weapon4_width = weapon4_size[0]
weapon4_height = weapon4_size[1]
weapon4_x_pos = 0
weapon4_y_pos = random.randint(0, ((screen_height / 2) / 2) - weapon4_height)
weapon4_speed = 10

weapon5 = pygame.image.load("image/weapon4.png")
weapon5_size = weapon5.get_rect().size
weapon5_width = weapon5_size[0]
weapon5_height = weapon5_size[1]
weapon5_x_pos = 0
weapon5_y_pos = random.randint(0, ((screen_height / 2) / 2) - weapon5_height)
weapon5_speed = 10

top_weapon = pygame.image.load("image/top_weapon.png")
top_weapon_size = top_weapon.get_rect().size
top_weapon_width = top_weapon_size[0]
top_weapon_height = top_weapon_size[1]
top_weapon_x_pos = random.randint(0, screen_width - top_weapon_width)
top_weapon_y_pos = 0
top_weapon_speed = 6

top_weapon2 = pygame.image.load("image/top_weapon.png")
top_weapon_size2 = top_weapon.get_rect().size
top_weapon_width2 = top_weapon_size[0]
top_weapon_height2 = top_weapon_size[1]
top_weapon_x_pos2 = random.randint(0, screen_width - top_weapon_width)
top_weapon_y_pos2 = 0
top_weapon_speed2 = 6


font = pygame.font.Font(None, 40)
total_time = 20
start_ticks = pygame.time.get_ticks()

running = True
while running:

    time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = font.render(str(int(total_time - time)), True, (0, 0, 0))
    get_time = total_time - time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_x_pos -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_x_pos += character_speed
            elif event.key == pygame.K_UP:
                character_y_pos -= character_speed
            elif event.key == pygame.K_DOWN:
                character_y_pos += character_speed
            



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                character_move = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or pygame.K_DOWN:
                character_move_y = 0

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        if character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height

    weapon_x_pos += weapon_speed
    weapon2_x_pos += weapon2_speed
    weapon4_x_pos += weapon4_speed
    weapon5_x_pos += weapon5_speed
    top_weapon_y_pos += top_weapon_speed
    top_weapon_y_pos2 += top_weapon_speed2

    if weapon_x_pos > screen_width:
        weapon_x_pos = 0
        weapon_y_pos = random.randint(0, screen_height - weapon_height)

    if weapon2_x_pos > screen_width:
        weapon2_x_pos = 0
        weapon2_y_pos = random.randint(0, screen_height - weapon2_height)


    if weapon4_x_pos > screen_width:
        weapon4_x_pos = 0
        weapon4_y_pos = random.randint(0, screen_height - weapon4_height)

    if weapon5_x_pos > screen_width:
        weapon5_x_pos = 0
        weapon5_y_pos = random.randint(0, screen_height - weapon5_height)

    if top_weapon_y_pos > screen_height:
        top_weapon_x_pos = random.randint(0, screen_width - top_weapon_width)
        top_weapon_y_pos = 0

    if top_weapon_y_pos2 > screen_height:
        top_weapon_x_pos2 = random.randint(0, screen_width - top_weapon_width)
        top_weapon_y_pos2 = 0

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    weapon_rect = weapon.get_rect()
    weapon_rect.left = weapon_x_pos 
    weapon_rect.top = weapon_y_pos

    weapon2_rect = weapon2.get_rect()
    weapon2_rect.left = weapon2_x_pos 
    weapon2_rect.top = weapon2_y_pos


    weapon4_rect = weapon4.get_rect()
    weapon4_rect.left = weapon4_x_pos
    weapon4_rect.top = weapon4_y_pos

    weapon5_rect = weapon5.get_rect()
    weapon5_rect.left = weapon5_x_pos
    weapon5_rect.top = weapon5_y_pos

    top_weapon_rect = top_weapon.get_rect()
    top_weapon_rect.left = top_weapon_x_pos
    top_weapon_rect.top = top_weapon_y_pos

    if character_rect.colliderect(weapon_rect):
        print("1번에 충돌했어요^^")
        running = False
        print(get_time)
        screen.blit(gameover, (0, 0))

    if character_rect.colliderect(weapon2_rect):
        print("2번에 충돌했어요^^")
        running = False
        print(get_time)
        screen.blit(gameover, (0, 0))

    if character_rect.colliderect(weapon4_rect):
        print("4번에 충돌했어요^^")
        running = False
        print(get_time)
        screen.blit(gameover, (0, 0))

    if character_rect.colliderect(weapon5_rect):
        print("5번에 충돌했어요^^")
        screen.blit(gameover, (0, 0))
        running = False
        print(get_time)

    if character_rect.colliderect(top_weapon_rect):
        print("재수없게 위에서 떨어지는거에 충돌 했네?^^")
        screen.blit(gameover, (0, 0))
        running = False 
        print(get_time)

  #계속 업데이트ㅡㅡㅡㅡㅡㅡ
    pygame.display.update()
    dt = clock.tick(30)

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(weapon2, (weapon2_x_pos, weapon2_y_pos))
    screen.blit(weapon4, (weapon4_x_pos, weapon4_y_pos))
    screen.blit(weapon5, (weapon5_x_pos, weapon5_y_pos))
    screen.blit(timer, (10, 10))
    screen.blit(top_weapon, (top_weapon_x_pos, top_weapon_y_pos))

    

    if total_time - time <= 0:
        print("오 잘했네??^^")
        screen.blit(finish, (0, 0))
        running = False 
                

pygame.time.delay(2000)
pygame.quit()
