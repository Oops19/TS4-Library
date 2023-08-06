from ts4lib.classes.math.std_quaternion import StdQuaternion

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