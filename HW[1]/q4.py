import cv2


if __name__ == '__main__':
    img = cv2.imread('background.png', cv2.IMREAD_COLOR)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = cv2.resize(img, (570, 290))

    img = cv2.line(img, (5, 5), (565, 5), (0, 255, 255))
    img = cv2.line(img, (5, 5), (5, 285), (0, 255, 255))
    img = cv2.line(img, (5, 285), (565, 285), (0, 255, 255))
    img = cv2.line(img, (565, 5), (565, 285), (0, 255, 255))

    rectangle_nodes = [(5, 5), (565, 5), (5, 285), (565, 285)]
    for node in rectangle_nodes:
        img = cv2.circle(img, node, 4, (255, 0, 0))

    y = int((285-5)/2 + 5)
    temp = (565-5)/7
    xs = [int(5 + i*temp) for i in range(8)]
    for node in rectangle_nodes:
        for x in xs:
            img = cv2.line(img, node, (x, y), (0, 0, 0))

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow('', img)
    cv2.waitKey()

    cv2.imwrite('mypic.jpg', img)
