import numpy as np
import matplotlib.pyplot as plt

!pip install stable-baselines[mpi]==2.10.0

import gym
from stable_baselines import PPO2
from random import random
from football import Football

class mod_anav(anav,gym.Env):
  def __init__(self):
    super(mod_anav,self).__init__()
    self.action_space=gym.spaces.Discrete(5)
    self.observation_space=gym.spaces.Box(low=0,high=30,shape=(6,))

env = mod_anav()

model = PPO2('MlpPolicy', env)
model.learn(total_timesteps=20000)

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()


