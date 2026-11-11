import time

running = False
stack = []
frame_time = 0.0


def quit():
    global running
    running = False


def run(start_mode):
    global running, stack, frame_time
    running = True
    stack = [start_mode]
    frame_time = 0.0

    try:
        start_mode.init()
        previous_time = time.perf_counter()
        while running:
            current_time = time.perf_counter()
            frame_time = current_time - previous_time
            previous_time = current_time
            stack[-1].handle_events()
            if not running:
                break
            stack[-1].update()
            stack[-1].render()
            time.sleep(max(0.0, 1 / 60 - (time.perf_counter() - current_time)))
    finally:
        while stack:
            stack.pop().finish()
        running = False
