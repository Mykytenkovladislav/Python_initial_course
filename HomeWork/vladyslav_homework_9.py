class Road:
    def __init__(self, quality, material=None):
        self.quality = quality
        if quality > 60:
            self.material = material


class Car:
    def __init__(self, max_speed=0, weight=0, model='Lada'):
        self.weight = weight
        self.max_speed = max_speed
        self.name = model

    def drive(self, current_speed=0, start_route='start_point', end_route='end_route', road: Road = None):
        if self.max_speed < current_speed:
            current_speed = self.max_speed
            print(current_speed)
        else:
            print(f'Drive from {start_route} to {end_route} with speed {current_speed}')


mercedes = Car(30, 200, 'Mercedes', 'Parapapam')
road_a = (67, 'asphalt')
tesla_x = Car(max_speed=250, weight=2000, model='Tesla X')
tesla_x.drive(current_speed=300, road=road_a)