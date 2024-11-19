import numpy


def graph_histogram(highlight, image: numpy.ndarray) -> list:
    """Graphic of count pixels and steps of highlights"""
    height, width, channels = image.shape
    counter = []
    for i in highlight:
        count = 0
        for yvalue in range(0, height):
            for xvalue in range(0, width):
                rgbsum = 0
                for elem in image[yvalue, xvalue]:
                    rgbsum+=int(elem)
                if rgbsum == int(i*3):
                    count += 1
        counter.append(count)
    return counter