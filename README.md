## Aerial Navigation with Reinforcement Learning

This project uses Deep Reinforcement Learning to train UAVs to reach their targets without colliding with obstacles. 
### File structure

The project consists of the following files:

* main_anav.py: This is the main driver file that trains the agent using the PPO2 algorithm from stable-baselines and then plays the game.
* helper.py: This file contains the definition of the anav class, which represents the environment.

## Dependencies

Make sure you have the following dependencies installed:

* Python 3.x
* NumPy
* Gym
* stable-baselines

To install stable-baselines, run the following command:

```
pip install stable-baselines[mpi]==2.10.0
```

### Running the code

To run the code, navigate to the directory where the files are located and run the following command:

```
python main_anav.py
```

This will train the agent on the football environment and then have it play the game. You can adjust the hyperparameters of the PPO2 algorithm, such as the learning rate and the number of epochs, by modifying the corresponding arguments in the PPO2 constructor in the main file.


### Additional notes

Make sure that all of the required files are in the same directory, and that the file paths specified in the main file are correct. You may also need to adjust the rendering settings in the main file to display the game properly.


| Image                                                                | Caption                                                                |
|----------------------------------------------------------------------|------------------------------------------------------------------------|
|![The red dots represent the static obstacles](https://github.com/Aravind-11/Aerial-Navigation/blob/main/Screenshot%202021-11-20%20at%209.06.40%20PM.png)|The red dots represent the static obstacles in the environment for the aerial navigation task. The dotted blue line represents the UAV in motion. The dotted redline represents the dynamic obstacle in motion|
| ![The red dots represent the static obstacles](https://github.com/Aravind-11/Aerial-Navigation/blob/main/Screenshot%202022-12-28%20at%204.33.08%20PM.png) |This is the case for four agents in the environment. |









## References
  
https://github.com/AtsushiSakai/PythonRobotics
