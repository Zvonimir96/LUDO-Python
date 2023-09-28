from .animation import Animation

animations = []


def add_callback(obj, callback):
    for animation in animations:
        if animation.object == obj:
            animation.callback = callback
            break


def add_animation(obj, animation_type):
    anim = Animation(obj, animation_type)
    anim.update()
    animations.append(anim)


def remove_animation(obj):
    for i, animation in enumerate(animations):
        if animation.object == obj:
            animations[i].disable()
            del animations[i]
            break
