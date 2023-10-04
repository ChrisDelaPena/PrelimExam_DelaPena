import math

    
def test_check():
#check grades if passed (greater than or equal to 50)
    grade=75
    assert grade>=50
    
def test_fun():
# celcius + kelvin = fahrenheit (Lets say kelvin=150 for example)
#this formula is an assumption only to show if the conversion is correct
    cel=10
    k=150
    far=160
    assert cel+k == far
    
def test_square():#area = side*side
    side=5
    area=25
    assert side*side == area

    
    