import game_framework


BIRD_SCALE = 0.45
FLAP_FRAMES_PER_SECOND = 20.0
SHEET_HEIGHT = 506
COLUMNS = (0, 182, 364, 546, 727, 918)
ROWS = ((0, 164, 103, 5), (164, 350, 267, 5), (350, 506, 440, 4))

# 원본의 위쪽 기준 행을 Pico2D의 아래쪽 기준으로 변환한다.
FRAMES = [
    (COLUMNS[column], SHEET_HEIGHT - bottom,
     COLUMNS[column + 1] - COLUMNS[column], bottom - top,
     (COLUMNS[column] + COLUMNS[column + 1]) / 2 - (182 * column + 105),
     body_y - (top + bottom) / 2)
    for top, bottom, body_y, count in ROWS
    for column in range(count)
]


class Bird:
    def __init__(self, image, x, y):
        self.image = image
        self.x, self.y = x, y
        self.frame = 0.0

    def update(self):
        self.frame = (self.frame + FLAP_FRAMES_PER_SECOND * game_framework.frame_time) % len(FRAMES)

    def draw(self, center_x, center_y):
        left, bottom, width, height, offset_x, offset_y = FRAMES[int(self.frame)]
        self.image.clip_draw(left, bottom, width, height,
                             center_x + self.x + offset_x * BIRD_SCALE,
                             center_y + self.y + offset_y * BIRD_SCALE,
                             round(width * BIRD_SCALE), round(height * BIRD_SCALE))



class Flock:
    def __init__(self, image):
        self.x, self.y = 650.0, 330.0
        self.birds = [Bird(image, 0, 0)]

    def update(self):
        for bird in self.birds:
            bird.update()

    def draw(self):
        for bird in self.birds:
            bird.draw(self.x, self.y)
