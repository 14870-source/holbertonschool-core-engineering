#!/usr/bin/env python3
"""Defines mixins and a Dragon class."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon with swimming and flying abilities."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
