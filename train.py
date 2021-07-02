import argparse
from utils.env import env_maker, env_save
from utils.logger import logging
from utils.model import model_building, model_learn
from utils.yaml import write_yaml, read_yaml
from stable_baselines3 import PPO, A2C, DQN, HER, SAC, TD3, DDPG


def step_based(algo: str, env_id: str):
    file_name = algo +".yml"
    data = read_yaml(file_name)[env_id]

    # create log folder
    path = logging(data['env_params']['env_name'], data['algorithm'])
    data['path'] = path

    # make the environment
    env = env_maker(data, num_envs=data["env_params"]['num_envs'])
    test_env = env_maker(data, num_envs=1, training=False, norm_reward=False)

    # make the model and save the model
    model = model_building(data, env)

    try:
        test_env_path = data['path'] + "/eval/"
        model_learn(data, model, test_env, test_env_path)

    except KeyboardInterrupt:
        data["algo_params"]['num_timesteps'] = model.num_timesteps
        write_yaml(data)
        env_save(data, model, env)
        print('')
        print('training interrupt, save the model and config file to ' + data["path"])
    else:
        data["algo_params"]['num_timesteps'] = model.num_timesteps
        write_yaml(data)
        env_save(data, model, env)
        print('')
        print('training FINISH, save the model and config file to ' + data['path'])

def episodic():
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", type=str, help="the algorithm")
    parser.add_argument("--env_id", type=str, help="the environment")
    args = parser.parse_args()

    if not args.algo and not args.env_id:
        parser.error('Please specify an algorithm (--algo) and an environment (--env_id) to train or enjoy')

    algo = args.algo
    env_id = args.env_id

    STEP_BASED = ["ppo", "sac"]
    EPISODIC = ["cmaes"]
    if algo in STEP_BASED:
        step_based(algo, env_id)
    elif algo in EPISODIC:
        episodic()
    else:
        print("the algorithm (--algo) is false or not implemented")

