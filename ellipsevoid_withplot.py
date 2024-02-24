import matplotlib.pyplot as plt
import numpy as np

def calculate_ellipse_axes(domain_size, percentage, ratio_ab):
    center_x = domain_size[0] / 2
    center_y = domain_size[1] / 2
    
    semi_major_axis = (domain_size[0] / 2) * (percentage / 100)
    semi_minor_axis = semi_major_axis / ratio_ab
    
    return center_x, center_y, semi_major_axis, semi_minor_axis

def plot_ellipse(ax, center_x, center_y, semi_major_axis, semi_minor_axis):
    ellipse = plt.Circle((center_x, center_y), semi_major_axis, fill=False, edgecolor='blue', linestyle='--', label='Ellipse')
    
    # Display a and b values on the left corner
    plt.text(center_x - semi_major_axis, center_y + semi_minor_axis, f'a={semi_major_axis:.2f}', ha='right', va='bottom')
    plt.text(center_x - semi_major_axis, center_y - semi_minor_axis, f'b={semi_minor_axis:.2f}', ha='right', va='top')

    # Draw centerline for a
    plt.plot([center_x - semi_major_axis, center_x + semi_major_axis], [center_y, center_y], linestyle='--', color='green', label='a-axis')

    # Draw centerline for b
    plt.plot([center_x, center_x], [center_y - semi_minor_axis, center_y + semi_minor_axis], linestyle='--', color='orange', label='b-axis')

    ax.add_patch(ellipse)

def main():
    domain_size = tuple(map(int, input("Enter domain size (e.g., 100 100): ").split()))
    ratio_ab = float(input("Enter ratio of a/b: "))
    
    percentages = [1, 5, 10, 20, 30, 40, 50]

    for percentage in percentages:
        center_x, center_y, semi_major_axis, semi_minor_axis = calculate_ellipse_axes(domain_size, percentage, ratio_ab)

        print(f"For {percentage}% ellipse with a/b ratio of {ratio_ab}:")
        print(f"Semi-Major Axis (a): {semi_major_axis}")
        print(f"Semi-Minor Axis (b): {semi_minor_axis}")
        print()

        fig, ax = plt.subplots()
        plt.xlim(0, domain_size[0])
        plt.ylim(0, domain_size[1])

        plot_ellipse(ax, center_x, center_y, semi_major_axis, semi_minor_axis)

        plt.title(f"Ellipse with {percentage}% axes in the center")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    main()








