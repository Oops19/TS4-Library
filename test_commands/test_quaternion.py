#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#
#

from ts4lib.classes.coordinates.vector_interface import VectorInterface

if __name__ == '__main__':
    from ts4lib.classes.coordinates.std_quaternion import StdQuaternion
    from ts4lib.classes.coordinates.std_vector3 import StdVector3

    q = StdQuaternion(1, 0.1, 0.4,0.0)
    print(f"q: {q.__class__.__name__} = {q} - (not normalized)")

    qn = q.normalize()
    print(f"qn: {qn.__class__.__name__} = {qn} - (normalized)")

    qc = qn.conjugate()
    print(f"qc: {qc.__class__.__name__} = {qc} - (conjugate)")

    qn_rnd = qn.randomize()
    print(f"qn_rnd: {qn_rnd.__class__.__name__} = {qn_rnd} - (qn.randomize())")

    q_mul = qn * qc
    print(f"q_mul: {q_mul.__class__.__name__} = {q_mul} - (qn*qc)")

    q_mul = qn * qn
    print(f"q_mul: {q_mul.__class__.__name__} = {q_mul} - (qn*qn)")

    q_div = qn / qc
    print(f"q_div: {q_div.__class__.__name__} = {q_div} - (qn/qc = qn*qc.conjugate() = qn*qn)")

    q_div = qn / qn
    print(f"q_div: {q_div.__class__.__name__} = {q_div} - (qn/qn = qn*qn.conjugate() = qn*qc)")

    roll, pitch, yaw = qn.get_euler_angles()
    print(f"roll / pitch / yaw = {roll:.3f} / {pitch:.3f} / {yaw:.3f}")

    q_add = qn + qn
    print(f"q_add: {q_add.__class__.__name__} = {q_add} - (qn+qn) -> not normalized)")

    q_add = qn.add(qn)
    print(f"q_add: {q_add.__class__.__name__} = {q_add} - (qn.add(qn) -> normalized)")

    q_sub = qn - qc
    print(f"q_sub: {q_sub.__class__.__name__} = {q_sub} - (qn-qc) -> not normalized)")

    q_sub = qn.sub(qc)
    print(f"q_sub: {q_sub.__class__.__name__} = {q_sub} - (qn.sub(qc) -> normalized)")

    ql = q.as_list()
    print(f"ql: {type(ql)} = {ql} - (list)")

    qt = q.as_tuple()
    print(f"qt: {type(qt)} = {qt} - (tuple)")

    eq = (q_div == StdQuaternion())
    print(f"eq = {eq} - (q_div == StdQuaternion() - tolerance=0.001)")

    eq = q_div.equals(StdQuaternion())
    print(f"eq = {eq} - (q_div.equals(StdQuaternion()), tolerance=0.001)")

    eq = q_div.equals(StdQuaternion(), tolerance=0)
    print(f"eq = {eq} - (q_div.equals(StdQuaternion()), tolerance=0)")

    delta = q_div.delta(StdQuaternion())
    print(f"delta = {delta:.20f} - (q_div.delta(StdQuaternion()))")

    v = StdVector3(1, 0, 0)
    print(f"v: {v.__class__.__name__} = {v}")

    v_rot = qn.rotate_vector(v)
    print(f"v_rot: {v_rot.__class__.__name__} = {v_rot} - (qn.rotate(v))")

    q = StdQuaternion(1, 1, 1, 1)
    q_rnd = q.randomize()
    print(f"q_rnd: {q_rnd.__class__.__name__} = {q_rnd} - (q.randomize())")

    qn = q_rnd.normalize()
    print(f"qn: {qn.__class__.__name__} = {qn} - (normalized)")

    q = StdQuaternion(4, 3, 1, 1)
    print(f"q: {q.__class__.__name__} = {q}")
    qn = q.normalize()
    print(f"qn: {qn.__class__.__name__} = {qn} - (normalized)")

    s = qn.as_tuple()
    print(f"s: {s.__class__.__name__} = {s}")
    qs = StdQuaternion(*s)
    print(f"qs: {qs.__class__.__name__} = {qs}")

    s = qn.serialize()
    print(f"s: {s.__class__.__name__} = {s}")
    qs = VectorInterface().deserialize(s)
    print(f"qs: {qs.__class__.__name__} = {qs}")

    """
    On-Load LOT Vector3(360.993591, 150.000366, 383.993347) Quaternion(0.000000, 0.707191, 0.000000, -0.707023)
    On-Load OBJ Vector3Immutable(351.990509, 150.000015, 396.991211) QuaternionImmutable(-0.000000, -0.000345, -0.000000, 1.000000)
    On-Load SIM Vector3Immutable(351.640381, 150.000015, 397.090881) QuaternionImmutable(0.000000, 0.643143, 0.000000, -0.765746)
    On-Load DLT Vector3(0.100006, 0.000000, 0.350021) Quaternion()
    DST sim positions Vector3(351.640381, 150.000015, 397.090881) << Vector3(-0.350114, 0.000000, 0.099681) << Vector3(-0.350045, 0.000000, 0.099923) << Vector3(0.100006, 0.000000, 0.350021)
    DST sim orientations Quaternion(0.000000, 0.643143, 0.000000, -0.765746) << Quaternion(0.000000, 0.643143, 0.000000, -0.765746) << Quaternion(0.000000, 0.642878, 0.000000, -0.765968) << Quaternion(0.000000, 0.087156, 0.000000, 0.996195)
    Loaded SIM Vector3Immutable(351.640381, 150.000015, 397.090881) QuaternionImmutable(0.000000, 0.643143, 0.000000, -0.765746)
    Successfully set the position of Sim.
    
    dst SIM orientations (-0.766, 0.000, 0.643, 0.000) << (-0.766, 0.000, 0.643, 0.000) << (-0.766, 0.000, 0.643, 0.000) << (0.996, 0.000, 0.087, 0.000)
    
    
    orientation_relative_to_lot = CommonQuaternion.multiply(lot_orientation, orientation)
    orientation_relative_to_lot_and_object = CommonQuaternion.multiply(object_orientation, orientation_relative_to_lot)
    new_sim_rotation = CommonQuaternion.normalize(orientation_relative_to_lot_and_object)  # normalize it before using it in TS4
    self.log.debug(f"DST sim orientations {new_sim_rotation} << {orientation_relative_to_lot_and_object} << {orientation_relative_to_lot} << {orientation}")
    self.log.debug(f"Loaded SIM {sim_position} {sim_orientation}")
    
    DST sim orientations Quaternion(0.000000, 0.643143, 0.000000, -0.765746) << Quaternion(0.000000, 0.643143, 0.000000, -0.765746) << Quaternion(0.000000, 0.642878, 0.000000, -0.765968) << Quaternion(0.000000, 0.087156, 0.000000, 0.996195)
    DST sim orientations (0.000, 0.766, 0.000, 0.643) << (0.000, 0.766, 0.000, 0.643) << (0.643, 0.000, -0.766, 0.000) << (0.000, 0.087, 0.000, 0.996)
    """
    lot_orientation = StdQuaternion( -0.707023, 0.000000, 0.707191, 0.000000,)  # w=0.707
    object_orientation = StdQuaternion( 1.000000, -0.000000, -0.000345, -0.000000,)  # w=-0.0003
    orientation = StdQuaternion(0.996195, 0.000000, 0.087156, 0.000000, )  # w=0.087
    orientation_relative_to_lot = lot_orientation.multiply(orientation)
    orientation_relative_to_lot_and_object = object_orientation * orientation_relative_to_lot
    new_sim_rotation = orientation_relative_to_lot_and_object.normalize()
    print(f"dst SIM orientations {new_sim_rotation} << {orientation_relative_to_lot_and_object} << {orientation_relative_to_lot} << {orientation}")


    print(f"orientation_relative_to_lot={orientation_relative_to_lot}")

    # from sims4communitylib.classes.math.common_quaternion import CommonQuaternion
    # lot_orientation = CommonQuaternion(0.000000, 0.707191, 0.000000, -0.707023)