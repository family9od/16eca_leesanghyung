# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이 사용되었다는 점을 표시하는 것임
# 2010112033 이상형
"""
1변수 방정식의 해
어떤 (비선형) 함수 f(x) 값이 0이 되도록 만드는 x 를 찾음
"""
# 컴퓨터 메모리에는 원래는 제한된 자릿수의 2진수만 저장할 수 있음
# 실수를 저장하면 오차가 발생하게 됨
# epsilon 은 허용되는 오차범위를 의미함

epsilon_global = 1e-4



def sequential(f, x0, delta_x=1e-6, epsilon=epsilon_global, b_verbose=False):
    """
    sequential method
    x0 로 부터 시작해서 delta_x 만큼씩 증가시키면서 절대값f(x) 값이 epsilon 값 보다 작아지는지 관찰함
    :param
    :param f:  f(x) = 0 인 x를 찾고자하는 함수
    :param x0: x의 초기값
    :param delta_x: x를 한번에 delta_x 만큼씩 증가시킴
    :param epsilon:  오차허용범위
    :param b_verbose: 추가 정보 표시, 정해주지 않으면 false
    :return: 절대값 f(x) <  epsilon 인 x
    """
    # 어떤 형태의 입력값이 들어올지 알 수 없으나
    # xi의 초기값은 (부동소숫점) 실수가 되어야하므로
    # float()를 이용
    xi = float(x0)
    # delta_x의 의미는
    # '아직 답을 찾지 못했을 때 xi 를 얼마만큼 증사기킬 것인가'

    # counter 는 아래 무한 반복문ㅇ르 실행한 횟수
    counter = 0


    # 무한반복문
    while True:
        fi = f(xi)
        # 절대값 f(x) <  epsilon 이며
        if abs(fi) < epsilon:
            # 무한반복문 중단
            break
        # 그렇치 않으면
        # x를 delta_x 만큼 증가시킴
        xi += delta_x
        # 반복문 한번 실행되면 counter 를 1증가시킴킴
        counter += 1

    if b_verbose:
        print "seq_counter =", counter
        # 반복문이 실행된 횟수를 표시

    return xi
    # 반복문에서 찾은 결과를 반환
# end of sequential()



def bisection(f , xl, xh, epsilon=epsilon_global, b_verbose=False):

    """
    bisection method
    f(xl) 과 f(xh)의 부로가 반대인 xl, xh 에서 시작
    xl ~ xh 사이의 구간을 절반 지점인 xn을 찾음
    f(xㅣ)과 f(xn) 의 부호가 반대이면 xh를 xn으로 옮김
        이렇게 하면 계속 f(xl) 과 f(xh)의 부호가 반대임
    그렇지않으면 xl 을 xn 으로 옮김
        f(xn) 과 f(xh) 의 부호가 반대일 것임

    xl ~ xh 사이의 구간의 길이가 epsilon 보다 작아지면 중단

    :param f: f(x)= 0인 x를 찾고자 하는 함수
    :param xl: x의 초기값 xl < xh && f(xl) f(xh) < 0
    :param xh: x의 초기값 xl < xh && f(xl) f(xh) < 0
    :param epsilon: 오차허용범위
    :param b_verbose: 중간 과정 표시, 정해주지 않으면 false
    :return: f(x) == 0 인 x와 가까운 값
    """

    # 어떤 형태의 입력값이 들어올지 알수 없으나
    # xi 의 초기값은 (부동소숫점) 실수가 되어야하므로
    # float()를 이용
    xl = float(xl)
    xh = float(xh)

    # xn 을 초기화한다
    xn = xl

    # counter 는 아래 무한 반복문을 실행한 횟수
    counter = 0

    # 무한 반복문
    while True:
        # xl ~ xh 사이의 가운데 지점을 xn 으로 삼는다
        xn = 0.5 * (xl + xh)

        # f(fn)과 f(xh)의 부호를 비교
        if f(xn) * f(xh) < 0:
            # 다르면 : 근이 xn~xh 사이에 있음, xl에 xn을 저장
            xl = xn
        else:
            # 같으면 : 근이 xn~xh 사이에 있음, xh에 xn을 저장
            xh = xn

        counter += 1

        if b_verbose:
            print "bis_counter = ", counter

        # xn을 반환
        return xn
# end of bisection()



def newton(f, df, x0, epsilon=epsilon_global, b_verbose=False):

    """
    newton Raphson method
    비선형 함수인 f(x)의 xi 지점에서의 접선의 방정실의 근을 구함

    xi 지점에서의 f(x)의 기울기가 di, 함수값이 fi이면
    접선의 방정식 di (x - xi) + fi 는 x = xi - fi/fd 이면 0이됨
    즉, 접선의 방정식의 근은 xi - fi/di 이고 접점 xi 로 부터 (-fi/di) 위치에 있음
    이를 이용하여 i +1 번째 x를 xi - fi/di 로 정함

    f(x) 의 xi 에서의 기울기 di 의 절대값이 0 에 가까울 경우 xi 로 부터 매우 먼 위치에 xi 가 자리하게 됨
    새로운 위치에서 절대값 f(x) 값이 epsilon 값 보다 작어지면 중단
    그렇치 않으면 접선의 방정식의 근을 다시 구함

    :param f: f(x) = 0 을 만족하는 x를 찾고자 하는 함수
    :param df: f(x) 의 미분
    :param x0: x의 초기값
    :param epsilon_global:
    :param b_verbose:
    :return:
    """

    # xi 를 (부동소숫점) 실수로 초기화
    xi = float(x0)

    # counter 는 아래 무한 반복문을 실행한 횟수
    counter = 0

    while True:
        fi = f(xi)

        counter += 1

        if abs(fi) < epsilon:

            break

        else:
            xi += (-fi/df(xi))
    if b_verbose:
        print("nr_counter = %d" % counter)

    return xi
# end of newton



def func(x):
    """
    f(x) = 0 을 만족하는 x 를 찾고자 하는 f()
    이 경우는 x* x- 2.0 =0 을 만족하는 x를 찾게 되며 이러한 x 는 2 ** 0.5 즉 2 의 제곱근임
    :param x:
    :return:
    """
    return 1.0 * x * x - 2.0

# end of func()
# BATzerk, "Square Root Calculator", Scratch, [Online] Available : https://scratch.mit.edu/program

def dfunc(x):
    """
    위 함수 func(x)를 x로 미분한 함수
    :param x:
    :return:
    """

    return 2.0 * x

# end of dfunc()

def main():
    # 순차 대입법 sequential method 로 func() 의 해를 구하기 위해 시도

    x0 = "0.01" # x 의 초기값, 정수인가? 실수인가?
    x_seq = sequential(func, x0, b_verbose=True)
    print "x_seq = ", x_seq
    print "f(x_seq) = ", func(x_seq)

    # 이분법 bisection method 로 func() 의 해를 구하기 위해 시도
    x_bis = bisection(func, 0.01, 2.0, b_verbose=True)
    print "x_bis = ", x_bis
    print "f(x_bis) = ", func(x_bis)

    # 뉴튼-랩슨법 으로 func() 의 해를 구하기 위해 시도
    # 초기값은 얼마인가?
    # 위의 두 방법에서는 필요하지 않았던 매개변수는 어떤 것인가?
    x_nr = newton(func, dfunc, 2.0, b_verbose=True)
    print "x_nr = ", x_nr
    print "f(x_nr) = ", func(x_nr)

    # 세 방법으로 구한 x의 정확도
    print "error    seq       bis     nr"
    print "         %7g %7g %7g" % (abs(2.0 **5.0 - x_seq), abs(2.0 **5.0 - x_bis), abs(2.0 **5.0 - x_nr))

if "__main__" == __name__:
    main()