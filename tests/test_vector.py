from pytest import raises

from spock.vector import BaseVector, CartesianVector, Vector3


def test_basevector(_class=BaseVector):
    vec = _class(1, 2, 3)

    # Iteration :

    ivec = iter(vec)

    assert next(ivec) == 1
    assert next(ivec) == 2
    assert next(ivec) == 3

    with raises(StopIteration):
        next(ivec)

    # __(g/s)etitem__

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

    # len

    assert len(vec) == 3
    assert len(_class(*range(100))) == 100


def test_cartesianvector(_class=CartesianVector):
    # check inheritance
    test_basevector(_class)

    vec = _class(1, -2, 3)

    # abs
    avec = abs(vec)

    assert vec[0] == 1
    assert vec[1] == -2
    assert vec[2] == 3

    assert avec[0] == 1
    assert avec[1] == 2
    assert avec[2] == 3

    del vec, avec

    # sub/neg
    v1 = _class(-1, 2, 1)
    v_1 = - v1
    v2 = v1 - v_1

    assert len(v2) == 3
    assert v2[0] == -2
    assert v2[1] == 4
    assert v2[2] == 2

    del v1, v_1, v2

    # add

    v1 = _class(-1, 2, 1)

    v2 = v1 + v1

    assert len(v2) == 3
    assert v2[0] == -2
    assert v2[1] == 4
    assert v2[2] == 2

    del v1, v2

    # sum do not work with strings :(
    # # Who said duck typing ?
    #
    # v1 = _class(1, "a")
    # v2 = _class(2, "b")
    #
    # v3 = v1 + v2
    #
    # assert len(v3) == 2
    # assert v3[0] == 3
    # assert v3[1] == "ab"
    #
    # del v1, v2, v3

    # mul + duck typing

    v1 = _class("a", "b")
    v2 = _class(2, 4)

    v3 = v1 * v2

    assert len(v3) == 2
    assert v3[0] == "aa"
    assert v3[1] == "bbbb"

    del v1, v2, v3

    # Well, with the evolution of int/float in py3, division is hard :/

    # div

    # v3 = _class(1, 2) // _class(2, 3)

    # assert v3[0] == 0.5
    # assert v3[1] == 2/3
    # assert float(v3[1]) == 2./3.

    # trunc

    v1 = _class(1.1, 2.9)
    v1 = v1.trunc()

    assert v1[0] == 1
    assert v1[1] == 2

    del v1

    # norm

    v1 = _class(3, 4)

    assert v1.norm() == 5

    del v1

    # Comparisons

    v1 = _class(1, 2, 3)
    v2 = _class(3, 2, 1)

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


def test_vector3(_class=Vector3):

    with raises(AssertionError):
        v1 = _class(1, 2)
    with raises(AssertionError):
        v1 = _class(1, 2, 3, 4)

    v1 = _class(1, 2, 3)

    assert v1.x == 1
    assert v1.y == 2
    assert v1.z == 3

    v1.x = 100
    v1.y = 200
    v1.z = 300

    assert v1.x == 100
    assert v1.y == 200
    assert v1.z == 300

    di = v1.get_dict()

    assert len(di) == 3
    assert di["x"] == 100
    assert di["y"] == 200
    assert di["z"] == 300

    di["z"] = 123

    v1.set_dict(di)

    assert v1.x == 100
    assert v1.y == 200
    assert v1.z == 123

    del v1

    # Yaw/pitch
    # All data come from http://wiki.vg/Protocol#Player_Look

    # yp = _class(1, 0, 0).yaw_pitch()

    # assert len(yp) == 2
    # assert yp.yaw == 0
    # assert yp.pitch == 90

    # uv = yp.unit_vector()

    # assert uv[0] == 1
    # assert uv.y == 0
    # assert uv[2] == 0
    # assert len(uv) == 3
