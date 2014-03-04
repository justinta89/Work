# cannonball.py
# 4th iteration
"""
Input the simulation parameters: angle, velocity, height, interval
Calculate the initial position of the cannonball: xpos, ypos
Calculate the initial velocities of the cannonball: xvel, yvel
While the cannonball is still flying:
    update the values of xpos, ypos, and yvel for interval seconds
        further into the flight
output the distance traveled as xpos
"""


from projectile import Projectile


def get_inputs():
    """Get all the inputs"""
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    t = float(input("Enter the time interval between position calculations: "))
    return a, v, h, t


def main():
    angle, vel, h0, time = get_inputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meteres.".format(cball.getX()))


if __name__ in ['__console__', '__main__']:
    main()