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

            # Change from secondary to primary color
            if fade <= utilities.fade_min_limit and self.object.secondary_color is not None \
                    and self.object.primary_color is not None:
                if self.object.color == self.object.primary_color:
                    self.object.set_secondary_color()
                else:
                    self.object.set_primary_color()

            self.object.color.value = fade

            if self.callback is not None:
                if self.callback.__name__ == 'figure_callback_max' and fade >= utilities.fade_max_limit:
                    self.callback(self)
                if self.callback.__name__ == 'figure_callback_min' and fade <= utilities.fade_min_limit:
                    self.callback(self)

    def disable(self):
        if self.animation_type == AnimationType.BUTTON_ENABLE:
            self.object.image.set_alpha(utilities.fade_max_limit)

        if self.animation_type == AnimationType.DICE_ENABLE:
            self.object.set_default_color()

        if self.animation_type == AnimationType.MOVE:
            self.object.secondary_color = None

            if self.object.primary_color is None:
                self.object.set_default_color()
            else:
                self.object.set_primary_color()
