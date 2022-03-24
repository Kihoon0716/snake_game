from typing import Iterator
import pygame
import numpy as np
import copy
import random

Color = (255, 255, 255)  # 하얀색
size = [100 + 5 * 10 + 100, 100 + 5 * 10 + 100]


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class BugGame:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.pika_y = 0
        self.screen = None
        self.head = None

    def reset(self):
        self.screen = pygame.display.set_mode(size)
        self.map = np.zeros((5, 5, 1))

        h_row = random.randint(0, 4)
        h_col = random.randint(0, 4)
        self.map[h_row][h_col] = 2
        self.head = [h_row, h_col]

        self.reset_star()
        return self.map

    def reset_star(self):
        while True:
            star_x = random.randint(0, 4)
            star_y = random.randint(0, 4)
            if self.map[star_x][star_y] == 0:
                self.map[star_x][star_y] = 4
                return

    def step(self, action):
        """
        action
            0: down
            1: up
            2: left
            3: right
        """

        """
        map
            0: empty space
            1: body of snake
            2: head of snake
            3: tail of snake
            4: star
        """
        # print(f"action: {action}")
        reward = 0
        d_row = [1, -1, 0, 0]
        d_col = [0, 0, -1, 1]
        head = self.head

        head_next = copy.deepcopy(head)
        head_next[0] += d_row[action]
        head_next[1] += d_col[action]
        if (
            head_next[0] > 4
            or head_next[1] > 4
            or head_next[0] < 0
            or head_next[1] < 0
            or self.map[head_next[0]][head_next[1]] not in [0, 4]
        ):
            done = True
            return self.map, -1, done, {}

        if self.map[head_next[0]][head_next[1]][0] == 4:
            eat_star = True
            reward += 100

        else:
            eat_star = False

        self.map[head[0]][head[1]][0] = 0
        self.map[head_next[0]][head_next[1]][0] = 2
        self.head = head_next

        if eat_star:
            self.reset_star()

        info = {}
        done = False
        return self.map, reward, done, info

    def render(self):
        self.clock.tick(10)
        self.screen.fill(Color)
        for idx_row, row in enumerate(self.map):
            for idx_col, col in enumerate(row):
                if col[0] == 0:
                    pygame.draw.rect(
                        self.screen,
                        WHITE,
                        [100 + idx_col * 10, 100 + idx_row * 10, 10, 10],
                    )
                elif col[0] == 1:
                    pygame.draw.rect(
                        self.screen,
                        BLACK,
                        [100 + idx_col * 10, 100 + idx_row * 10, 10, 10],
                    )
                elif col[0] == 2:
                    pygame.draw.rect(
                        self.screen,
                        RED,
                        [100 + idx_col * 10, 100 + idx_row * 10, 10, 10],
                    )
                elif col[0] == 3:
                    pygame.draw.rect(
                        self.screen,
                        BLUE,
                        [100 + idx_col * 10, 100 + idx_row * 10, 10, 10],
                    )
                elif col[0] == 4:
                    pygame.draw.rect(
                        self.screen,
                        GREEN,
                        [100 + idx_col * 10, 100 + idx_row * 10, 10, 10],
                    )
        pygame.display.update()  # 게임 화면 업데이트

    def get_key(self):
        action = -1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 게임 화면 종료
                finish = True
            # !#!#!# 추가 코드시작 #!#!#!#
            # 방향키 입력에 대한 이벤트 처리
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    action = 0
                elif event.key == pygame.K_UP:
                    action = 1
                elif event.key == pygame.K_LEFT:
                    action = 2
                elif event.key == pygame.K_RIGHT:
                    action = 3
            # !#!#!# 추가 코드 끝 #!#!#!#

        return action

    def quit(self):
        print("quit game")
        pygame.quit()
        pygame.display.quit()


if __name__ == "__main__":
    game = BugGame()
    done = False
    game.reset()
    game.render()
    while not done:
        action = game.get_key()
        if action is not -1:
            state, reward, done, info = game.step(action=action)
            print(f"reward: {reward}")
            print(f"action: {action}")
            game.render()
    game.quit()
