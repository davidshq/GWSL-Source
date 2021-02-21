class animation:
    """
    Animation
    """
    def __init__(self, pos, identifier):
        self.pos = pos
        self.new_pos = pos
        self.id = identifier
        self.vel = []

    def get(self):
        pos = [round(self.pos[0]), round(self.pos[1])]
        return self.pos

    def update(self, func, clock):
        axes = len(self.pos)
        vel = []
        FPS = clock.get_fps()
        scale = (FPS / 60.0) * 2.0

        if scale <= 0.2:
            scale = 3

        for axis in range(axes):
            vel.append(0)
            if self.pos[axis] != self.new_pos[axis]:
                if func == "ease":
                    if self.pos[axis] < self.new_pos[axis] - ((self.new_pos[axis] - self.pos[axis] / 2 * scale)):
                        vel[axis] = (self.new_pos[axis] - self.pos[axis]) / (2 * scale)

                    elif self.pos[axis] > self.new_pos[axis] + (((self.pos[axis] - self.new_pos[axis]) / (2 * scale))):
                        vel[axis] = -1 * (self.pos[axis] - self.new_pos[axis]) / (2 * scale)
                elif func == "old":
                    if self.pos[axis] < self.new_pos[axis]:
                        vel[axis] = 1 * scale

                    elif self.pos[axis] > self.new_pos[axis]:
                        vel[axis] = -1 * scale

                elif func == "pop":
                    self.pos[axis] = self.new_pos[axis]

                self.vel = vel
                self.pos[axis] += vel[axis]
                if self.pos[axis] < 0:
                    self.pos[axis] = 0
                diff = self.new_pos[axis] - self.pos[axis]
                if diff < 0:
                    diff *= -1
                if diff < 1:
                    self.pos[axis] = self.new_pos[axis]

            # bounce

    def animate(self, new_pos):
        self.new_pos = new_pos

    def pop(self, new_pos):
        self.new_pos = new_pos
        self.pos = new_pos


class animator:
    def __init__(self, fpsClock):
        self.animations = set()
        self.func = "ease"
        self.clock = fpsClock

    def register(self, identifier, init_pos):
        animation_object = animation(init_pos, identifier)
        self.animations.add(animation_object)

    def update(self):
        for anim in self.animations:
            anim.update(self.func, self.clock)

    def animate(self, identifier, new_pos):
        for anim in self.animations:
            if anim.id == identifier:
                return anim.animate(new_pos)

    def get(self, identifier):
        for anim in self.animations:
            if anim.id == identifier:
                return anim.get()

    def pop(self, identifier, new_pos):
        for anim in self.animations:
            if anim.id == identifier:
                return anim.pop(new_pos)

    def set_func(self, anim_type):
        self.func = anim_type

