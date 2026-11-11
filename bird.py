BIRD_SCALE = 0.45
SHEET_HEIGHT = 506
COLUMNS = (0, 182, 364, 546, 727, 918)
ROWS = ((0, 164, 5), (164, 350, 5), (350, 506, 4))

# 원본의 위쪽 기준 행을 Pico2D의 아래쪽 기준으로 변환한다.
FRAMES = [
    (COLUMNS[column], SHEET_HEIGHT - bottom,
     COLUMNS[column + 1] - COLUMNS[column], bottom - top)
    for top, bottom, count in ROWS
    for column in range(count)
]


class Bird:
    def __init__(self, image, x, y):
        self.image = image
        self.x, self.y = x, y
        self.frame = 0.0

    def update(self):
        pass

    def draw(self):
        left, bottom, width, height = FRAMES[int(self.frame)]
        self.image.clip_draw(left, bottom, width, height, self.x, self.y,
                             round(width * BIRD_SCALE), round(height * BIRD_SCALE))
