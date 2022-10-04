def Flip(image1, image2):
    img = graphics.Image(graphics.Point(0, 0), image1)
    X = img.getWidth()
    Y = img.getHeight()
    for y in range(Y):
        for x in range(X):
            A = img.getPixel(x,y)
            r = A[0]
            g = A[1]
            b = A[2]
            color = graphics.color_rgb(r,g,b)
            img.setPixel(X-x,y,color)
    img = graphics.Image(graphics.Point(0,0), image2)
    win = graphics.GraphWin(image2, img.getWidth(), img.getHeight())
    img.draw(win)
