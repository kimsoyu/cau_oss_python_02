"""
클래스 Line : 선분을 나타내는 클래스입니다.
함수 area_square : 길이를 입력받아 정사각형의 넓이를 구하는 함수입니다.
함수 area_circle : 길이를 입력받아 원의 넓이를 구하는 함수입니다.
함수 area_regular_triangle : 길이를 입력받아 정삼각형의 넓이를 구하는 함수입니다.
"""

import math

class Line:
    """선분을 나타내는 클래스입니다.
    Attributes:
        __length (int or float): 선분의 길이입니다.
    Methods:
        __init__(length=1): Line 객체를 생성하는 생성자입니다.
        set_length(length): 길이 값을 설정하는 함수입니다.
        get_length(): 길이 값을 반환하는 함수입니다.
    """
    def __init__(self, length=1):
        """Line 객체를 생성하는 생성자입니다.
        Args:
            length (int or float): 길이 값입니다. (반드시 0 보다 큰 값이어야 하며, 타입/범위를 위반하거나 미입력시 기본값은 1)
        """
        if type(length) in (int, float) and length > 0:
            self.__length = length
        else:
            self.__length = 1
    
    def set_length(self, length):
        """길이 값을 설정하는 함수입니다.
        Args:
            length (int or float): 새롭게 설정할 길이 값입니다. (반드시 0 보다 큰 값이어야 하며, 타입/범위를 위반할시 이전 값 유지)
        """
        if type(length) in (int, float) and length > 0:
            self.__length = length

    def get_length(self):
        """길이 값을 반환하는 함수입니다.
        Returns:
            int or float: 길이 값을 반환합니다.
        """
        return self.__length

def area_square(line):
    """길이를 입력받아 정사각형의 넓이를 구하는 함수입니다.
    Args:
        line (Line): 한 변의 길이입니다.
    Returns:
        int or float: 정사각형의 넓이를 반환합니다. (매개변수의 타입이 Line 클래스가 아닌 경우, 0 을 반환)
    """
    if type(line) == Line:
        return line.get_length() ** 2
    else:
        return 0

def area_circle(line):
    """길이를 입력받아 원의 넓이를 구하는 함수입니다.
    Args:
        line (Line): 반지름의 길이입니다.
    Returns:
        int or float: 원의 넓이를 반환합니다. (매개변수의 타입이 Line 클래스가 아닌 경우, 0 을 반환)
    """
    if type(line) == Line:
        return line.get_length() ** 2 * math.pi
    else:
        return 0

def area_regular_triangle(line):
    """길이를 입력받아 정삼각형의 넓이를 구하는 함수입니다.
    Args:
        line (Line): 한 변의 길이입니다.
    Returns:
        int or float: 정삼각형의 넓이를 반환합니다. (매개변수의 타입이 Line 클래스가 아닌 경우, 0 을 반환)
    """
    if type(line) == Line:
        return line.get_length() ** 2 * math.sqrt(3) / 4
    else:
        return 0
    