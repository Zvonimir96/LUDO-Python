from .animationType import AnimationType
import utilities


class Animation:
    def __init__(self, obj, animation_type):
        self.object = obj
        self.animation_type = animation_type
        self.fade_direction = True
        self.callback = None

    def update(self):
        if self.animation_type == AnimationType.BUTTON_ENABLE:
            self.object.image.set_alpha(utilities.fade_alfa)

        elif self.animation_type == AnimationType.DICE_ENABLE:
            self.object.color.value = utilities.fade_alfa

        elif self.animation_type == AnimationType.MOVE:
            fade = self.object.color.value

            if self.fade_direction:
                fade += utilities.fade_rate
            else:
                fade -= utilities.fade_rate

            if fade >= utilities.fade_max_limit:
                fade = utilities.fade_max_limit
                self.fade_direction = False
            elif fade <= utilities.fade_min_limit:
                fade = utilities.fade_min_limit
                self.fade_direction = True

            self.object.color.value = fade

            if self.callback is not None and fade == utilities.fade_max_limit:
                self.callback(self)

    def disable(self):
        if self.animation_type == AnimationType.BUTTON_ENABLE:
            self.object.image.set_alpha(utilities.fade_max_limit)

        # Turn off field
        if self.animation_type == AnimationType.DICE_ENABLE:
            self.object.set_default_color()
