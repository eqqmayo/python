# 281 ~ 287
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    
    def 정보(self):
        print('바퀴수', self.바퀴)
        print('가격', self.가격)

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

    def 정보(self):
        super().정보()
        print('구동계', self.구동계)

class 자동차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)

# 288
# 자식호출 

# 289
# 자식생성

# 290
# 자식생성
# 부모생성