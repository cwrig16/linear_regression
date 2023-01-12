# Create class to determine slope and offset of a line to best fit as set of points in a dataset.  The distance from the line of each point is also calculated as 'Error'.
class Error():
    def __init__(self, name):
        self.name = name 
        self.possible_ms = [m * 0.1 for m in range(-100, 101)]
        self.possible_bs = [b * 0.1 for b in range(-200, 201)]
    
    # Method to get y value for given line
    def get_y(self, m, x, b):
        y = (m * x) + b
        return y

    # Method to error for a given point
    def calculate_error(self, m, b, point):
        x_point = point[0]
        y_point = point[1]
        get_y = self.get_y(m, x_point, b)
        return abs(get_y - y_point)
    
    # Method to calculate error for a set of points
    def calculate_all_error(self, m, b, points):
        error_total = 0
        for point in points:
            point_error = self.calculate_error(m, b, point)
            error_total += point_error
        return error_total

    # Method to optimize the line with the smallest total error for a given set of points. Returns the best 'm' and 'b' values for the smallest error
    def smallest_error(self, m, b, datapoints):
        self.smallest_error = (float('inf'))
        self.best_m = 0
        self.best_b = 0
        for m in self.possible_ms:
            for b in self.possible_bs:
                if self.calculate_all_error(m, b, datapoints) < self.smallest_error:
                    self.smallest_error = self.calculate_all_error(m, b, datapoints)
                    self.best_m = m
                    self.best_b = b
        print(self.smallest_error, self.best_m, self.best_b)
            

reggie = Error('Reggie')

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

reggie.smallest_error(reggie.possible_ms, reggie.possible_bs, datapoints)
print(reggie.get_y(reggie.best_m, 6, reggie.best_b))