import itertools

class Vector(list):
    def __add__(self, other):
        if len(self) == len(other):
            result = Vector([s + o for s, o in itertools.izip(self, other)])
        else:
            raise ValueError("Vector size mismatch")
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float, complex)):
            """scala vector product"""
            result = Vector([s * other for s in self])
        elif isinstance(other, Vector):
            """dot product"""
            if len(self) == len(other):
                result = 0.0
                for s, o in itertools.izip(self, other):
                    result += s * o
            else:
                raise ValueError("Vector size mismatch")
        else:
            raise TypeError("Not defined")
        return result

    def __rmul__(self, other):
        return self * other

    def __abs__(self):
        square_sum = self * self
        result = square_sum ** 0.5
        return result

    def __pow__(self, power, modulo=None):
        return Vector([s ** power for s in self])

if __name__ == '__main__':
    import matplotlib.pylab as plt

    def main():
        x = Vector([1, 3, 0, -1, 5])
        print(x)
        print(dir())
        a = Vector([5,6,7])
        print(a)

        g_meter_per_second_per_second = -9.8
        u_meter_per_second = 60
        t_sec = Vector(range(0, 123)) * 0.1
        s = u_meter_per_second * t_sec +g_meter_per_second_per_second *0.5 * (t_sec ** 2)
        plt.plot(t_sec, s)
        plt.show()

    main()

