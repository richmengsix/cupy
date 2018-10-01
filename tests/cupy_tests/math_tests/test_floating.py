import unittest

import numpy

import cupy
from cupy import testing


@testing.gpu
class TestFloating(unittest.TestCase):

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_array_equal()
    def test_signbit(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        return xp.signbit(a)

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_array_equal()
    def test_copysign(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        b = testing.shaped_reverse_arange((2, 3), xp, dtype)
        return xp.copysign(a, b)

    @testing.for_float_dtypes(name='ftype')
    @testing.for_dtypes(['i', 'l'], name='itype')
    @testing.numpy_cupy_array_equal()
    def test_ldexp(self, xp, ftype, itype):
        a = xp.array([-3, -2, -1, 0, 1, 2, 3], dtype=ftype)
        b = xp.array([-3, -2, -1, 0, 1, 2, 3], dtype=itype)
        return xp.ldexp(a, b)

    @testing.for_float_dtypes()
    def test_frexp(self, dtype):
        numpy_a = numpy.array([-300, -20, -10, -1, 0, 1, 10, 20, 300],
                              dtype=dtype)
        numpy_b, numpy_c = numpy.frexp(numpy_a)

        cupy_a = cupy.array(numpy_a)
        cupy_b, cupy_c = cupy.frexp(cupy_a)

        testing.assert_array_equal(cupy_b, numpy_b)
        testing.assert_array_equal(cupy_c, numpy_c)

    @testing.for_all_dtypes(no_complex=True)
    @testing.numpy_cupy_array_equal()
    def test_nextafter(self, xp, dtype):
        a = testing.shaped_arange((2, 3), xp, dtype)
        b = testing.shaped_reverse_arange((2, 3), xp, dtype)
        return xp.nextafter(a, b)
