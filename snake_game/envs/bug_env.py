from snake_game.game.bug_game import BugGame
import numpy as np
import gym

N_CHANNELS = 1
HEIGHT = 5
WIDTH = 5


class BugEnv(gym.Env):
    def __init__(self):
        self.game = BugGame()
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
