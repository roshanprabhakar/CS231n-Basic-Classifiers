import random

from ComputationalGraphs import Commands
from ComputationalGraphs.Commands import Multiplication


class ComputationalGraph:
    connections = 2

    def __init__(self, layers):
        self.final = Node()
        self.graph(self.final, layers)

    def simple_graph(self, node):
        for i in range(self.connections):
            node.add_value_channel(random.randint(0, 5))

    def graph(self, node, layers):
        if layers == 2:
            self.simple_graph(node)
        else:
            for i in range(self.connections):
                new_node = Node()
                self.graph(new_node, layers - 1)
                node.add_input_channel(new_node)


class Node:

    def __init__(self, computation="add"):
        self.input = []
        self.computation = computation
        self.computer = Utils.commands[computation]

    # one of two content modifiers
    def add_input_channel(self, node):
        self.input.append(node)

    # one of two content modifiers
    def add_value_channel(self, value):
        self.input.append(value)

    def compute_output(self):

        if type(self.input[0]) is not int:
            feed_forward = []
            for node in self.input:
                feed_forward.append(node.compute_output())

            return self.computer.compute(feed_forward)
        else:
            print(self.input)
            return self.computer.compute(self.input)

    def __str__(self):
        return self.computation


class Utils:
    commands = {"multiply": Commands.Multiplication, "add": Commands.Addition}


graph = ComputationalGraph(4)
print(graph.final.compute_output())
