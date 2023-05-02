from point2d import Point2D
import math


class Manager:
    def calculate_distance(self, point1, point2):
        if isinstance(point1, Point2D) and isinstance(point2, Point2D):
            dx = point1.get_x() - point2.get_x()
            dy = point1.get_y() - point2.get_y()
            # distance = (dx ** 2 + dy ** 2) ** 0.5
            distance = math.sqrt(dx ** 2 + dy ** 2)
            return distance

        return -1
