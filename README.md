# Compare Episodic and Step-based Reinforcement Learning

Author: Gong, Yuhe

#Overview

This repository builds a framework to easily compare episodic and step-based reinforcement learning with several environments (DeepMind Control Suite , ALR environments, OpenAI environment).

- For step-based reinforcement learning, we use PPO, SAC from stable-baselines3 framework.

- For episodic reinforcement learning, we use DMP, ProMP from ALR's framework

We use different reward function to compare the performance in each environment:

- Sparse reward function: in one episode, only one step has the reward according to the task, other steps' rewards is 0.
- Dense reward function: in one episode, every step has the reward according to the task.

# Training with dense reward

|Name (env_id)| PPO|SAC|DMP|ProMP
|---|---|---|---|---|
|`ALR HoleReacher`|HoleReacherDense-v0|  |  | 
|`ALR Ball In A Cup`|ALRBallInACupSimpleDense-v0|  |  | 
|`DeepMind Ball In Cup`|DeepMindBallInCupDense-v0|  | DeepMindBallInCupDenseDMP-v0 | DeepMindBallInCupDenseProMP-v0

# Training with sparse reward

|Name (env_id)| PPO|SAC|DMP|ProMP
|---|---|---|---|---|
|`ALR HoleReacher`||  |  | 
|`ALR Ball In A Cup`||  |  | 
|`DeepMind Ball In Cup`||  | DeepMindBallInCupDMP-v0 | DeepMindBallInCupProMP-v0










-------------------------------------------------------------
## For training environment

#### Step-based algo

python train.py --algo ppo --env_id ALRBallInACupSimpleDense-v0

python train.py --algo ppo --env_id DeepMindBallInCupDense-v0

python train.py --algo ppo --env_id HoleReacherDense-v0

#### Episodic algo

python train.py --algo cmaes --env_id DeepMindBallInCupDMP-v0 --stop_cri True

python train.py --algo cmaes --env_id DeepMindBallInCupDenseDMP-v0

python train.py --algo cmaes --env_id DeepMindBallInCupProMP-v0

python train.py --algo cmaes --env_id DeepMindBallInCupDenseProMP-v0


## For continue training

python train_continue.py --algo ppo --env_id ALRBallInACupSimpleDense-v0 --model_id 1

python train_continue.py --algo ppo --env_id DeepMindBallInCupDense-v0 --model_id 1

## For enjoy a well-trained model:

python enjoy.py --algo ppo --env_id ALRBallInACupSimpleDense-v0 --model_id 20 --step 300

python enjoy.py --algo ppo --env_id DeepMindBallInCupDense-v0 --model_id 2 --step 300

python enjoy.py --algo cmaes --env_id DeepMindBallInCupDenseProMP-v0 --model_id 4 --step 300

python enjoy.py --algo ppo --env_id HoleReacherDense-v0 --model_id 1 --step 400



