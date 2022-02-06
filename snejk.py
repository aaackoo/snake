## Snake Game
## Adam Šupej, I. ročník, Bc. studium, Informatika IPP
## Zimný semester, 2021/22
## Programování 1 NPRG030

import sys
import random as rnd
import pygame as pg
from pygame.math import Vector2 as vec ## Vectors for easier use (personal preference)

## Class for SNAKE
class SNAKE():
    def __init__(self) -> None:
        self.generate_snake()
        self.body_img = pg.image.load('Images/skver.png').convert_alpha()
        self.sound = pg.mixer.Sound('Sounds/drink.wav')
        self.ded = pg.mixer.Sound('Sounds/hit.mp3')

    def generate_snake(self):
        self.body = [vec(10, 10), vec(9, 10), vec(8, 10)]
        self.direction = vec(1, 0)
        self.turn_status = 1
          ## 0 - Snake just turned recently
          ## 1 - Snake is ready to turn again

    def draw_snake(self):
        for body_part in self.body:
            snake = pg.Rect(int(body_part.x * tile_size), int(body_part.y * tile_size), tile_size, tile_size)
            win.blit(self.body_img, snake)

    def move(self):
        body_copy = self.body[:-1] ## REMOVING LAST SEGMENT
        body_copy.insert(0, body_copy[0] + self.direction) ## ADDING NEW SEGMENT AT THE BEGINNING
        self.body = body_copy.copy()

    def extend(self):
        self.body.append(self.body[-1])
        self.sound.play()

## Class for FOOD
class FOOD():
    def __init__(self) -> None:
        self.generate_food_pos()
        self.photo = pg.transform.scale(pg.image.load('Images/food.png'), (40,40)).convert_alpha()

    def generate_food_pos(self): ## Generates RANDOM position for FOOD
        self.pos = vec(rnd.randrange(0, tile_count), rnd.randrange(0, tile_count))

    def draw_food(self): ## Draws image on screen
        food = pg.Rect(int(self.pos.x * tile_size), int(self.pos.y * tile_size), tile_size, tile_size)
        win.blit(self.photo, food) 
    
## Class for GAME
class GAME():
    def __init__(self) -> None:
        self.snake = SNAKE()
        self.food = FOOD()
        self.state = 0
          ## 0 - Title screen
          ## 1 - Main game
          ## 2 - Ending_screen
        ## MAP SETTINGS
        self.map = 1
        self.finger_pos = 60
        self.obstacles = []
        self.obs_img = pg.transform.scale(pg.image.load('Images/obstacle.png'), (40,40)).convert_alpha()
        ## FONT
        self.font = pg.font.Font('Fonts/Sticky_Notes.TTF', 40)
        self.font_title = pg.font.Font('Fonts/Sticky_Notes.TTF', 100)
        ## INPUT_BOX
        self.color = pg.Color('black')
        self.input_box = pg.Rect(300, 500, 200, 35)
        self.written = False
        self.writting = False
        self.name = ""

    ## USER EVENT
    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == timer and self.state == 1:
                self.update()

            ## KEYBOARD INTERACTIONS
            if event.type == pg.KEYDOWN:
                ## RESETING GAME
                if event.key == pg.K_RETURN and self.state == 0:
                    self.snake.generate_snake()
                    self.read_obstacles()
                    self.state = 1
                    self.written = False
                if event.key == pg.K_n and self.state == 2 and not self.writting:
                    self.state = 0
                    self.written = False
                
                ## WRITING INTO INPUT_BOX
                if self.writting:
                    if event.key == pg.K_RETURN:
                        with open('hall_of_fame.txt', 'a', encoding = 'utf-8-sig') as f:
                            f.write(f'{self.name} {len(self.snake.body) - 3}\n')
                        self.generate_table()
                        self.written = True
                        self.name = ''
                    
                    elif event.key == pg.K_BACKSPACE:
                        self.name = self.name[:-1]
                    else:
                        self.name += event.unicode

                ## DIRECTIONS
                if self.snake.turn_status == 1:
                    if event.key == pg.K_LEFT:
                        if self.snake.direction.x != 1: self.snake.direction = vec(-1, 0)
                        self.snake.turn_status = 0
                    if event.key == pg.K_UP:
                        if self.snake.direction.y != 1: self.snake.direction = vec(0, -1)
                        self.snake.turn_status = 0
                    if event.key == pg.K_RIGHT:
                        if self.snake.direction.x != -1: self.snake.direction = vec(1, 0)
                        self.snake.turn_status = 0
                    if event.key == pg.K_DOWN:
                        if self.snake.direction.y != -1: self.snake.direction = vec(0, 1)
                        self.snake.turn_status = 0

            ## MOUSEBUTTON INTERACTIONS
            if event.type == pg.MOUSEBUTTONDOWN:
                ## MAP CHOOSING
                if self.state == 0:
                    click = list(event.pos)
                    if click[0] in range(50, 150) and click[1] in range(420,520):
                        self.map = 1
                        self.finger_pos = 60
                        pg.mixer.Sound('Sounds/hm.mp3').play()
                    if click[0] in range(250, 350) and click[1] in range(420,520):
                        self.map = 2
                        self.finger_pos = 260
                        pg.mixer.Sound('Sounds/hm.mp3').play()
                    if click[0] in range(450, 550) and click[1] in range(420,520):
                        self.map = 3
                        self.finger_pos = 460
                        pg.mixer.Sound('Sounds/hm.mp3').play()
                    if click[0] in range(650, 750) and click[1] in range(420,520):
                        self.map = 4
                        self.finger_pos = 660
                        pg.mixer.Sound('Sounds/hm.mp3').play()
                
                ## CLICKING ONTO INPUT_BOX
                if self.state == 2:
                    if self.input_box.collidepoint(event.pos) and not self.written:
                        self.writting = not self.writting
                    else:
                        self.writting = False

    ## TITLE SCREEN ##
    def title_screen(self):
        self.state = 0
        self.draw_score()

        text = self.font.render('Collect BEERS to get higher score.', True, self.color)
        text2 = self.font.render('Avoid walls, obstacles and crashing into yourself!', True, self.color)
        text3 = self.font.render('Press [ ENTER ] to play', True, self.color)
        text4 = self.font.render('Choose your Map:', True, self.color)
        win.blit(text, text.get_rect(center = (350, 200)))
        win.blit(text2, text.get_rect(center = (350, 240)))
        win.blit(text3, text.get_rect(center = (350, 280)))
        win.blit(text4, text.get_rect(center = (350, 320)))

        map1 = pg.transform.scale((pg.image.load('Images/map1.png')), (100, 100)).convert_alpha()
        map2 = pg.transform.scale((pg.image.load('Images/map2.png')), (100, 100)).convert_alpha()
        map3 = pg.transform.scale((pg.image.load('Images/map3.png')), (100, 100)).convert_alpha()
        map4 = pg.transform.scale((pg.image.load('Images/map4.png')), (100, 100)).convert_alpha()
        win.blit(map1, (50,420))
        win.blit(map2, (250,420))
        win.blit(map3, (450,420))
        win.blit(map4, (650,420))

        Finger = pg.transform.scale((pg.image.load('Images/finger.png')), (75, 75)).convert_alpha()
        win.blit(Finger, (self.finger_pos, 350))

    ## RUN TIME ##
    def run(self):
        self.snake.draw_snake()
        self.food.draw_food()
        self.check_food_collision()
        if self.map != 1:
            self.draw_obstacles()
        self.draw_score()

    def update(self): ## Update game state, moving snake
        self.snake.turn_status = 1 ## SNAKE can turn again
        if len(self.snake.body) > 13:
            game.rand_turn()
        self.snake.move()
        self.eat()
        self.collision()

    def eat(self): ## Compare SNAKE head pos and FOOD pos
        if self.food.pos == self.snake.body[0]:
            self.food.generate_food_pos()
            self.snake.extend()

    # Checks if food is not in collision with snake or obstacles
    def check_food_collision(self):
        for body_part in self.snake.body[1:]: ## Prevent spawning on our SNAKE
            if body_part == self.food.pos:
                self.food.generate_food_pos()

        for obstacle in self.obstacles: ## Prevent spawning on our OBSTACLES
            if obstacle == self.food.pos:
                self.food.generate_food_pos()

    # Snake Collision
    def collision(self):
        if self.state == 1: ## Crashing into edges of the screen
            if not 0 <= self.snake.body[0].x < tile_count or not 0 <= self.snake.body[0].y < tile_count: ## Crashing into walls
                self.game_over()
                self.snake.ded.play()

            for i in self.snake.body[1:]: ## Crashing into ourselves
                if i == self.snake.body[0]:
                    self.game_over()
                    self.snake.ded.play()

            for i in self.obstacles: ## Crashing into obstacles
                if i == self.snake.body[0]:
                    self.game_over()
                    self.snake.ded.play()

    def rand_turn(self): ## SNAKE GETS "DRUNK" AND TENDS TO CHANGE DIRECTION ON HIS OWN
        num = rnd.randint(1, int(1000/(len(self.snake.body) - 3) * 5))
        dir = rnd.randint(0, 3)
        if 1 <= num <= 3:
            if game.snake.direction.x != 1 and dir == 0:
                self.snake.turn_status = 0
                self.snake.direction = vec(-1, 0)
            if game.snake.direction.y != 1 and dir == 1:
                self.snake.turn_status = 0
                self.snake.direction = vec(0, -1)                
            if game.snake.direction.x != -1 and dir == 2:
                self.snake.turn_status = 0
                self.snake.direction = vec(1, 0)
            if game.snake.direction.y != -1 and dir == 3:
                self.snake.turn_status = 0
                self.snake.direction = vec(0, 1)

    ## READING chosen map.txt and putting positions into self.obstacles
    def read_obstacles(self):
        self.obstacles = []
        with open(f'Maps/{self.map}.txt', 'r') as F:
            for i in F.readlines():
                self.obstacles.append(vec(int(i.split()[0]),int(i.split()[1])))

    ## DRAWING obstacles from self.obstacles onto screen
    def draw_obstacles(self):
        for vector in self.obstacles:
            obs_rect = pg.Rect((vector.x) * tile_size, (vector.y) * tile_size, tile_size, tile_size)
            win.blit(self.obs_img, obs_rect)

    ## Drawing score
    def draw_score(self):
        text = f"beers: {len(self.snake.body) - 3}"
        score = self.font.render(text, True, self.color)
        score_pos = int(tile_size * tile_count - 100) 
        win.blit(score, score.get_rect(center = (score_pos, 40)))

    ## Drawing HALL_OF_FAME.txt onto screen
    def generate_table(self):
        with open('hall_of_fame.txt', 'r', encoding = 'utf-8-sig') as leader:
            row = leader.readlines()
        self.top = []

        ## Sorting algorithm
        for index, i in enumerate(row): 
            row[index] = i.split() ## Getting everything into list
        lenght = len(row)
        while (len(self.top) != lenght):
            if len(self.top) == 5: ## We have enough
                break
            max_value = int(row[0][-1]) ## Setting the maximum value as the first value from original list
            for index, num in enumerate(row):
                if max_value <= int(num[-1]): ## Comparing every value with our current maximum value
                    max_value = int(num[-1])
                    max_index = index
                    full = num
            self.top.append(full) ## Appending biggest value into final list
            row.pop(max_index) ## Removing value from original list

    ## ENDING SCREEN ##
    def game_over(self):
        self.state = 2

        text = self.font_title.render('GAMEOVER', True, pg.Color('red'))
        text2 = self.font.render(f'You have finished with the final beer count of {len(self.snake.body) - 3}!', True, self.color)
        text3 = self.font.render("Write your name below to save your highscore", True, self.color)
        text4 = self.font.render('Press [n] to go back to main menu!', True, self.color)
        win.blit(text, text.get_rect(center = (400,200)))
        win.blit(text2, text2.get_rect(center = (400,380)))
        win.blit(text3, text3.get_rect(center = (400,420)))
        win.blit(text4, text4.get_rect(center = (400,460)))

        ## INPUT_BOX
        color = pg.Color('green') if self.writting else self.color
        entry = self.font.render(self.name, True, color)
        win.blit(entry, (self.input_box.x + 5, self.input_box.y))
        pg.draw.rect(win, color, self.input_box, 2)
        
        ## LEADERBOARD
        if self.written: 
            for i in range(len(self.top)):
                leaderboard = self.font.render(f'{i + 1}. {self.top[i][0]}: {self.top[i][-1]} beers', True, self.color)
                win.blit(leaderboard, leaderboard.get_rect(center = (400, 580 + i * 40)))
                if i == 4:
                    break
        
        ## Flip display
        pg.display.flip()

## Game proportions
tile_size, tile_count = 40, 20

## Setting up display
pg.init()
pg.display.set_caption("SNEJK")
win = pg.display.set_mode((tile_size * tile_count, tile_size * tile_count))
fps = pg.time.Clock()

## Game timer, how fast snake moves
timer = pg.USEREVENT
pg.time.set_timer(timer, 180)

## Infinite game loop
game = GAME()
while True:
    win.fill((0,100,0))
    game.check_event()
    if game.state == 0:
        game.title_screen()
    if game.state == 1:
        game.run()
    if game.state == 2:
        game.game_over()
    pg.display.update()
    fps.tick(60)