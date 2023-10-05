from .animation import Animation

animations = []


def add_callback(obj, callback):
    """
    Add callback to already existing animation.

    :param obj: field or button that already has animation.
    :param callback: function to be called.
    :return: None
    """

    for animation in animations:
        if animation.object == obj:
            animation.callback = callback
            break


def add_animation(obj, animation_type):
    """
    Add animation to pool.

    :param obj: can be field or button.
    :param animation_type: type of animation.
    :return: None
    """

    anim = Animation(obj, animation_type)
    anim.update()
    animations.append(anim)


def remove_animation(obj):
    """
    Remove animation from pool.

    :param obj: field or button that already has animation.
    :return: None
    """
    for i, animation in enumerate(animations):
        if animation.object == obj:
            animations[i].disable()
            del animations[i]
            break
