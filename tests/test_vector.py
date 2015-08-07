from pytest import raises

from spock.vector import BaseVector, CartesianVector, Vector3


def test_basevector_iter():
    vec = BaseVector(1, 2, 3)

    # Iteration :

    ivec = iter(vec)

    assert next(ivec) == 1
    assert next(ivec) == 2
    assert next(ivec) == 3

    with raises(StopIteration):
        next(ivec)


def test_basevector_gsetitem():
    vec = BaseVector(1, 2, 3)

    assert vec[0] == 1
    assert vec[1] == 2
    assert vec[2] == 3

    vec[0] = 100
    vec[1] = 200
    vec[2] = 300

    assert vec[0] == 100
    assert vec[1] == 200
    assert vec[2] == 300

    # BaseVector doesn't care about the type, duck typing & co ;)
    vec[0] = "100"
    vec[1] = "200"
    vec[2] = "300"

    assert vec[0] == "100"
    assert vec[1] == "200"
    assert vec[2] == "300"


def test_basevector_len():
    vec = BaseVector(1, 2, 3)

    assert len(vec) == 3
    assert len(BaseVector(*range(100))) == 100


def test_cartesianvector_abs():
    vec = CartesianVector(1, -2, 3)

    avec = abs(vec)

    assert vec[0] == 1
    assert vec[1] == -2
    assert vec[2] == 3

    assert avec[0] == 1
    assert avec[1] == 2
    assert avec[2] == 3


def test_cartesianvector_subneg():
    v1 = CartesianVector(-1, 2, 1)
    v_1 = - v1
    v2 = v1 - v_1

    assert len(v2) == 3
    assert v2[0] == -2
    assert v2[1] == 4
    assert v2[2] == 2


def test_cartesianvector_add():

    v1 = CartesianVector(-1, 2, 1)

    v2 = v1 + v1

    assert len(v2) == 3
    assert v2[0] == -2
    assert v2[1] == 4
    assert v2[2] == 2

    # sum do not work with strings :(
    # # Who said duck typing ?
    #
    # v1 = CartesianVector(1, "a")
    # v2 = CartesianVector(2, "b")
    #
    # v3 = v1 + v2
    #
    # assert len(v3) == 2
    # assert v3[0] == 3
    # assert v3[1] == "ab"
    #
    # del v1, v2, v3


def test_cartesianvector_mul():

    v1 = CartesianVector("a", "b")
    v2 = CartesianVector(2, 4)

    v3 = v1 * v2

    assert len(v3) == 2
    assert v3[0] == "aa"
    assert v3[1] == "bbbb"


def test_cartesianvector_div():
    pass

    # Well, with the evolution of int/float in py3, division is hard :/

    # div

    # v3 = CartesianVector(1, 2) // CartesianVector(2, 3)

    # assert v3[0] == 0.5
    # assert v3[1] == 2/3
    # assert float(v3[1]) == 2./3.


def test_cartesianvector_trunc():

    v1 = CartesianVector(1.1, 2.9)
    v1 = v1.trunc()

    assert v1[0] == 1
    assert v1[1] == 2


def test_cartesianvector_norm():

    v1 = CartesianVector(3, 4)

    assert v1.norm() == 5

    v1 = CartesianVector(-3, -4)

    assert v1.norm() == 5


def test_cartesianvector_comps():

    v1 = CartesianVector(1, 2, 3)
    v2 = CartesianVector(3, 2, 1)

    v3 = v1 <= v2
    assert v3[0] is True
    assert v3[1] is True
    assert v3[2] is False

    v3 = v1 < v2
    assert v3[0] is True
    assert v3[1] is False
    assert v3[2] is False

    v3 = v1 >= v2
    assert v3[0] is False
    assert v3[1] is True
    assert v3[2] is True

    v3 = v1 > v2
    assert v3[0] is False
    assert v3[1] is False
    assert v3[2] is True

    v3 = v1 == v2

    assert v3[0] is False
    assert v3[1] is True
    assert v3[2] is False


def test_vector3_raises():

    with raises(AssertionError):
        v1 = Vector3(1, 2)
    with raises(AssertionError):
        v1 = Vector3(1, 2, 3, 4)
    with raises(AssertionError):
        # Different length, should make a shorter vector3
        # And I need to reuse v1, because flake8
        v1 = Vector3(1, 2, 3)
        v1 = v1 + CartesianVector(1, 2)


def test_vector3_shortcuts():

    v1 = Vector3(1, 2, 3)

    assert v1.x == 1
    assert v1.y == 2
    assert v1.z == 3

    v1.x = 100
    v1.y = 200
    v1.z = 300

    assert v1.x == 100
    assert v1.y == 200
    assert v1.z == 300


def test_vector3_dict():

    v1 = Vector3(1, 2, 3)

    di = v1.get_dict()

    assert len(di) == 3
    assert di["x"] == 1
    assert di["y"] == 2
    assert di["z"] == 3

    di["z"] = 123

    v1.set_dict(di)

    assert v1.x == 1
    assert v1.y == 2
    assert v1.z == 123

    # Yaw/pitch
    # All data come from http://wiki.vg/Protocol#Player_Look

    # yp = Vector3(1, 0, 0).yaw_pitch()

    # assert len(yp) == 2
    # assert yp.yaw == 0
    # assert yp.pitch == 90

    # uv = yp.unit_vector()

    # assert uv[0] == 1
    # assert uv.y == 0
    # assert uv[2] == 0
    # assert len(uv) == 3
