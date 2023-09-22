
def classify_triangle(a, b, c):
    if not all(isinstance(side, int) for side in [a, b, c]):
        return 'All sides must be integers'
    if not all(side > 0 for side in [a, b, c]):
        return 'All sides must be greater than 0'
    if not (a + b > c and b + c > a and a + c > b):
        return 'Not a triangle'

    a, b, c = sorted([a, b, c])
    isRightTriangle = a ** 2 + b ** 2 == c ** 2
    isEquilateralTriangle = a == b == c
    isIsoscelesTriangle = a == b or b == c

    if isEquilateralTriangle:
        answer = 'Equilateral'
    elif isIsoscelesTriangle:
        answer = 'Isosceles'
    else:
        answer = 'Scalene'

    if isRightTriangle:
        answer += ' and Right'

    return answer + ' Triangle'


if __name__ == '__main__':
    classify_triangle(1, 2, 3)
