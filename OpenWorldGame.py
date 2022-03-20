from ursina import *
from ursina.prefabs.first_person_controller import *
app=Ursina()
player=FirstPersonController()
player.position=(-10, 0, -35)
player.speed=30
player.gravity=0
plane=Entity(model='plane',scale=(100,0,100),collider='mesh',texture="StreetRoad")
def Voxel(p1,p2,p3):
    e=Entity(model='cube',position=(p1,p2,p3),scale=(1,10,1),texture='grass',collider='cube')
Voxel(4, 0, 17)
Voxel(4, 0, 16)
Voxel(4, 0, 15)
Voxel(4, 0, 14)
Voxel(4, 0, 14)
Voxel(4, 0, 13)
Voxel(4, 0, 12)
Voxel(4, 0, 12)
Voxel(4, 0, 11)
Voxel(4, 0, 10)
Voxel(4, 0, 9)
Voxel(4, 0, 8)
Voxel(4, 0, 7)
Voxel(4, 0, 6)
Voxel(4, 0, 5)
Voxel(3, 0, 5)
Voxel(2, 0, 5)
Voxel(1, 0, 5)
Voxel(0, 0, 5)
Voxel(0, 0, 4)
Voxel(0, 0, 3)
Voxel(0, 0, 3)
Voxel(-1, 0, 3)
Voxel(-2, 0, 3)
Voxel(-2, 0, 2)
Voxel(-2, 0, 1)
Voxel(-2, 0, 1)
Voxel(-3, 0, 1)
Voxel(-4, 0, 1)
Voxel(-4, 0, 0)
Voxel(-5, 0, 0)
Voxel(-6, 0, 0)
Voxel(-6, 0, -1)
Voxel(-7, 0, -1)
Voxel(-8, 0, -1)
Voxel(-7, 0, -2)
Voxel(-8, 0, -2)
Voxel(-9, 0, -2)
Voxel(-10, 0, -2)
Voxel(-11, 0, -2)
Voxel(-12, 0, -1)
Voxel(-13, 0, -1)
Voxel(-14, 0, -1)
Voxel(-15, 0, -1)
Voxel(-16, 0, -1)
Voxel(-17, 0, -1)
Voxel(-18, 0, -1)
Voxel(-19, 0, -1)
Voxel(-20, 0, -1)
Voxel(-21, 0, -1)
Voxel(-22, 0, -1)
Voxel(-23, 0, -1)
Voxel(-24, 0, -1)
Voxel(-24, 0, -1)
Voxel(-25, 0, -1)
Voxel(-26, 0, -1)
Voxel(-27, 0, -1)
Voxel(-28, 0, -1)
Voxel(-29, 0, -1)
Voxel(-30, 0, -1)
Voxel(-30, 0, -2)
Voxel(-31, 0, -2)
Voxel(-32, 0, -3)
Voxel(-33, 0, -4)
Voxel(-33, 0, -5)
Voxel(-33, 0, -6)
Voxel(-33, 0, -7)
Voxel(-34, 0, -7)
Voxel(-34, 0, -8)
Voxel(-35, 0, -8)
Voxel(-35, 0, -9)
Voxel(-35, 0, -10)
Voxel(-35, 0, -10)
Voxel(-35, 0, -11)
Voxel(-35, 0, -12)
Voxel(-35, 0, -12)
Voxel(-35, 0, -13)
Voxel(-35, 0, -14)
Voxel(-35, 0, -15)
Voxel(-35, 0, -16)
Voxel(-35, 0, -17)
Voxel(-35, 0, -18)
Voxel(-35, 0, -19)
Voxel(-35, 0, -20)
Voxel(-34, 0, -21)
Voxel(-34, 0, -22)
Voxel(-34, 0, -23)
Voxel(-34, 0, -24)
Voxel(-33, 0, -24)
Voxel(-33, 0, -25)
Voxel(-32, 0, -26)
Voxel(-32, 0, -27)
Voxel(-31, 0, -27)
Voxel(-31, 0, -28)
Voxel(-30, 0, -28)
Voxel(-29, 0, -28)
Voxel(-28, 0, -28)
Voxel(-27, 0, -29)
Voxel(-26, 0, -29)
Voxel(-26, 0, -29)
Voxel(-25, 0, -29)
Voxel(-24, 0, -29)
Voxel(-23, 0, -29)
Voxel(-22, 0, -29)
Voxel(-21, 0, -29)
Voxel(-20, 0, -29)
Voxel(-19, 0, -29)
Voxel(-18, 0, -29)
Voxel(-17, 0, -29)
Voxel(-16, 0, -29)
Voxel(-15, 0, -29)
Voxel(-14, 0, -29)
Voxel(-13, 0, -29)
Voxel(-12, 0, -29)
Voxel(-11, 0, -29)
Voxel(-10, 0, -29)
Voxel(-9, 0, -29)
Voxel(-8, 0, -29)
Voxel(-7, 0, -29)
Voxel(-6, 0, -29)
Voxel(-5, 0, -29)
Voxel(-4, 0, -29)
Voxel(-3, 0, -29)
Voxel(-2, 0, -29)
Voxel(-1, 0, -29)
Voxel(0, 0, -29)
Voxel(1, 0, -29)
Voxel(2, 0, -29)
Voxel(3, 0, -29)
Voxel(4, 0, -29)
Voxel(4, 0, -28)
Voxel(5, 0, -28)
Voxel(5, 0, -27)
Voxel(6, 0, -27)
Voxel(7, 0, -27)
Voxel(8, 0, -26)
Voxel(9, 0, -25)
Voxel(10, 0, -24)
Voxel(10, 0, -24)
Voxel(10, 0, -23)
Voxel(10, 0, -22)
Voxel(10, 0, -21)
Voxel(11, 0, -20)
Voxel(11, 0, -19)
Voxel(11, 0, -18)
Voxel(11, 0, -17)
Voxel(11, 0, -15)
Voxel(11, 0, -16)
Voxel(11, 0, -14)
Voxel(11, 0, -13)
Voxel(11, 0, -12)
Voxel(11, 0, -11)
Voxel(11, 0, -10)
Voxel(11, 0, -10)
Voxel(11, 0, -9)
Voxel(11, 0, -8)
Voxel(11, 0, -7)
Voxel(11, 0, -6)
Voxel(11, 0, -5)
Voxel(11, 0, -4)
Voxel(12, 0, -3)
Voxel(12, 0, -2)
Voxel(12, 0, -1)
Voxel(13, 0, 0)
Voxel(13, 0, 1)
Voxel(14, 0, 2)
Voxel(15, 0, 2)
Voxel(16, 0, 3)
Voxel(17, 0, 3)
Voxel(18, 0, 3)
Voxel(18, 0, 4)
Voxel(19, 0, 4)
Voxel(20, 0, 4)
Voxel(21, 0, 4)
Voxel(22, 0, 4)
Voxel(23, 0, 4)
Voxel(24, 0, 4)
Voxel(25, 0, 4)
Voxel(26, 0, 4)
Voxel(27, 0, 4)
Voxel(28, 0, 4)
Voxel(28, 0, 4)
Voxel(29, 0, 4)
Voxel(30, 0, 4)
Voxel(30, 0, 5)
Voxel(31, 0, 5)
Voxel(32, 0, 5)
Voxel(32, 0, 6)
Voxel(33, 0, 6)
Voxel(33, 0, 6)
Voxel(33, 0, 7)
Voxel(33, 0, 8)
Voxel(34, -1, 7)
Voxel(34, 0, 8)
Voxel(34, 0, 9)
Voxel(34, 0, 10)
Voxel(34, 0, 11)
Voxel(34, 0, 12)
Voxel(35, 0, 13)
Voxel(35, 0, 14)
Voxel(35, 0, 14)
Voxel(35, 0, 15)
Voxel(35, 0, 17)
Voxel(35, 0, 16)
Voxel(35, 0, 18)
Voxel(35, 0, 19)
Voxel(35, 0, 20)
Voxel(35, 0, 21)
Voxel(35, 0, 22)
Voxel(34, 0, 22)
Voxel(34, 0, 24)
Voxel(34, 0, 23)
Voxel(34, 0, 25)
Voxel(33, 0, 25)
Voxel(33, 0, 26)
Voxel(33, 0, 26)
Voxel(33, 0, 27)
Voxel(31, 0, 28)
Voxel(30, 0, 28)
Voxel(30, 0, 29)
Voxel(29, 0, 29)
Voxel(28, 0, 29)
Voxel(27, 0, 29)
Voxel(29, 0, 30)
Voxel(28, 0, 30)
Voxel(27, 0, 30)
Voxel(26, 0, 30)
Voxel(26, 0, 30)
Voxel(25, 0, 30)
Voxel(32, 0, 27)
Voxel(24, 0, 30)
Voxel(23, 0, 30)
Voxel(22, 0, 30)
Voxel(21, 0, 30)
Voxel(20, 0, 30)
Voxel(20, 0, 30)
Voxel(20, 0, 30)
Voxel(19, 0, 30)
Voxel(18, 0, 30)
Voxel(17, 0, 30)
Voxel(16, 0, 30)
Voxel(16, 0, 30)
Voxel(15, 0, 30)
Voxel(14, 0, 30)
Voxel(13, 0, 30)
Voxel(12, 0, 30)
Voxel(11, 0, 30)
Voxel(10, 0, 30)
Voxel(9, 0, 30)
Voxel(8, 0, 30)
Voxel(8, 0, 29)
Voxel(7, 0, 29)
Voxel(7, 0, 28)
Voxel(6, 0, 27)
Voxel(6, 0, 26)
Voxel(5, 0, 25)
Voxel(5, 0, 24)
Voxel(5, 0, 23)
Voxel(5, 0, 22)
Voxel(5, 0, 21)
Voxel(5, 0, 20)
Voxel(4, 0, 20)
Voxel(4, 0, 19)
Voxel(4, 0, 18)
Voxel(-6, 0, -41)
Voxel(-5, 0, -41)
Voxel(-4, 0, -41)
Voxel(-3, 0, -41)
Voxel(-3, 0, -40)
Voxel(-2, 0, -41)
Voxel(-2, 0, -40)
Voxel(-1, 0, -40)
Voxel(0, 0, -40)
Voxel(1, 0, -40)
Voxel(2, 0, -40)
Voxel(2, 0, -41)
Voxel(3, 0, -42)
Voxel(4, 0, -42)
Voxel(5, 0, -43)
Voxel(6, 0, -43)
Voxel(6, 0, -43)
Voxel(7, 0, -43)
Voxel(8, 0, -43)
Voxel(8, 0, -42)
Voxel(9, 0, -42)
Voxel(10, 0, -42)
Voxel(11, 0, -42)
Voxel(12, 0, -42)
Voxel(10, 0, -41)
Voxel(11, 0, -42)
Voxel(11, 0, -41)
Voxel(12, 0, -41)
Voxel(12, 0, -40)
Voxel(13, 0, -39)
Voxel(14, 0, -39)
Voxel(14, 0, -38)
Voxel(14, 0, -37)
Voxel(15, 0, -37)
Voxel(15, 0, -36)
Voxel(16, 0, -36)
Voxel(16, 0, -35)
Voxel(17, 0, -34)
Voxel(17, 0, -33)
Voxel(18, 0, -32)
Voxel(18, 0, -31)
Voxel(19, 0, -31)
Voxel(19, 0, -30)
Voxel(19, 0, -29)
Voxel(19, 0, -28)
Voxel(19, 0, -27)
Voxel(19, 0, -26)
Voxel(20, 0, -26)
Voxel(20, 0, -25)
Voxel(20, 0, -24)
Voxel(20, 0, -23)
Voxel(20, 0, -22)
Voxel(20, 0, -22)
Voxel(20, 0, -21)
Voxel(19, 0, -21)
Voxel(19, 0, -20)
Voxel(19, 0, -19)
Voxel(19, 0, -18)
Voxel(19, 0, -17)
Voxel(19, 0, -16)
Voxel(19, 0, -16)
Voxel(19, 0, -15)
Voxel(19, 0, -14)
Voxel(19, 0, -13)
Voxel(19, 0, -12)
Voxel(20, 0, -11)
Voxel(20, 0, -10)
Voxel(21, 0, -10)
Voxel(21, 0, -10)
Voxel(21, 0, -9)
Voxel(22, 0, -9)
Voxel(22, 0, -8)
Voxel(23, 0, -8)
Voxel(24, 0, -8)
Voxel(25, 0, -8)
Voxel(25, 0, -9)
Voxel(26, 0, -9)
Voxel(26, 0, -10)
Voxel(27, 0, -10)
Voxel(28, 0, -10)
Voxel(28, 0, -10)
Voxel(29, 0, -10)
Voxel(30, 0, -10)
Voxel(30, 0, -10)
Voxel(31, 0, -10)
Voxel(31, 0, -9)
Voxel(32, 0, -9)
Voxel(33, 0, -9)
Voxel(33, 0, -8)
Voxel(34, 0, -8)
Voxel(34, 0, -7)
Voxel(35, 0, -7)
Voxel(36, 0, -7)
Voxel(37, 0, -7)
Voxel(37, 0, -6)
Voxel(38, 0, -6)
Voxel(38, 0, -5)
Voxel(38, 0, -4)
Voxel(39, 0, -4)
Voxel(40, 0, -4)
Voxel(40, 0, -3)
Voxel(40, 0, -2)
Voxel(41, 0, -2)
Voxel(41, 0, -1)
Voxel(42, 0, -1)
Voxel(42, 0, 0)
Voxel(42, 0, 1)
Voxel(42, 0, 2)
Voxel(42, 0, 3)
Voxel(42, 0, 4)
Voxel(42, 0, 5)
Voxel(42, 0, 6)
Voxel(42, 0, 6)
Voxel(42, 0, 7)
Voxel(42, 0, 8)
Voxel(42, 0, 9)
Voxel(42, 0, 10)
Voxel(42, 0, 11)
Voxel(42, 0, 12)
Voxel(42, 0, 13)
Voxel(42, 0, 14)
Voxel(42, 0, 14)
Voxel(42, 0, 15)
Voxel(42, 0, 16)
Voxel(42, 0, 16)
Voxel(42, 0, 17)
Voxel(42, 0, 18)
Voxel(42, 1, 18)
Voxel(42, 1, 18)
Voxel(42, 1, 18)
Voxel(42, 1, 18)
Voxel(42, 0, 19)
Voxel(42, 0, 20)
Voxel(42, 0, 21)
Voxel(42, 0, 22)
Voxel(42, 0, 23)
Voxel(42, 0, 24)
Voxel(42, 0, 24)
Voxel(42, 0, 25)
Voxel(42, 0, 26)
Voxel(42, 0, 27)
Voxel(42, 0, 28)
Voxel(42, 0, 29)
Voxel(42, 0, 30)
Voxel(42, 0, 30)
Voxel(42, 0, 31)
Voxel(42, 0, 32)
Voxel(42, 0, 33)
Voxel(42, 0, 34)
Voxel(42, 0, 34)
Voxel(42, 0, 34)
Voxel(42, 0, 34)
Voxel(42, -1, 34)
Voxel(42, -1, 34)
Voxel(42, -1, 34)
Voxel(42, -1, 34)
Voxel(42, -1, 34)
Voxel(42, -1, 34)
Voxel(42, -1, 34)
Voxel(42, 0, 34)
Voxel(41, 0, 35)
Voxel(41, 0, 36)
Voxel(41, 0, 37)
Voxel(40, 0, 37)
Voxel(40, 0, 38)
Voxel(39, 0, 38)
Voxel(39, 0, 39)
Voxel(38, 0, 39)
Voxel(38, 0, 40)
Voxel(37, 0, 40)
Voxel(37, 0, 41)
Voxel(36, 0, 41)
Voxel(36, 0, 42)
Voxel(35, 0, 42)
Voxel(34, 0, 43)
Voxel(34, 0, 43)
Voxel(34, 0, 43)
Voxel(33, 0, 43)
Voxel(33, 0, 44)
Voxel(32, 0, 44)
Voxel(31, 0, 44)
Voxel(30, 0, 44)
Voxel(29, 0, 44)
Voxel(28, 0, 44)
Voxel(28, 0, 45)
Voxel(27, 0, 45)
Voxel(26, 0, 45)
Voxel(25, 0, 45)
Voxel(25, 0, 44)
Voxel(25, 0, 43)
Voxel(25, 0, 42)
Voxel(24, 0, 42)
Voxel(24, 0, 42)
Voxel(23, 0, 42)
Voxel(22, 0, 42)
Voxel(21, 0, 42)
Voxel(20, 0, 42)
Voxel(19, 0, 42)
Voxel(18, 0, 42)
Voxel(17, 0, 42)
Voxel(16, 0, 42)
Voxel(15, 0, 42)
Voxel(14, 0, 42)
Voxel(13, 0, 42)
Voxel(13, 0, 43)
Voxel(12, 0, 43)
Voxel(12, 0, 44)
Voxel(11, 0, 44)
Voxel(10, 0, 44)
Voxel(9, 0, 44)
Voxel(8, 0, 44)
Voxel(7, 0, 44)
Voxel(6, 0, 44)
Voxel(6, 0, 43)
Voxel(5, 0, 43)
Voxel(4, 0, 43)
Voxel(4, 0, 42)
Voxel(3, 0, 42)
Voxel(3, 0, 41)
Voxel(2, 0, 41)
Voxel(2, 0, 40)
Voxel(1, 0, 40)
Voxel(1, 0, 39)
Voxel(0, 0, 39)
Voxel(0, 0, 38)
Voxel(0, 0, 38)
Voxel(-1, 0, 38)
Voxel(-1, 0, 37)
Voxel(-1, 0, 36)
Voxel(-2, 0, 36)
Voxel(-2, 0, 35)
Voxel(-3, 0, 35)
Voxel(-3, 0, 34)
Voxel(-3, 0, 33)
Voxel(-3, 0, 32)
Voxel(-4, 0, 32)
Voxel(-4, 0, 31)
Voxel(-4, 0, 30)
Voxel(-5, 0, 30)
Voxel(-5, 0, 29)
Voxel(-5, 0, 28)
Voxel(-5, 0, 28)
Voxel(-5, 0, 27)
Voxel(-5, 0, 26)
Voxel(-5, 0, 25)
Voxel(-5, 0, 24)
Voxel(-5, 0, 23)
Voxel(-5, 0, 22)
Voxel(-4, 0, 22)
Voxel(-4, 0, 21)
Voxel(-4, 0, 20)
Voxel(-4, 0, 19)
Voxel(-4, 0, 18)
Voxel(-5, 0, 18)
Voxel(-5, 0, 17)
Voxel(-6, 0, 17)
Voxel(-6, 0, 16)
Voxel(-7, 0, 15)
Voxel(-7, 0, 14)
Voxel(-8, 0, 14)
Voxel(-8, 0, 13)
Voxel(-9, 0, 13)
Voxel(-10, 0, 13)
Voxel(-10, 0, 12)
Voxel(-11, 0, 12)
Voxel(-12, 0, 12)
Voxel(-13, 0, 12)
Voxel(-14, 0, 12)
Voxel(-15, 0, 12)
Voxel(-16, 0, 12)
Voxel(-17, 0, 12)
Voxel(-18, 0, 12)
Voxel(-19, 0, 12)
Voxel(-20, 0, 12)
Voxel(-21, 0, 12)
Voxel(-22, 0, 12)
Voxel(-22, 0, 13)
Voxel(-23, 0, 13)
Voxel(-24, 0, 13)
Voxel(-24, 0, 14)
Voxel(-25, 0, 14)
Voxel(-26, 0, 14)
Voxel(-27, 0, 14)
Voxel(-28, 0, 14)
Voxel(-29, 0, 14)
Voxel(-30, 0, 14)
Voxel(-31, 0, 14)
Voxel(-31, 0, 13)
Voxel(-32, 0, 13)
Voxel(-32, 0, 12)
Voxel(-33, 0, 12)
Voxel(-33, 0, 12)
Voxel(-33, 0, 11)
Voxel(-34, 0, 11)
Voxel(-35, 0, 11)
Voxel(-35, 0, 10)
Voxel(-36, 0, 10)
Voxel(-37, 0, 10)
Voxel(-37, 0, 9)
Voxel(-38, 0, 9)
Voxel(-38, 0, 8)
Voxel(-39, 0, 7)
Voxel(-39, 0, 6)
Voxel(-40, 0, 6)
Voxel(-40, 0, 5)
Voxel(-41, 0, 5)
Voxel(-41, 0, 4)
Voxel(-41, 0, 3)
Voxel(-42, 0, 3)
Voxel(-42, 0, 2)
Voxel(-42, 0, 2)
Voxel(-42, 0, 1)
Voxel(-43, 0, 1)
Voxel(-43, 0, 0)
Voxel(-44, 0, 0)
Voxel(-44, 0, -1)
Voxel(-44, 0, -2)
Voxel(-44, 0, -3)
Voxel(-44, 0, -4)
Voxel(-44, 0, -5)
Voxel(-45, 0, -5)
Voxel(-45, 0, -6)
Voxel(-45, 0, -7)
Voxel(-45, 0, -8)
Voxel(-45, 0, -9)
Voxel(-45, 0, -10)
Voxel(-45, 0, -10)
Voxel(-45, 0, -11)
Voxel(-45, 0, -12)
Voxel(-45, 0, -13)
Voxel(-45, 0, -14)
Voxel(-45, 0, -15)
Voxel(-45, 0, -16)
Voxel(-45, 0, -17)
Voxel(-45, 0, -18)
Voxel(-45, 0, -19)
Voxel(-45, 0, -20)
Voxel(-45, 0, -20)
Voxel(-45, 0, -21)
Voxel(-45, 0, -22)
Voxel(-45, 0, -23)
Voxel(-45, 0, -24)
Voxel(-45, 0, -25)
Voxel(-44, 0, -25)
Voxel(-44, 0, -26)
Voxel(-44, 0, -27)
Voxel(-43, 0, -27)
Voxel(-43, 0, -28)
Voxel(-43, 0, -28)
Voxel(-42, 0, -28)
Voxel(-42, 0, -29)
Voxel(-42, 0, -30)
Voxel(-42, 0, -31)
Voxel(-42, 0, -32)
Voxel(-42, 0, -32)
Voxel(-42, 0, -32)
Voxel(-42, 0, -32)
Voxel(-41, 0, -32)
Voxel(-41, 0, -32)
Voxel(-41, 0, -32)
Voxel(-41, 0, -32)
Voxel(-41, 0, -32)
Voxel(-41, 0, -32)
Voxel(-41, 0, -32)
Voxel(-41, 0, -32)
Voxel(-41, 0, -32)
Voxel(-41, 0, -32)
Voxel(-41, 0, -32)
Voxel(-41, 0, -33)
Voxel(-41, 0, -34)
Voxel(-40, 0, -34)
Voxel(-40, 0, -35)
Voxel(-39, 0, -35)
Voxel(-39, 0, -36)
Voxel(-39, 0, -37)
Voxel(-39, 0, -38)
Voxel(-38, 0, -38)
Voxel(-38, 0, -39)
Voxel(-37, 0, -39)
Voxel(-37, 0, -40)
Voxel(-36, 0, -40)
Voxel(-36, 0, -41)
Voxel(-35, 0, -41)
Voxel(-34, 0, -41)
Voxel(-34, 0, -42)
Voxel(-33, 0, -42)
Voxel(-33, 0, -43)
Voxel(-32, 0, -43)
Voxel(-31, 0, -43)
Voxel(-30, 0, -43)
Voxel(-29, 0, -43)
Voxel(-28, 0, -43)
Voxel(-27, 0, -43)
Voxel(-26, 0, -43)
Voxel(-25, 0, -43)
Voxel(-24, 0, -43)
Voxel(-23, 0, -42)
Voxel(-22, 0, -41)
Voxel(-21, 0, -41)
Voxel(-20, 0, -41)
Voxel(-20, 0, -41)
Voxel(-18, 0, -41)
Voxel(-19, 0, -41)
Voxel(-17, 0, -41)
Voxel(-16, 0, -41)
Voxel(-15, 0, -41)
Voxel(-7, 0, -41)
Voxel(-8, 0, -41)
Voxel(-9, 0, -41)
Voxel(-10, 0, -41)
Voxel(-11, 0, -41)
Voxel(-12, 0, -41)
Voxel(-12, 0, -40)
Voxel(-13, 0, -41)
Voxel(-13, 0, -40)
Voxel(-14, 0, -41)
#mountains=Entity(model='mountains.obj', texture='mountain.png', collider='mesh')
def YouWon():
    Text('You won!',x=-.5,background=True)
def update():
    if held_keys["w"] or held_keys["s"] or held_keys["a"] or held_keys["d"]:
        Audio("Racecar.wav")
Entity(model='cube',position=(-7,0,-35),scale=(1,10,11),texture='grass',collider='cube')
Entity(model='cube',position=(-4,0,-35),scale=(0.5,5,0.5),texture='grass',color=color.black,collider='cube',on_click=YouWon)
Entity(model='sphere',position=(-4,2.5,-35),scale=(0.5,0.5,0.5),texture='grass',color=color.red,collider='cube',on_click=YouWon)
app.run()