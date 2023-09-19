from .animation import Animation

animations = []


def add_animation(obj, animation_type):
    anim = Animation(obj, animation_type)
    anim.update()
    animations.append(anim)


def remove_animation(obj):
    for i, a in enumerate(animations):
        if a.object == obj:
            animations[i].disable()
            del animations[i]
            break
