BIRD_SCALE = 0.45


class Bird:
    def __init__(self, image, x, y):
        self.image = image
        self.x, self.y = x, y

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 342, 182, 164, self.x, self.y,
                             round(182 * BIRD_SCALE), round(164 * BIRD_SCALE))
