# Aline Hammermuller
# A01276569


import utilities


def main():
    """
    Function to prompt the user the radius of a circle in cm and display the circle area;
    prompt the user the radius of a sphere in cm and display the sphere volume;
    display to the user the body mass index;
    display to the user the hypotenuse of a right triangle.
    """
    circle_radius = float(input("Enter the radius of a circle in cm: "))
    circle_area = utilities.calculate_circle_area(circle_radius)
    print("The area of circle is ", circle_area)
    sphere_radius = float(input("Enter the radius of a sphere in cm: "))
    sphere_volume = utilities.calculate_sphere_volume(sphere_radius)
    print("The volume of the sphere is: ", sphere_volume)
    body_mass_index = utilities.calculate_BMI()
    print("The body mass index is: ", body_mass_index)
    hypotenuse = utilities.calculate_hypotenuse()
    print("The hypotenuse length of the right triangle is: ", hypotenuse)


if __name__ == '__main__':
    main()
