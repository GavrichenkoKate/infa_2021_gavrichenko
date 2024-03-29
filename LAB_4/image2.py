import pygame
from math import pi, cos, sin, radians
from pygame.draw import rect, ellipse, arc, polygon

pygame.init()

pandaColorLight = "WHITE"
pandaColorDark = "BlACK"
screenColor = "#FFAF79"
plantColor = "#00FF00"
plantColor = "DARKGREEN"

countEarCords = 1000

rEarLeft = 80
arcEarLeft = 200
leftEarAngle = 110

rEarRight = 80
arcEarRight = -220
rightEarAngle = 110

aNose = 65
bNose = 45
aLeftEye = 45
bLeftEye = 60
aRightEye = 60
bRightEye = 60

pandaX = 900
pandaY = 350
palmaX1 = 650
palmaY1 = 400
palmaX2 = 300
palmaY2 = 470
kPalma1 = 1.5
kPalma2 = 1.1

podgonX1 = 140
podgonY1 = 330
podgonX2 = 0
podgonY2 = 300
podgonX3 = -10
podgonY3 = 335
podgonXface = -140
podgonYface = 60
podgonXhead = 100
podgonYhead = 100
podgonXLeftEar = -115
podgonYLeftEar = -90
podgonXRightEar = 100
podgonYRightEar = -80
podgonXNose = -90
podgonYNose = 0
podgonXLeftEye = -110
podgonYLeftEye = -70
podgonXRightEye = -40
podgonYRightEye = -60

unitLength = 10
kAbody = 40
kBbody = 20

deltaXpaw1 = unitLength * 5
deltaXpaw2 = unitLength * 0
deltaXpaw3 = unitLength * (-5)
deltaYpaw1 = unitLength * 5
deltaYpaw2 = unitLength * 10
deltaYpaw3 = unitLength * 0

deltaX1 = 40
deltaY1 = 60

kPaw1 = 2
kPaw2 = 1.2
kPaw3 = 2
kFace = 1.9

FPS = 60
screen = pygame.display.set_mode((1400, 750))
screen.fill(screenColor)


def drawEarLeft(x, y):
    leftEarCords = [0] * countEarCords
    kEllipseMosiv = [(2 * sin((i / (countEarCords)))) / 2 for i in range(countEarCords)]
    angleEarLeftMosiv = [((arcEarLeft / countEarCords) * i + leftEarAngle) for i in range(countEarCords)]
    for i in range(countEarCords):
        leftEarCords[i] = [x + round(rEarLeft * cos(radians(angleEarLeftMosiv[i])) * kEllipseMosiv[i]),
                           y + round(rEarLeft * sin(radians(angleEarLeftMosiv[i])) * kEllipseMosiv[i])]
    polygon(screen, pandaColorDark, leftEarCords)


def drawEarRight(x, y):
    rightEarCords = [0] * countEarCords
    kEllipseMosiv = [(2 * sin((i / (countEarCords)))) / 2 for i in range(countEarCords)]
    angleEarRightMosiv = [((arcEarRight / countEarCords) * i + rightEarAngle) for i in range(countEarCords)]
    for i in range(countEarCords):
        rightEarCords[i] = [x + round(rEarRight * cos(radians(angleEarRightMosiv[i])) * kEllipseMosiv[i]),
                            y + round(rEarRight * sin(radians(angleEarRightMosiv[i])) * kEllipseMosiv[i])]
    polygon(screen, pandaColorDark, rightEarCords)


def drawface(x, y):
    imageFace = pygame.image.load('pngs/face.png')
    sizeFace = imageFace.get_size()
    sizeFace = list(sizeFace)
    sizeFace = round((sizeFace[0]) / kFace), round((sizeFace[1]) / kFace)
    imageFace = pygame.transform.scale(imageFace, sizeFace)
    rectFace = imageFace.get_rect(bottomleft=(x + podgonXface, y + podgonYface))
    screen.blit(imageFace, rectFace)


def drawnose(x, y):
    x, y = x + podgonXNose, y + podgonYNose
    ellipse(screen, pandaColorDark, (x, y, aNose, bNose))


def draweyes(x, y):
    drawlefteye(x, y)
    drawrighteye(x, y)


def drawlefteye(x, y):
    x, y = x + podgonXLeftEye, y + podgonYLeftEye
    ellipse(screen, pandaColorDark, (x, y, aLeftEye, bLeftEye))


def drawrighteye(x, y):
    x, y = x + podgonXRightEye, y + podgonYRightEye
    ellipse(screen, pandaColorDark, (x, y, aRightEye, bRightEye))


def drawears(x, y):
    xLeft = x + podgonXLeftEar
    yLeft = y + podgonYLeftEar
    xRight = x + podgonXRightEar
    yRight = y + podgonYRightEar
    drawEarLeft(xLeft, yLeft)
    drawEarRight(xRight, yRight)


def drawhead(pandaX, pandaY):
    x, y = pandaX + podgonXhead, pandaY + podgonYhead
    drawface(x, y)
    drawnose(x, y)
    draweyes(x, y)
    drawears(x, y)


def drawpandabody(x, y):
    a = kAbody * unitLength
    b = kBbody * unitLength
    color = pandaColorLight
    ellipse(screen, color, (x, y, a, b))


def drawpandapaw1(x, y):
    imagePaw1 = pygame.image.load('pngs/paw1.png')
    sizePaw1 = imagePaw1.get_size()
    sizePaw1 = list(sizePaw1)
    sizePaw1 = round((sizePaw1[0]) / kPaw1), round((sizePaw1[1]) / kPaw1)
    imagePaw1 = pygame.transform.scale(imagePaw1, sizePaw1)
    rectPaw1 = imagePaw1.get_rect(bottomleft=(x + podgonX1, y + podgonY1))
    screen.blit(imagePaw1, rectPaw1)


def drawpandapaw2(x, y):
    imagePaw2 = pygame.image.load('pngs/paw2.png')
    sizePaw2 = imagePaw2.get_size()
    sizePaw2 = list(sizePaw2)
    sizePaw2 = round((sizePaw2[0]) / kPaw2), round((sizePaw2[1]) / kPaw2)
    imagePaw2 = pygame.transform.scale(imagePaw2, sizePaw2)
    rectPaw2 = imagePaw2.get_rect(bottomleft=(x + podgonX2, y + podgonY2))
    screen.blit(imagePaw2, rectPaw2)


def drawpandapaw3(x, y):
    imagePaw3 = pygame.image.load('pngs/paw3.png')
    sizePaw3 = imagePaw3.get_size()
    sizePaw3 = list(sizePaw3)
    sizePaw3 = round((sizePaw3[0]) / kPaw2), round((sizePaw3[1]) / kPaw2)
    imagePaw3 = pygame.transform.scale(imagePaw3, sizePaw3)
    rectPaw3 = imagePaw3.get_rect(bottomleft=(x + podgonX3, y + podgonY3))
    screen.blit(imagePaw3, rectPaw3)


def drawpandapaws(pandaX, pandaY):
    drawpandapaw1(pandaX + deltaXpaw1, pandaY + deltaYpaw1)
    drawpandapaw2(pandaX + deltaXpaw2, pandaY + deltaYpaw2)
    drawpandapaw3(pandaX + deltaXpaw3, pandaY + deltaYpaw3)


def drawpanda(pandaX, pandaY):
    drawpandabody(pandaX, pandaY)
    drawpandapaws(pandaX, pandaY)
    drawhead(pandaX, pandaY)


def drawtrunk(x, y, kPalma):
    uL = kPalma  # unitLength
    rect(screen, plantColor, (x, y, 20 * uL, 80 * uL))
    rect(screen, plantColor, (x + 3 * uL, y - 85 * uL, 15 * uL, 80 * uL))
    polygon(screen, plantColor, ([x + 6 * uL, y - 92 * uL],
                                 [x + 12 * uL, y - 90 * uL],
                                 [x + 30 * uL, y - 170 * uL],
                                 [x + 24 * uL, y - 172 * uL]))
    polygon(screen, plantColor, ([x + 26 * uL, y - 178 * uL],
                                 [x + 30 * uL, y - 176 * uL],
                                 [x + 66 * uL, y - 250 * uL],
                                 [x + 62 * uL, y - 252 * uL]))


def drawrotateleaf(color, x, y, kPalma, rotateAngle):
    leafCords = [0] * 400
    angleLeafMosiv = [((360 / 400) * i + 60) for i in range(400)]
    for i in range(400):
        leafCords[i] = [round(x + 20 * cos(radians(angleLeafMosiv[i])) * kPalma),
                        round(y + 30 * sin(radians(angleLeafMosiv[i] + rotateAngle)) * kPalma)]
    polygon(screen, color, leafCords)


def drawleaves(x, y, kPalma):
    uL = kPalma

    drawrotateleaf("DARKGREEN", x + 200 * uL, y - 215 * uL, uL, 110)
    drawrotateleaf("DARKGREEN", x + 180 * uL, y - 215 * uL, uL, 110)
    drawrotateleaf("DARKGREEN", x + 160 * uL, y - 213 * uL, uL, 110)
    drawrotateleaf("DARKGREEN", x + 140 * uL, y - 208 * uL, uL, 110)
    drawrotateleaf("DARKGREEN", x + 120 * uL, y - 200 * uL, uL, 110)

    drawrotateleaf("DARKGREEN", x - 150 * uL, y - 185 * uL, uL, -110)
    drawrotateleaf("DARKGREEN", x - 130 * uL, y - 185 * uL, uL, -110)
    drawrotateleaf("DARKGREEN", x - 110 * uL, y - 182 * uL, uL, -110)
    drawrotateleaf("DARKGREEN", x - 90 * uL, y - 179 * uL, uL, -110)
    drawrotateleaf("DARKGREEN", x - 70 * uL, y - 173 * uL, uL, -110)

    drawrotateleaf("DARKGREEN", x + 135 * uL, y - 100 * uL, uL * 0.8, 110)
    drawrotateleaf("DARKGREEN", x + 120 * uL, y - 100 * uL, uL * 0.8, 110)
    drawrotateleaf("DARKGREEN", x + 105 * uL, y - 98 * uL, uL * 0.8, 110)
    drawrotateleaf("DARKGREEN", x + 90 * uL, y - 93 * uL, uL * 0.8, 110)
    drawrotateleaf("DARKGREEN", x + 75 * uL, y - 85 * uL, uL * 0.8, 110)

    drawrotateleaf("DARKGREEN", x - 115 * uL, y - 70 * uL, uL * 0.8, -110)
    drawrotateleaf("DARKGREEN", x - 100 * uL, y - 70 * uL, uL * 0.8, -110)
    drawrotateleaf("DARKGREEN", x - 85 * uL, y - 67 * uL, uL * 0.8, -110)
    drawrotateleaf("DARKGREEN", x - 71 * uL, y - 61 * uL, uL * 0.8, -110)
    drawrotateleaf("DARKGREEN", x - 59 * uL, y - 53 * uL, uL * 0.8, -110)


def drawbranches(x, y, kPalma):
    uL = kPalma  # unitLength
    arc(screen, plantColor, (x + 15 * uL, y - 130 * uL, 200 * uL, 200 * uL), pi / 3, 7 * pi / 8, width=4)
    arc(screen, plantColor, (x + 30 * uL, y - 250 * uL, 300 * uL, 200 * uL), pi / 3, 7 * pi / 8, width=4)
    arc(screen, plantColor, (x - 195 * uL, y - 100 * uL, 200 * uL, 200 * uL), pi / 8, 2 * pi / 3, width=4)
    arc(screen, plantColor, (x - 270 * uL, y - 220 * uL, 300 * uL, 200 * uL), pi / 8, 2 * pi / 3, width=4)
    drawleaves(x, y, kPalma)


def drawpalma(x, y, kPalma):
    drawbranches(x, y, kPalma)
    drawtrunk(x, y, kPalma)


drawpanda(pandaX, pandaY)
drawpalma(palmaX1, palmaY1, kPalma1)
drawpalma(palmaX2, palmaY2, kPalma2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()