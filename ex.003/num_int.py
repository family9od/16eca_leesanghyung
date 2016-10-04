# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이 사용되었다는 점을 표시하는 것임

# 수학 관련 기능을 담고 있는 math 모듈에서 exp 함수를 불러들임
# 2010112033 이상형 9.27

from math import exp

def rect0(f, xi, xe, n=100):
    """
    0차 수치 적분
    xi ~ xe 사이를 n개의 구획으로 나눔
    한 구획안에서는 f(x)가 상수일 것이라고 가정함
    :param f: 적분할 함수
    :param xi: 정적분 시작 지점
    :param xe: 정적분 끝지점
    :param n: 구획을 나누는 갯수
    :return: f(x)를 xi ~ xe 구간에서 정적분한 근사값
    """
    # 초기화 시작
    # n개로 나눈 각 구획의 길이를 정함
    delta_x = (float(xe) - float(xi)) / n

    # 각 구획 중간 지점 x값의 list 를 만듦
    x = [xi + delta_x * (0.5 + k) for k in xrange(n)]

    result = 0.0

    # 초기화 끝

    # 주 반복문  main loop
    for k in xrange(n):
        xk = x[k]
        area_k = f(xk) * delta_x
        result += area_k

    # 주 반복문 끝

    return result

def trapezoid1(f, xi, xe, n=100):
    delta_x = (float(xe) - float(xi)) / n
    xk = xi
    fxk = f(xk)

    result = 0.0
    # 초기화 끝

    for k in xrange(n):
        xk1 = xk + delta_x
        fxk1 = f(xk1)
        area_k = (fxk + fxk1) * delta_x * 0.5
        result += area_k
        xk = xk1
        fxk = fxk1
    # 주 반복문 끝

    return result

def simpson2(f, xi, xe, n=100, b_verbose=False):
    """
    2차 수치 적분
    :param f:
    :param xi:
    :param xe:
    :param n:
    :param b_verbose:
    :return:
    """
    # 초기화 시작
    if b_verbose:
        print "n =", n
        print "n%2 =", n % 2

    if (n % 2):
        n += 1

    delta_x = (float(xe) - float(xi)) / n
    xk = xi
    fxk = f(xk)

    result = 0.0


    # 초기화 끝

    for k in xrange(0, n, 2):
        xk1 = xk + delta_x
        fxk1 = f(xk1)

        xk2 = xk1 + delta_x
        fxk2 = f(xk2)

        area_k = (fxk + 4 * fxk1 + fxk2) * (delta_x / 3.0)
        result += area_k
        xk = xk2
        fxk = fxk2

    return result

# 적분 될 함수
def f(x):
    return exp(x)

# 적분이 된 함수
def g(x):
    return exp(x)

# main() 함수를 정함
def main():
    """
    위 0, 1, 2 차 함수의 적분
    :return:
    """
    help(rect0)
    # 적분 구간 시작점
    x_begin = 0.0
    # 적분 구간 끝나는 점
    x_end = 1.0
    # 적분 구간을 몇개의 구획으로 나눌 것인가
    n_interval = 8

    # 이론적 엄밀해
    exact = (g(x_end) - g(x_begin))
    print "exact solution = ", exact

    # 함수 ect0 을 호출하여 수치 적분을 계산
    integration_0 = rect0(f, x_begin, x_end, n_interval)
    print "integration_0 = ", integration_0, "err =", integration_0 -exact

    # 함수 trapezoid1 을 호출하여 수치 적분을 계산
    integration_1 = trapezoid1(f, x_begin, x_end, n_interval)
    print "integration_1 = ", integration_1, "err =", integration_1 - exact

    # 함수 simpson2 를 호출하여 수치 적분을 계산
    integration_2 = simpson2(f, x_begin, x_end, n_interval)
    print "integration_2 = ", integration_2, "err =", integration_2 - exact

    # 적분결과를 그림으로 표시하기 위하여 pylab 불로옴
    from pylab import fill, bar, show, xlim, ylim, grid

    # 엄밀해 그림 시작
    n_plot = 100
    delta_x_plot = (float(x_end) - x_begin) / n_plot
    x = [x_begin + k * delta_x_plot for k in xrange(n_plot)]
    y = [f(x[k]) for k in xrange(n_plot)]
    x += [x_end, x_end, x_begin]
    y += [f(x_end), 0.0, 0.0]

    fill(x, y)
    # 엄밀해 그림 끝
    n_plot = n_interval
    delta_x_plot = (float(x_end) - x_begin) / n_plot
    x = [x_begin + k * delta_x_plot for k in xrange(n_plot)]
    y = [f(xk + 0.5 * delta_x_plot) for xk in x]
    x += [x_end]
    y += [0]

    bar(x, y, width = delta_x_plot, color= 'g', alpha = 0.3)
    # 0차 적분 그림 끝

    # 1차 적분 그림 시작
    n_plot = n_interval
    delta_x_plot = (float(x_end) - x_begin) / n_plot
    x = [x_begin + k * delta_x_plot for k in xrange(n_plot)]
    y = [f(xk) for xk in x]
    x += [x_end, x_end, x_begin]
    y += [f(x_end), 0.0, 0.0]

    fill(x, y, color='r', alpha=0.2)
    # 1차 적분 그림 끝

    xlim((x_begin, x_end))
    ylim((0.0, ylim()[1]))

    grid()
    show()

if "__main__" == __name__:
    main()



