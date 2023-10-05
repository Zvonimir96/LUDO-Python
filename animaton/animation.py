from .animationType import AnimationType
import utilities


class Animation:
    """
    Represents one animation.
    """
    def __init__(self, obj, animation_type):
        """

        :param obj: can be field or button.
        :param animation_type: type of animation.
        """

        self.object = obj
        self.animation_type = animation_type
        self.fade_direction = True
        self.callback = None

    def update(self):
        """
        Update animation depended on the type of animation.

        :return: None
        """

        if self.animation_type == AnimationType.BUTTON_ENABLE:
            self.object.image.set_alpha(utilities.fade_alfa)

        elif self.animation_type == AnimationType.DICE_ENABLE:
            self.object.color.value = utilities.fade_alfa

        elif self.animation_type == AnimationType.MOVE:
            fade = self.object.color.value

            # Fade or illuminate object
            if self.fade_direction:
                fade += utilities.fade_rate
            else:
                fade -= utilities.fade_rate

            # Decide whether object should be faded or illuminated
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

            # Some functions have callbacks
            if self.callback is not None:
                # Depended on the illumination of object call different function
                if self.callback.__name__ == 'figure_callback_max' and fade >= utilities.fade_max_limit:
                    self.callback(self)
                if self.callback.__name__ == 'figure_callback_min' and fade <= utilities.fade_min_limit:
                    self.callback(self)

    def disable(self):
        """
        Set default color of the object.

        :return: None
        """

        if self.animation_type == AnimationType.BUTTON_ENABLE:
            self.object.image.set_alpha(utilities.fade_max_limit)

        if self.animation_type == AnimationType.DICE_ENABLE:
            self.object.set_default_color()

        if self.animation_type == AnimationType.MOVE:
            # Secondary color is only used for animations
            # When animation is done color is no longer needed
            self.object.secondary_color = None

            # If object has primary color, set it instead of default color
            if self.object.primary_color is None:
                self.object.set_default_color()
            else:
                self.object.set_primary_color()
