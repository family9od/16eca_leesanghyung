import gauss_jordan as gj
import matrix as m
import my_unittest

class TestGaussJordan(my_unittest.MyTestCase):

    def test_gauss_jordan_00(self):
        for n in range(3, 10):
            mat_a = m.get_random_mat(n,n)

            mat_a_inv = gj.gauss_jordan(mat_a)
            mat_b = m.mul_mat(mat_a, mat_a_inv)

            for i in range(n):
                vec_exp = [0.0] * n
                vec_exp[i] = 1.0
                vec_res = mat_b[i]
                self.assertSequenceAlmostEqual(vec_exp, vec_res)

                del vec_exp

            del mat_b[:]
            del mat_b
            del mat_a_inv[:]
            del mat_a_inv
            del mat_a[:]
            del mat_a

if "__main__" == __name__:
    my_unittest.main()

