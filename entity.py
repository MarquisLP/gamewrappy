"""This module contains base classes for defining game objects as well
as their individual components and behaviours.
"""
from pygame.sprite import Sprite


class Entity(Sprite):
    """An object within the game.

    It contains several Component objects that are used to define how it
    is handled graphically and physically, as well as its behaviour.

    Since it inherits from PyGame's Sprite class, it can be added to
    any Groups you have created. (Components will automatically add it
    to the appropriate Groups.)
    This also makes discarding it from the game simple, as it will
    automatically be removed from memory once it belongs to no Groups.

    Attributes:
        components (list): Contains all of the Component objects that
            are contained in this Entity.
        * Note that components will also be added as unique attributes
          automatically. This will make it possible to access each
          component directly, rather than having to add .components.
          in-between this Entity's name and the component's name.
    """
    pass


class Component(object):
    """Part of an Entity object.

    It will handle one facet of the Entity, which can be graphics,
    physics, or part of its behaviour. Subclasses should define their
    own attributes and methods in order to accomplish this.

    Ideally, a game would have many Component subclasses to define the
    many different parts that make up different game objects.

    Attributes:
        entity (Entity): This Component is bound to it and has access
            to all of its members.
    """
    def __init__(*args):
        """Declare and initialize instance variables.

        Subclasses can override this method with their own unique
        parameters. However, make sure to call this as a super method in
        order to initialize the entity attribute.
        """
        self.entity = None

    def bind_to_entity(self, entity):
        """Bind this Component to an Entity object.

        Args:
            entity (Entity): This component will be bound to it and have
                access to all of its members.
        """
        self.entity = entity
        self._add_self_as_attribute(entity)

    def _add_self_as_attribute(self, entity):
        """Add this Component as a new attribute in an Entity object.

        Note that this will overwrite an existing Component in the
        Entity if it is of the same class as this one.

        Args:
            entity (Entity): Will receive this Component as an
                attribute.
        """
        class_name = type(self).__name__
        setattr(entity, class_name, self)