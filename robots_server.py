import mesa
from robots_visualization import *

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": 0.5}
    if agent.wealth == 2:
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0
    if agent.wealth == 3:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0

    return portrayal

grid = mesa.visualization.CanvasGrid(
    agent_portrayal,
    10, 10, 500, 500
)
server = mesa.visualization.ModularServer(
    MoneyModel,
    [grid],
    "Money Model",
    {"N": 2, "NB": 5, "NP": 2, "width": 10, "height": 10}
)

server.port = 8521
server.launch()