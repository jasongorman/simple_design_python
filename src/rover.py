import logging


class Rover(object):
    def __init__(self, x, y, facing):
        self.facing = facing
        self.position = (x, y)

    def go(self, instructions):
        logging.basicConfig(filename='rover.log', level=logging.INFO)
        logging.info('Instructions received: ' + instructions)

        for instruction in list(instructions):
            self.execute(instruction)

    def execute(self, instruction):
        if instruction == "R":
            if self.facing == "N":
                self.facing = "E"
                return

            if self.facing == "E":
                self.facing = "S"
                return

            if self.facing == "S":
                self.facing = "W"
                return

            self.facing = "N"
            return

        if instruction == "L":
            if self.facing == "N":
                self.facing = "W"
                return

            if self.facing == "W":
                self.facing = "S"
                return

            if self.facing == "S":
                self.facing = "E"
                return

            self.facing = "N"
            return

        if instruction == "F":
            if self.facing == "N":
                self.position = (self.position[0], self.position[1] + 1)

            if self.facing == "E":
                self.position = (self.position[0] + 1, self.position[1])

            if self.facing == "S":
                self.position = (self.position[0], self.position[1] - 1)

            if self.facing == "W":
                self.position = (self.position[0] - 1, self.position[1])

        if instruction == "B":
            if self.facing == "N":
                self.position = (self.position[0], self.position[1] - 1)

            if self.facing == "E":
                self.position = (self.position[0] - 1, self.position[1])

            if self.facing == "S":
                self.position = (self.position[0], self.position[1] + 1)

            if self.facing == "W":
                self.position = (self.position[0] + 1, self.position[1])