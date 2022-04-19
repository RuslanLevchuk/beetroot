import pyglet

window = pyglet.window.Window(fullscreen=True)

class Timer:

    def __init__(self):
        self.label = pyglet.text.Label('00:00', font_size=300,
                                       x=window.width // 2,
                                       y=window.height // 2,
                                       anchor_x='center', anchor_y='center')
        self.reset()

    def reset(self):
        self.time = 0
        self.running = False
        self.label.text = '00:00'
        self.label.color = (20, 200, 0, 234)

    def update(self, dt):
        if self.running:
            self.time += dt
            m, s = divmod(self.time, 60)
            self.label.text = '%02d:%02d' % (m, s)
            if m >= 5:
                self.label.color = (180, 0, 0, 0)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        if timer.running:
            timer.running = False
        else:
            if timer.time > 0:
                timer.reset()
            else:
                timer.running = True
    elif symbol == pyglet.window.key.ESCAPE:
        window.close()

@window.event
def on_draw():
    window.clear()
    timer.label.draw()

timer = Timer()
pyglet.clock.schedule_interval(timer.update, 1)
pyglet.app.run()
