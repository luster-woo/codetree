class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score


agents = []

# 5명 입력
for _ in range(5):
    codename, score = input().split()
    agents.append(Agent(codename, int(score)))

# 최소 점수 찾기
min_agent = agents[0]
for agent in agents:
    if agent.score < min_agent.score:
        min_agent = agent

# 출력
print(min_agent.codename, min_agent.score)