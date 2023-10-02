from copy import copy

from dice import Dice
from layot import houses, button_sets, PositionType, safe_houses
from layot.elements.path import path_fields
from utilities import available_colors, default_color_value, default_color_saturation, black_color
from .figure import Figure


class Player:
    def __init__(self, orderNumber):
        # Get first available color
        self.color = available_colors.pop()

        # Get house and buttons layout for player
        self.house = houses[orderNumber]
        self.safe_house = safe_houses[orderNumber]
        self.buttons = button_sets[orderNumber]

        # Create player figures
        self.figures = []
        for i in range(4):
            self.figures.append(Figure(self.house.fields[i], self.color))

        self.selected_figure = None
        self._change_color()

        # Sometimes player can roll more than once at one turn
        self.re_rolls = 0

        # LUDO can be played with two players
        # Not everyone has to play
        self.playable = False

    def change_color_left(self):
        # Set player color to next available color in descending order
        available_colors.insert(0, self.color)
        self.color = available_colors.pop()

        # Change player color
        self._change_color()

    def change_color_right(self):
        # Set player color to next available color
        available_colors.append(self.color)
        self.color = available_colors.pop(0)

        # Change player color
        self._change_color()

    def disable(self):
        # Set black color to all buttons and figures
        for button in self.buttons:
            button.set_color(black_color)

        for figure in self.figures:
            figure.set_color(black_color)

        # Şet black color of house exit
        self.house.exit_field.default_color = black_color
        self.house.exit_field.set_default_color()

        # Şet black color of safe house fields
        for field in self.safe_house.fields:
            field.default_color = black_color
            field.set_default_color()

    def _change_color(self):
        # Change color of all buttons and figures
        for button in self.buttons:
            button.set_color(self.color)

        for figure in self.figures:
            figure.set_color(self.color)

        # Create fade color
        fade_color = copy(self.color)
        fade_color.value = default_color_value
        fade_color.saturation = default_color_saturation

        # Set house exit to faded player color
        self.house.exit_field.default_color = fade_color
        self.house.exit_field.set_default_color()

        # Set safe house exit to faded player color
        for field in self.safe_house.fields:
            field.default_color = fade_color
            field.set_default_color()

    def get_empty_house_field(self):
        for field in self.house.fields:
            if field.color == black_color:
                return field

    def select_figure_left(self):
        # This function can only be called when figure is selected
        index = self.figures.index(self.selected_figure)

        # Iterate through figures from selected figure to end
        for figure in self.figures[index+1:]:
            if self._can_figure_move(figure):
                self.selected_figure = figure
                return figure

        # Iterate through figures from start to end
        for figure in self.figures[:index+1]:
            if self._can_figure_move(figure):
                self.selected_figure = figure
                return figure

    def select_figure_right(self):
        # This function can only be called when figure is selected
        index = self.figures.index(self.selected_figure)

        # Iterate through figures from selected figure to start
        for figure in self.figures[index-1::-1]:
            if self._can_figure_move(figure):
                self.selected_figure = figure
                return figure

        # Iterate through figures from end to selected figure
        for figure in self.figures[:index:-1]:
            if self._can_figure_move(figure):
                self.selected_figure = figure
                return figure

    def select_figure(self):
        # Find figure in ascending order
        for figure in self.figures:
            if self._can_figure_move(figure):
                self.selected_figure = figure
                return figure

        return None

    def can_reroll(self):
        # If player haw all figures in hose, allow it to reroll
        for figure in self.figures:
            if not figure.field.position.type == PositionType.HOUSE:
                return False

        return True

    def _can_fit_sh(self, num_filed):
        if num_filed > 4:
            return False

        position = self.safe_house.fields[0].position

        # Check for each position
        for i in range(num_filed):
            # Check for each figure
            for figure in self.figures:
                if figure.field.position == position:
                    return False

            position += 1

        return True

    def _can_figure_move(self, figure):
        figure_position = figure.field.position

        if figure_position.type == PositionType.PATH:
            # Check if figure can go to safe house
            sh_entrance_position = self.safe_house.entrance_field.position
            distance_to_safe_house = figure_position.distance(sh_entrance_position)
            if distance_to_safe_house < Dice.number:
                safe_house_fields = Dice.number - distance_to_safe_house
                # TODO Check if figure can fit into safe house
                if not self._can_fit_sh(safe_house_fields):
                    return False

                # Add fields in front of the house
                position = figure_position
                for i in range(Dice.number - safe_house_fields):
                    position += 1
                    figure.move_fields.append(path_fields[position.index])

                # Add fields in safe house
                position = self.safe_house.fields[0].position
                for i in range(safe_house_fields):
                    figure.move_fields.append(self.safe_house.fields[position.index])
                    position += 1

                return True

            next_position = figure_position + Dice.number

            # If one of player figures is located on same position as figure destination return false
            for fig in self.figures:
                if fig.field.position == next_position:
                    return False

            # Set next available field to move
            position = figure_position
            for i in range(Dice.number):
                position += 1
                figure.move_fields.append(path_fields[position.index])

            return True

        elif figure_position.type == PositionType.HOUSE:
            if Dice.number == 6:
                # If one of player figures is located on same position as figure destination return false
                for fig in self.figures:
                    if fig.field.position == self.house.exit_field.position:
                        return False

                # Set next available field to move
                figure.move_fields.append(self.house.exit_field)
                return True

        elif figure_position.type == PositionType.SAFE_HOUSE:
            pass

        return False
