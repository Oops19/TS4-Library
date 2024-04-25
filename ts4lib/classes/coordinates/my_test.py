from ts4lib.classes.coordinates.std_vector3 import StdVector3
from ts4lib.classes.coordinates.std_quaternion import StdQuaternion


def tests():
    q = StdQuaternion(1, 0.1, 0.4,0.0)
    a = sum(n * n for n in q)
    print(a)

    print(f"q: {type(q)} = {q}")

    for n in q:
        print(f"n: {type(n)} = {n}")

    ql = q.as_list()
    print(f"ql: {type(ql)} = {ql}")


    ql = q.as_tuple()
    print(f"ql: {type(ql)} = {ql}")

    # qn = q
    qn = q.normalize()
    print(f"qn: {type(qn)} = {qn}")
    print(qn == qn)
# tests()

def a():
    p_zone = StdVector3(0, 0, 0)
    q_zone = StdQuaternion(1, 0, 0, 0)

    p_lot = StdVector3(100, 100, 100)
    q_lot = StdQuaternion(1, 0, 0, 0).normalize()

    p_object = StdVector3(100, 100, 100)
    q_object = StdQuaternion(1, 0, 0, 0).normalize()

    p_sim = StdVector3(100, 100, 100)
    q_sim = StdQuaternion(1, 0, 0, 0).normalize()
    p_rel = p_sim - p_object

    print(f"p_sim={p_sim}")
    print(f"p_object={p_object}")
    print(f"p_rel={p_rel}")

    print(f"Move x+1")
    p_sim = StdVector3(101, 100, 100)
    q_sim = StdQuaternion(1, 0, 0, 0).normalize()
    p_rel = p_sim - p_object
    print(f"p_sim={p_sim}")
    print(f"p_object={p_object}")
    p_rel = p_sim - p_object
    print(f"p_rel={StdVector3(p_rel)}")  # p_rel=(1.000, 0.000, 0.000)

    calc_p_sim = p_object + p_rel
    print(f"calc_p_sim={calc_p_sim}")  # (0.000, 101.000, 100.000, 100.000)

    print("-----\nSame as before but bed +45°")
    p_rel = StdVector3(1, 0, 0)
    q_object = StdQuaternion(0.924, 0, 0.383, 0).normalize()  # 45°
    rot_p_rel = q_object.rotate_vector(p_rel)
    print(f"rot_p_rel={rot_p_rel}")  # rot_p_rel=(0.707, 0.000, -0.707)
    calc_p_sim = p_object + rot_p_rel
    print(f"calc_p_sim={calc_p_sim}")  # calc_p_sim=(100.707, 100.000, 99.293)

    p_rel = calc_p_sim - p_object
    print(f"p_rel={StdVector3(p_rel)}")  # p_rel=(1.000, 0.000, 0.000)
    nq_object = q_object.conjugate()
    print(f"p_rel_fixe={nq_object.rotate_vector(p_rel)}")

    print("-----\nSame as before but bed +90°")
    p_rel = StdVector3(1, 0, 0)
    q_object = StdQuaternion(0.707, 0, 0.707, 0).normalize()  # 90°
    rot_p_rel = q_object.rotate_vector(p_rel)
    print(f"rot_p_rel={rot_p_rel}")  # rot_p_rel=(0.000, 0.000, -1.000)
    calc_p_sim = p_object + rot_p_rel
    print(f"calc_p_sim={calc_p_sim}")  # calc_p_sim=(100.000, 100.000, 99.000)

    p_rel = calc_p_sim - p_object
    print(f"p_rel={StdVector3(p_rel)}")  # p_rel=(1.000, 0.000, 0.000)
    nq_object = q_object.conjugate()
    print(f"p_rel_fixe={nq_object.rotate_vector(p_rel)}")  # reverse rotation of the vector to get the vector value without any applied rotation
a()

def c():
    p_zone = StdVector3(0, 0, 0)
    q_zone = StdQuaternion(1, 0, 0, 0)

    p_lot = StdQuaternion(0, 170, 150, 100)
    q_lot = StdQuaternion(0.7, 0, 0.8, 0).normalize()

    p_object = StdQuaternion(0, 172, 150, 110)
    q_object = StdQuaternion(0.9, 0, 0.2, 0).normalize()

    p_sim = StdQuaternion(0, 172, 150, 111)
    q_sim = StdQuaternion(0.5, 0, 0.7, 0).normalize()

    print(f"p_sim={p_sim}")
    print(f"p_object={p_object}")
    p_rel = p_sim - p_object
    print(f"p_rel={p_rel}")
