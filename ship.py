

class ShipAbstract:
    def __init__(self):
        self.is_sunk = False
        self.is_hit = False
        self.cost = -1
        self.vertical_length = -1
        self.horizontal_length = -1
        self.sprite = None
        self.num_scouts = -1
        self.num_attacks = -1
        self.total_alive = self.get_total()

    def get_total(self):
        return self.vertical_length * self.horizontal_length

    def rotate(self):
        self.vertical_length, self.horizontal_length = \
            self.horizontal_length, self.vertical_length

    def can_scout(self):
        return self.num_scouts > 0

    def can_attack(self):
        return self.can_attack > 0

    def register_hit(self):
        self.total_alive -= 1
        self.is_hit = True
        if self.total_alive == 0:
            self.is_sunk = True


class Carrier(ShipAbstract):
    def __init__(self):
        super().__init__()
        self.num_scouts, self.num_attacks = 0, 3
        self.vertical_length, self.horizontal_length = 5, 1
        self.cost = 5
        self.total_alive = self.get_total()


class Battleship(ShipAbstract):
    def __init__(self):
        super().__init__()
        self.num_scouts,  self.num_attacks = 0, 3
        self.vertical_length, self.horizontal_length = 4, 1
        self.cost = 4
        self.total_alive = self.get_total()


class Cruiser(ShipAbstract):
    def __init__(self):
        super().__init__()
        self.num_scouts, self.num_attacks = 0, 3
        self.vertical_length, self.horizontal_length = 3, 1
        self.cost = 3
        self.total_alive = self.get_total()


class Destroyer(ShipAbstract):
    def __init__(self):
        super().__init__()
        self.num_scouts, self.num_attacks = 0, 3
        self.vertical_length, self.horizontal_length = 2, 1
        self.cost = 2
        self.total_alive = self.get_total()


class Scout(ShipAbstract):
    def __init__(self):
        super().__init__()
        self.num_scouts, self.num_attacks = 0, 3
        self.vertical_length, self.horizontal_length = 1, 1
        self.cost = 1
        self.total_alive = self.get_total()
