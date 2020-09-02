import unittest

from src.rover import Rover


class RoverTest(unittest.TestCase):
    def test_turn_right_N_to_E(self):
        rover = Rover(0, 0, "N")
        rover.go("R")
        self.assertEqual(rover.facing, "E")

    def test_turn_right_E_to_S(self):
        rover = Rover(0, 0, "E")
        rover.go("R")
        self.assertEqual(rover.facing, "S")

    def test_turn_right_S_to_W(self):
        rover = Rover(0, 0, "S")
        rover.go("R")
        self.assertEqual(rover.facing, "W")

    def test_turn_right_W_to_N(self):
        rover = Rover(0, 0, "W")
        rover.go("R")
        self.assertEqual(rover.facing, "N")

    def test_turn_left_N_to_W(self):
        rover = Rover(0, 0, "N")
        rover.go("L")
        self.assertEqual(rover.facing, "W")

    def test_turn_left_W_to_S(self):
        rover = Rover(0, 0, "W")
        rover.go("L")
        self.assertEqual(rover.facing, "S")

    def test_turn_left_S_to_E(self):
        rover = Rover(0, 0, "S")
        rover.go("L")
        self.assertEqual(rover.facing, "E")

    def test_turn_left_E_to_N(self):
        rover = Rover(0, 0, "E")
        rover.go("L")
        self.assertEqual(rover.facing, "N")

    def test_go_forward_facing_N(self):
        rover = Rover(5, 4, "N")
        rover.go("F")
        self.assertEqual(rover.position, (5, 5))

    def test_go_forward_facing_E(self):
        rover = Rover(5, 4, "E")
        rover.go("F")
        self.assertEqual(rover.position, (6, 4))

    def test_go_forward_facing_S(self):
        rover = Rover(5, 4, "S")
        rover.go("F")
        self.assertEqual(rover.position, (5, 3))

    def test_go_forward_facing_W(self):
        rover = Rover(5, 4, "W")
        rover.go("F")
        self.assertEqual(rover.position, (4, 4))

    def test_go_back_facing_N(self):
        rover = Rover(5, 4, "N")
        rover.go("B")
        self.assertEqual(rover.position, (5, 3))

    def test_go_back_facing_E(self):
        rover = Rover(5, 4, "E")
        rover.go("B")
        self.assertEqual(rover.position, (4, 4))

    def test_go_back_facing_S(self):
        rover = Rover(5, 4, "S")
        rover.go("B")
        self.assertEqual(rover.position, (5, 5))

    def test_go_back_facing_W(self):
        rover = Rover(5, 4, "W")
        rover.go("B")
        self.assertEqual(rover.position, (6, 4))

    def test_executes_sequence_of_instructions(self):
        rover = Rover(5, 5, "N")
        rover.go("RFF")
        self.assertEqual(rover.facing, "E")
        self.assertEqual(rover.position, (7, 5))


if __name__ == '__main__':
    unittest.main()
