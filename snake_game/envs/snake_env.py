from snake_game.game.snake_game import SnakeGame
import numpy as np
import gym

N_CHANNELS = 1
HEIGHT = 40
WIDTH = 40


class SnakeEnv(gym.Env):
    def __init__(self):
        self.game = SnakeGame()
        self.action_space = gym.spaces.Discrete(4)
        # self.observation_space = gym.spaces.Discrete(2)
        self.observation_space = gym.spaces.Box(
            low=0, high=4, shape=(HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8
        )

    def step(self, action):
        return self.game.step(action)

    def reset(self):
        return self.game.reset()

    def render(self):
        self.game.render()

    def quit(self):
        self.game.quit()
