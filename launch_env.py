import gym
import turtlebot3_env

if __name__ == '__main__':
    # make environment
    env = gym.make('turtlebot3_env/Turtlebot3-v0')
    try:
        conti = True
        while conti:
            # reset environment
            env.reset()

            # a random policy
            done = False
            its = 0
            while not done:
                action = [0, 1]
                next_state, reward, done, _ = env.step(action)
                print(f"it ({its});\nstate : {next_state}\naction : {action}\nreward : {reward}")

                its += 1
                if (its == 200):
                    break
            env.stop()
            print(f"final : {env.state}")

            # continue or not?
            key = int(input("ENTER 1 TO CONTINUE : "))
            if key != 1:
                conti = False

        # close environment
        input("ENTER TO CLOSE")
    finally:
        env.close()
