"""
Circle class for representing a circle in n-dimensional space.

This module provides a simple Circle class that represents a circle (or sphere in higher dimensions)
with a center point and radius.
"""

class Circle:
    """
    A class representing a circle in n-dimensional space.

    Attributes:
        radius (float): The radius of the circle.
        center (numpy.ndarray): The center coordinates of the circle.
    """

    def __init__(self, radius, center):
        """
        Initialize a Circle object.

        Args:
            radius (float): The radius of the circle.
            center (numpy.ndarray): The center coordinates of the circle.
        """
        self.radius = radius
        self.center = center

    def __repr__(self):
        """
        Return a string representation of the Circle.

        Returns:
            str: A string representation of the Circle.
        """
        return f"Circle(radius={self.radius}, center={self.center})"
