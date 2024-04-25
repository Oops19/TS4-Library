#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#
#
import math

from ts4lib.classes.coordinates.std_euler_angle import StdEulerAngle
from ts4lib.classes.coordinates.std_vector2 import StdVector2
from ts4lib.classes.coordinates.vector_interface import VectorInterface

if __name__ == '__main__':
    from ts4lib.classes.coordinates.std_quaternion import StdQuaternion
    from ts4lib.classes.coordinates.std_vector3 import StdVector3

    v1 = StdVector3(3, 0, 0)
    v1 = v1.randomize()
    print(f"v1: {v1.__class__.__name__} = {v1}")

    v2 = StdVector3(1, 1, 1)
    v2 = v2.randomize()
    print(f"v2: {v2.__class__.__name__} = {v2}")

    v_add = v1 + v2
    print(f"v_add: {v_add.__class__.__name__} = {v_add}")

    v_sub = v1 - v2
    print(f"v_sub: {v_sub.__class__.__name__} = {v_sub}")

    v_eq = v1 == v2
    print(f"v_eq: {v_eq.__class__.__name__} = {v_eq}")

    v_dot: float = v1.dot(v2)
    print(f"v_dot: {v_dot.__class__.__name__} = {v_dot}")

    v_cross = v1.cross(v2)
    print(f"v_cross: {v_cross.__class__.__name__} = {v_cross}")

    print(f"v2: {v2.__class__.__name__} = {v2}")
    s = v2.serialize()
    print(f"s: {s.__class__.__name__} = {s}")
    vs = VectorInterface().deserialize(s)
    print(f"vs: {vs.__class__.__name__} = {vs}")

    a = {'std_3d_vector.Std3DVector': (0.5735553769620676, -0.4349190695349341, 0.8150967994474205)}


    # Vectors support all VectorInterface operations:
    # v.delta(v2)
    # v.equals(v2, tolerance=tolerance)
    # v.as_list()
    # v.as_tuple()
    # v.randomize()

    v = StdVector3(-0.525269, 0.000000, -0.162415)
    print(v.length())

    v = StdVector3(0.018127, 0.000000, -0.549506)
    print(v.length())

    v = StdVector3(0.534830, 0.000000, -0.127444)
    print(v.length())

    v = StdVector3(0.576721, 0.000000, 0.164703)
    print(v.length())

    v = StdVector3(0.006764, 0.000000, -0.599741)
    print(v.length())

    v = StdVector3(0.580289, 0.000000, -0.151653)
    print(v.length())

    v = StdVector3(1.115119457244873, 0.0, -0.2790972590446472)
    print(v.length())
    print(v.z)

    v = StdVector2(1.1, 1.1, axis_names=('x', 'z'))
    w = StdVector2(0,1, axis_names=('x', 'z'))
    print(v.cross(w))
    print(w.cross(v))
    print(v.cross_3d(w))
    print(w.cross_3d(v))
    vv = StdVector3(v)
    ww = StdVector3(w)
    print(vv.cross(ww))
    print(ww.cross(vv))

    v1 = StdVector3(0, 0, -30)  # set y=0
    v2 = StdVector3(10, 10, -30)  # set y=0
    len_v1 = v1.length()
    len_v2 = v2.length()
    a: StdVector3 = v1.cross(v2)
    q: StdQuaternion = StdQuaternion(a)
    print(q)
    dot = v1.dot(v2)
    w = math.sqrt((len_v1 ** 2) * (len_v2 ** 2)) + dot
    q = StdQuaternion(w, q.x, q.x, q.z)
    print(q.format(digits=1, keep_trailing_zero=True))
    qn = q.normalize()
    print(q)
    ea = StdEulerAngle(*q.get_euler_angles())
    print(ea.deg())
    r'''
    Quaternion q;
    vector a = crossproduct(v1, v2);
    q.xyz = a;
    q.w = sqrt((v1.Length ^ 2) * (v2.Length ^ 2)) + dotproduct(v1, v2); 
    '''

    v = StdVector3(None)
    print(v)

    o_v = StdVector3(208.025, 158.244, 218.214)
    o_q = StdQuaternion(0.709, 0, 0.705, 0)
    s_v = StdVector3(208.115, 158.102, 218.428)
    s_q = StdQuaternion(0.707, -0.055, 0.705, -0)
    d = s_v - o_v
    print(d)
    conjugated_object_q = o_q.conjugate()
    print(conjugated_object_q)
    rotated_v = o_q.rotate_vector(d)
    print(rotated_v)
    r'''
    On-Save OBJ (208.025, 158.244, 218.214) (0.709, 0, 0.705, 0)
    On-Save SIM (208.115, 158.102, 218.428) (0.707, -0.055, 0.705, -0)
    SRC sim positions (0.09, -0.142, 0.213) >> (-0.784, -0.522, 0.335)
    '''
