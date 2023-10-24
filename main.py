class Ship:
    def __init__(self):
        self.onanchor = True
        self.dist = 0
        self.speed = 0
        self.kernels = 0
        self.kernels_in_port = 25

    def sail(self):
        if self.onanchor:
            print('Не можем плыть, пока стоим на якоре')
        else:
            self.dist += self.speed
            print('Проплыли', self.dist, 'км')

    def port(self):
        self.kernels += self.kernels_in_port
        print('Зашли в порт, закупили', self.kernels_in_port, 'ядер')

    def anchor(self):
        if self.onanchor:
            self.onanchor = False
            print('Снялись с якоря')
        else:
            self.onanchor = True
            print('Встали на якорь')

    def fire(self, rounds):
        pass


class Frigate(Ship):
    def __init__(self):
        Ship.__init__(self)
        self.cannons = 20
        self.speed = 30

    def fire(self, rounds=1):
        if self.kernels >= self.cannons:
            print('Сделали', self.cannons, 'выстрелов')
            self.kernels -= self.cannons
        elif self.kernels > 0:
            print('Сделали', self.kernels, 'выстрелов')
            self.kernels = 0
        else:
            print('Нет ядер')



class Yacht(Ship):
    def __init__(self):
        Ship.__init__(self)
        self.cannons = 2
        self.speed = 60

    def fire(self, rounds):
        if self.kernels >= self.cannons * rounds:
            print('Сделали', rounds, 'полных залпов по', self.cannons, 'выстрела')
            self.kernels -= self.cannons * rounds
        elif self.cannons <= self.kernels < self.cannons * rounds:
            if self.kernels % self.cannons == 0:
                print('Сделали', self.kernels / self.cannons, 'полных залпов по', self.cannons, 'выстрела')
            else:
                print('Сделали', self.kernels // self.cannons, 'полных залпов по', self.cannons, 'выстрела и 1 залп', self.kernels % self.cannons, 'выстрел')
            self.kernels = 0
        elif self.kernels > 0:
            print('Сделали 1 залп', self.kernels, 'выстрел')
            self.kernels = 0
        else:
            print('Нет ядер')


frig = Frigate()
ya = Yacht()

print('=============Фрегат=============')
frig.sail()
frig.anchor()
frig.sail()
frig.sail()
frig.anchor()
frig.fire()
frig.anchor()
frig.port()
frig.anchor()
frig.fire()
frig.fire()
frig.fire()

print('=============Яхта=============')
ya.sail()
ya.anchor()
ya.sail()
ya.sail()
ya.anchor()
ya.fire(1)
ya.anchor()
ya.port()
ya.anchor()
ya.fire(6)
ya.fire(5)
ya.fire(6)
ya.fire(5)