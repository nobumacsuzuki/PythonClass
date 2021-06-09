class Cuboid(object):
    def __init__(self, width, height, depth):
        self._width = width
        self._height = height
        self._depth = depth
    @property
    def width(self):
            return self._width
    @width.setter
    def width(self, width):
        self._width = width
    @property
    def height(self):
            return self._height
    @height.setter
    def height(self, height):
        self._height = height
    @property
    def depth(self):
            return self._depth
    @depth.setter
    def depth(self, depth):
        self._depth = depth
    @property
    def volume(self):
        return self._width * self._height * self._depth

def main():
    cuboidExample = Cuboid(5, 4, 6)
    print (cuboidExample.width)
    print (cuboidExample.height)
    print (cuboidExample.depth)
    print (cuboidExample.volume)
    cuboidExample = Cuboid(0, 0, 0)
    cuboidExample.width = 2
    cuboidExample.height = 3
    cuboidExample.depth = 7
    print (cuboidExample.width)
    print (cuboidExample.height)
    print (cuboidExample.depth)
    print (cuboidExample.volume)
    

if __name__ == "__main__":
    main()

    