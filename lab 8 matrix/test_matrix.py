import unittest

import matrix as m

class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.mat_a = [[11,12],
                      [21,22]]
        self.mat_b = [[1100,1200],
                      [2100, 2200]]
        self.mat_i = [[1,0],
                      [0,1]]
        self.mat_c = [[11,12,13],
                      [21,22,23],
                      [31,32,33]]
        self.mat_d = [[1,2,3],
                      [0,4,5],
                      [0, 0, 6]]

        self.mat_e = [[2, 2, 0],
                      [-2, 1, 1],
                      [3, 0, 1]]
        self.mat_adj_e = [[1, -2, 2],
                          [5, 2, -2],
                          [-3, 6, 6]]
        self.mat_g = [[1, 0, -1],
                      [0, 1, 2],
                      [-2, -1, 0]]


    def tearDown(self):
        for key in dir(self):
            attr = getattr(self, key)
            if key.startswith('mat_'):
                del attr[:]

    def test_add01(self):
        self.mat_r = m.add_mat(self.mat_a, self.mat_b)
        self.mat_exp = [[self.mat_a[0][0] + self.mat_b[0][0], self.mat_a[0][1] + self.mat_b[0][1]],
                        [self.mat_a[1][0] + self.mat_b[1][0], self.mat_a[1][1] + self.mat_b[1][1]], ]
        self.assertSequenceEqual(self.mat_r, self.mat_exp)

    def test_add02(self):
        self.mat_r = m.add_mat(self.mat_a, self.mat_a)
        self.mat_exp = [[self.mat_a[0][0] + self.mat_a[0][0], self.mat_a[0][1] + self.mat_a[0][1]],
                        [self.mat_a[1][0] + self.mat_a[1][0], self.mat_a[1][1] + self.mat_a[1][1]], ]
        self.assertSequenceEqual(self.mat_r, self.mat_exp)

    def test_scala_mul01(self):
        self.mat_r = m.scalar_mul_mat(1, self.mat_a)
        self.mat_exp = [[self.mat_a[0][0] , self.mat_a[0][1] ],
                        [self.mat_a[1][0] , self.mat_a[1][1] ], ]
        self.assertSequenceEqual(self.mat_r, self.mat_exp)

    def test_scala_mul02(self):
        self.mat_r = m.scalar_mul_mat(2.0, self.mat_a)
        self.mat_exp = [[self.mat_a[0][0] *2.0 , self.mat_a[0][1] *2.0 ],
                        [self.mat_a[1][0] *2.0 , self.mat_a[1][1] *2.0 ], ]
        self.assertSequenceEqual(self.mat_r, self.mat_exp)

    def test_scala_mul03(self):
        self.mat_r = m.scalar_mul_mat(-1, self.mat_a)
        self.mat_exp = [[-self.mat_a[0][0] , -self.mat_a[0][1] ],
                        [-self.mat_a[1][0] , -self.mat_a[1][1] ], ]
        self.assertSequenceEqual(self.mat_r, self.mat_exp)

    def test_transpose(self):
        self.mat_r = m.transpose_mat(self.mat_a)
        self.mat_exp = [[self.mat_a[0][0], self.mat_a[1][0]],
                        [self.mat_a[0][1], self.mat_a[1][1]],]
        self.assertSequenceEqual(self.mat_r, self.mat_exp)

    def test_mul_mat_vec01(self):
        x = [0, 1]
        vec_c = m.mul_mat_vec(self, mat_a, x)
        vec_e = [self.mat_a[0][0], self.mat_a[1][0]]
        self.assertSequenceEqual(vec_c, vec_e)

    def test_mul_mat_vec02(self):
        vec_y = [0, 1]
        vec_c = m.mul_mat_vec(self.mat_a, vec_y)
        vec_e = [self.mat_a[0][1], self.mat_a[1][1]]
        self.assertSequenceEqual(vec_c, vec_e)

    def test_mul_mat01(self):
        self.mat_r = m.mul_mat(self.mat_a, self.mat_i)
        self.assertSequenceEqual(self.mat_r, self.mat_a)

    def test_mul_mat02(self):
        self.mat_r = m.mul_mat(self.mat_i, self.mat_a)
        self.assertSequenceEqual(self.mat_r, self.mat_a)

    def test_cofactor01(self):
        self.mat_r = m.get_cofactor_matrix(self.mat_c, 0, 0)
        self.mat_exp = [[self.mat_c[1][1], self.mat_c[1][2]],
                        [self.mat_c[2][1], self.mat_c[2][2]]]
        self.assertSequenceEqual(self.mat_r, self.mat_exp)

    def test_cofactor02(self):

        self.mat_r = m.get_cofactor_matrix(self.mat_c, 0, 1)
        self.mat_exp = [[self.mat_c[1][0], self.mat_c[0][2]],
                        [self.mat_c[2][0], self.mat_c[2][2]]]
        self.assertSequenceEqual(self.mat_r, self.mat_exp)

    def test_cofactor03(self):
        self.mat_r = m.get_cofactor_matrix(self.mat_c, 1, 1)
        self.mat_exp = [[self.mat_c[0][0], self.mat_c[0][2]],
                        [self.mat_c[2][0], self.mat_c[2][2]]]
        self.assertSequenceEqual(self.mat_r, self.mat_exp)

    def test_cofactor04(self):
        self.mat_r = m.get_cofactor_matrix(self.mat_c, 2, 1)
        self.mat_exp = [[self.mat_c[0][0], self.mat_c[0][2]],
                        [self.mat_c[1][0], self.mat_c[1][2]]]
        self.assertSequenceEqual(self.mat_r, self.mat_exp)

    def test_cofactor05(self):
        self.mat_r = m.get_cofactor_matrix(self.mat_e, 0, 0)
        self.mat_exp = [[1, 1],
                        [0, 1]]
        self.assertSequenceEqual(self.mat_r, self.mat_exp)

    def test_cofactor06(self):
        self.mat_r = m.get_cofactor_matrix(self.mat_e, 0, 1)
        self.mat_exp = [[-2, 1],
                        [3, 1]]
        self.assertSequenceEqual(self.mat_r, self.mat_exp)

    def test_det01(self):
        d = m.det(self.mat_i)
        self.assertEqual(d,1,0)

    def test_det01(self):
        d = m.det(self.mat_i)
        self.assertEqual(d,1.0)

    def test_det02(self):
        d = m.det(self.mat_d)
        self.assertEqual(d,24.0)

    def test_det03(self):
        d = m.det(self.mat_a)
        e = self.mat_a[0][0] * self.mat_a[1][1] - self.mat_a[0][1] * self.mat_a[1][0]
        self.assertEqual(d, e)

    def test_adk01(self):
        self.mat_r = m.adjugate_matrix(self.mat_d)
        d = m.det(self.mat_d)
        self.mat_exp = [[d, 0, 0],
                        [0, d, 0],
                        [0, 0, d]]
        self.assertEqual(m.mul_mat(self.mat_r, self.mat_d), self.mat_exp)
        self.assertEqual(m.mul_mat(self.mat_d, self.mat_r), self.mat_exp)

    def test_adj02(self):
        self.mat_r = m.adjugate_matrix(self.mat_e)
        self.assertEqual(self.mat_r, self.mat_adj_e)

    def test_row_mul_scalar_00(self):
        m.row_mul_scalar(self.mat_i, 0, 2)
        self.mat_exp = [[2, 0],
                        [0, 1]]
        self.assertSequenceEqual(self.mat_i, self.mat_exp)

    def test_row_mul_scalar_01(self):
        m.row_mul_scalar(self.mat_i, 1, 0.5)
        self.mat_exp = [[1, 0],
                        [0, 0.5]]
        self.assertSequenceEqual(self.mat_i, self.mat_exp)

    def test_row_mul_scalar_02(self):
        m.row_mul_scalar(self.mat_g, 1, -1)
        self.mat_exp = [[1, 0, -1],
                        [0, -1, -2],
                        [-2, -1, 0]]
        self.assertSequenceEqual(self.mat_g, self.mat_exp)

    def test_row_mul_scalar_03(self):
        m.row_mul_scalar(self.mat_g, 2, 0.5)
        self.mat_exp = [[1, 0, -1],
                        [0, 1, 2],
                        [-1.0, -0.5, 0.0]]
        self.assertSequenceEqual(self.mat_g, self.mat_exp)

    def test_row_mac_00(self):
        m.row_mul_add(self.mat_l, 0, 1, 1)
        self.mat_exp = [[1, 1],
                        [0, 1], ]
        self.assertSequenceEqual(self.mat_l, self.mat_exp)

    def test_row_mac_01(self):
        det_before = m.det(self.mat_l)
        m.row_mul_add(self.mat_l, 1, 0, 0.5)
        det_after = m.det(self.mat_l)

        self.mat_exp = [[1, 0],
                        [0.5, 1.0], ]
        self.assertSequenceEqual(self.mat_l, self.mat_exp)
        self.assertEqual(det_before, det_after)

    def test_row_mac_02(self):
        det_before = m.det(self.mat_g)
        m.row_mul_add(self.mat_g, 1, 2, -1)
        det_after = m.det(self.mat_g)

        self.mat_exp = [[1, 0, -1],
                        [2, 2, 2],
                        [-2, -1, 0]]
        self.assertSequenceEqual(self.mat_g, self.mat_exp)
        self.assertEqual(det_before, det_after)

    def test_row_mac_03(self):
        det_before = m.det(self.mat_g)
        m.row_mul_add(self.mat_g,0,2,0.5)
        det_after = m.det(self.mat_g)
        self.mat_exp = [[0, -0.5, -1.0],
                        [0, 1 ,2],
                        [-2, -1, 0]]
        self.assertSequenceEqual(self.mat_g, self.mat_exp)
        self.assertEqual(det_before, det_after)


if "__main__" == __name__:
    unittest.main()










































































