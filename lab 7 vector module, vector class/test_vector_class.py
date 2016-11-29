import my_unittest
import vector_class as vc

class TestVectorClass(my_unittest.MyTestCase):
    def setUp(self):
        self.x_element_0 = 1.0
        self.x_element_1 = 2.0
        self.x_list = [self.x_element_0, self.x_element_1]
        self.x = vc.Vector(self.x_list)

        self.y_element_0 = 4.0
        self.y_element_1 = 3.0
        self.y_list = [self.y_element_0, self.y_element_1]
        self.y = vc.Vector(self.y_list)

    def test_get_item(self):
        self.assertEqual(self.x_element_0, self.x[0])
        self.assertEqual(self.x_element_1, self.x[1])

    def test_len(self):
        self.assertEqual(len(self.x_list), len(self.x))

    def test_add(self):
        z = self.x + self.y

        self.assertSequenceEqual([self.x_element_0 + self.y_element_0, self.x_element_1 + self.y_element_1], z)

    def test_scalar_product(self):
        ratio = 2.0
        z = self.x * ratio

        self.assertSequenceEqual([self.x_element_0 * ratio, self.x_element_1 * ratio], z)

        w = ratio * self.y

        self.assertSequenceEqual([self.y_element_0 * ratio, self.y_element_1 * ratio], w)

    def test_dot_product(self):
        z = self.x * self.y
        self.assertEqual(self.x_element_0 * self.y_element_0 + self.x_element_1 * self.y_element_1, z)

    def test_abs(self):
        z = abs(self.y)
        self.assertAlmostEqual((self.y_element_0 ** 2 + self.y_element_1 ** 2)**0.5, z)

    def test_element_wise_power(self):
        p = 2
        z = self.y ** p
        self.assertSequenceEqual([self.y_element_0 **p, self.y_element_1 ** p], z)

if __name__ == '__main__':
    my_unittest.main()

