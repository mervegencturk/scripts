def calculate_ellipse_axes(domain_size, percentage, ratio_ab):
    semi_major_axis = (domain_size[0] / 2) * (percentage / 100)
    semi_minor_axis = semi_major_axis / ratio_ab
    
    return semi_major_axis, semi_minor_axis

def main():
    domain_size = tuple(map(int, input("Enter domain size (e.g., 100 100): ").split()))
    ratio_ab = float(input("Enter ratio of a/b: "))
    
    percentages = [1, 5, 10, 20, 30, 40, 50]

    for percentage in percentages:
        semi_major_axis, semi_minor_axis = calculate_ellipse_axes(domain_size, percentage, ratio_ab)
        
        print(f"For {percentage}% ellipse with a/b ratio of {ratio_ab}:")
        print(f"Semi-Major Axis (a): {semi_major_axis}")
        print(f"Semi-Minor Axis (b): {semi_minor_axis}")
        print()

if __name__ == "__main__":
    main()

