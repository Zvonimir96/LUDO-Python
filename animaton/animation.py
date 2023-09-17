from .animationType import AnimationType
import utilities


class Animation:
    def __init__(self, obj, animation_type):
        self.object = obj
        self.animation_type = animation_type

    def update(self):
        if self.animation_type == AnimationType.BUTTON_ENABLE:
            self.object.image.set_alpha(utilities.fade_alfa)

        if self.animation_type == AnimationType.DICE_ENABLE:
            self.object.color.value = utilities.fade_alfa

    def disable(self):
        if self.animation_type == AnimationType.BUTTON_ENABLE:
            self.object.image.set_alpha(utilities.fade_max_limit)
