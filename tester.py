!pip install --upgrade kaggle-environments


from kaggle_environments import make
env = make("chess", debug=True)


result = env.run(["sample.py", "random"])
print("Agent exit status/reward/time left: ")
for agent in result[-1]:
    print("\t", agent.status, "/", agent.reward, "/", agent.observation.remainingOverageTime)
print("\n")
# render the game
env.render(mode="ipython", width=700, height=700) 
