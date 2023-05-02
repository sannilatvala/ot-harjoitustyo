import pygame


class Snake:
    """Matoa kuvaava luokka.
    """

    def snake(self, position, block_size):
        """Palauttaa madon yhtä osaa vastaavan objektin.

        Args:
            position: lista, joka kuvaa madon osan sijaintia.

        Returns:
            Palauttaa 'pygame.Rect'-objektin
        """

        rect = pygame.Rect(position[0], position[1], block_size, block_size)
        return rect

    def move_snake(self, snake_body, change_x, change_y, collision):
        """Vastaa madon liikumisesta

        Args:
            snake_body: lista joka kuvaa matoa.
            change_x: muutos x:n arvossa
            change_y: muutos y:n arvossa
            collision: Boolean-arvo, joka kuvastaa onko mato törmännyt ruokaan.

        Returns:
            Palauttaa listan, joka kuvaa matoa
        """

        old_head = snake_body[0]
        new_x = old_head[0] + change_x
        new_y = old_head[1] + change_y
        new_head = [new_x, new_y]
        snake_body.insert(0, new_head)
        if not collision:
            snake_body.pop()

        return snake_body
