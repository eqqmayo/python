class Car:
    def __init__(self, make, model):
        self._make = make
        self._model = model
        self._odometer = 0

    def get_name(self):
        long_name = f'{self._make} {self._model}'
        return long_name.title()  # 문자열에서 각 단어의 첫번째 문자를 대문자화

    def read_odometer(self):
        print(f'이 차의 주행거리: {self._odometer}')

    def update_odometer(self, mileage):
        if self._odometer < mileage:
            self._odometer = mileage
        else:
            print('주행거리 속일 수 없음')

    def increment_odometer(self, distance):
        self._odometer += distance
