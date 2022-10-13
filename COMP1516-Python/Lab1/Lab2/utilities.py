# Aline Hammermuller
# A01276569

import math


def calculate_circle_area(radius):
    """
    Function to calculate the area of a circle.
    :param radius:
    :return: circle_area
    """
    circle_area = math.pi * (radius ** 2)
    return circle_area


def calculate_sphere_volume(radius):
    """
    Function to calculate the sphere volume.
    :param radius:
    :return: sphere_volume
    """
    sphere_volume = 4 / 3 * math.pi * (radius ** 3)
    return sphere_volume


def calculate_BMI():
    """Function to calculate the body mass index
    after prompt the user to enter the weight in kilograms and the height in meters"""
    weight_kilograms = float(input("Enter the weight in kilograms: "))
    height_meters = float(input("Enter the height in meters: "))
    body_mass_index = weight_kilograms / (height_meters * height_meters)
    return body_mass_index


def calculate_hypotenuse():
    """ Function to calculate the length of a right triangle hypotenuse
    after prompt the user to enter the length of side A and side B """
    side_a = float(input("Enter the length of side A in cm: "))
    side_b = float(input("Enter the length of side B in cm: "))
    hypotenuse = math.hypot(side_a, side_b)
    return hypotenuse
