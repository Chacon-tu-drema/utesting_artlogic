class MarsRover:
    def execute(self, command: str) -> str:
        x = 0
        y = 0
        c_points = ["N", "E", "S", "W"]
        index = 0

        for instruction in command:
            if instruction == "R":
                # if index < 3:
                index += 1
                if index > 3:
                    index = 0
            if instruction == "L":
                index -= 1
                if index < 0:
                    index = 3
            if instruction == "M":
                if c_points[index] == "N":
                    y += 1
                if c_points[index] == "S":
                    y -= 1
                if c_points[index] == "W":
                    x -= 1
                if c_points[index] == "E":
                    x += 1
            if x > 9:
                x = 0
            if y > 9:
                y = 0

        cardinal = c_points[index]

        return "{}:{}:{}".format(x, y, cardinal)
