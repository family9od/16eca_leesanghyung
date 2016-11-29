import itertools
import my_unittest2
from my_unittest2 import main

class MyMatrixTestCase(my_unittest2.MyTestCase):
    def assertMatrixAlmostEqual(self, mat1, mat2, msg=None, places=None, delta=None):
        self.assertEqual(len(mat1), len(mat2), msg="len(mat1 != len(mat2)")

        for row1, row2 in itertools.izip(mat1, mat2):
            self.assertMatrixAlmostEqual(row1, row2, msg=msg, places=places, delta=delta)

    def tearDown(self):
        for key in dir(self):
            attr = getattr(self, key)
            if key.startswith('mat_'):
                del attr[:]