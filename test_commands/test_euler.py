#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#
#
from ts4lib.classes.coordinates.vector_interface import VectorInterface

if __name__ == '__main__':
    from ts4lib.classes.coordinates.std_quaternion import StdQuaternion
    from ts4lib.classes.coordinates.std_vector3 import StdVector3
    from ts4lib.classes.coordinates.std_euler_angle import StdEulerAngle
    r'''
    @param roll: x-axis rotation in rad (axis to the right)
    @param pitch: y-axis rotation in rad (axis to the top)
    @param yaw: z-axis rotation in rad (axis to the viewer)
    '''
    # Z X Y
    roll, pitch, yaw = -80, 0, 0
    ea = StdEulerAngle(roll, pitch, yaw, convert_deg_to_rad=True)
    print(ea)
    q: StdQuaternion = ea.quaternion()
    print(q)

    print(StdEulerAngle(1.571, 3.142, 4.712).deg())
    print(StdEulerAngle(90, 180, 270, True).rad())

    print(StdEulerAngle(1.571, 3.142, 4.712))
    print(StdEulerAngle(90, 180, 270, True))


    roll, pitch, yaw = 180.000, -74.708, 180.000
    ea = StdEulerAngle(roll, pitch, yaw)
    print(ea)
    print(ea.format(digits=4, unit=' mm'))
    q: StdQuaternion = ea.quaternion()
    print(q)

    ea4 = StdEulerAngle(0, 0, 0)
    q4: StdQuaternion = ea4.quaternion()
    print(f"q={q4}")
    print(f"a={ea4}  {ea4.deg()}")

    q2 = StdQuaternion( 0.996, 0,  -0.093, 0)
    q3 = q2.normalize()
    ea3: StdEulerAngle = q3.euler_angles()
    print(f"q={q3}")
    print(f"a={ea3} {ea3.deg()}")

    print(ea3.as_tuple())

    ea = StdEulerAngle(0, 10.5, 11.12345, convert_deg_to_rad=True)
    print(f"a={ea} {ea.deg()}")

    s = ea.serialize()
    print(f"s={s}")
    b = VectorInterface().deserialize(s)
    print(f"a={b} {b.deg()}")

