# -*- coding: utf8 -*-
# 2010112033 이상형 9/20
"""
1변수 방정식의 근을 찾느 방법 중 Newton-Raphson method 를 사용하여
어떤 함수 g(x) 의 근을 찾고자 함
아래 예는 newton_raphson method 를 사용하기 곤란한 경우임
"""

# 1 변수 방정식의 근을 찾는 함수를 모아둔 rootfinding 모듈을 불러들임
# 값을 못찾는 경우의 프로그래밍의 예이다. 이를 해결하는 방법은 초기값을 바꿔주면 된다.

import rootfinding as rf

def g(x):
    # 근을 구하고자 하는 함수
    return x ** 3 - 2 * x + 2

def dgdx(x):
    # g(x) 의 x 에 대한 미분
    return 3.0 * x ** 2.0 - 2.0

if "__main__" == __name__:
    # 주어진 초기값에서 시작하여 g(x) = 0 인 x를 찾고자 함
    # 생각보다 시간이 많이 걸릴 수 있음
    x_nr = rf.newton(g, dgdx, 0)
    print('x = %g, f(%g) = %g' % (x_nr, x_nr, g(x_nr)))