class BigThree:
    def __init__(self, weight, bench_press, squat, dead_lift):
        self.weight = weight
        self.bench_press = bench_press
        self.squat = squat
        self.dead_lift = dead_lift

    def output_big_three_weight_ratio(self):
        print(f'bench_press / weight = {self.bench_press / self.weight}')
        print(f'squat / weight = {self.squat / self.weight}')
        print(f'dead_lift / weight = {self.dead_lift / self.weight}')

    def output_big_three_weight_total(self):
        print(f'big three total is {self.bench_press + self.squat + self.dead_lift}')

    def output_big_three_weight_total_ratio(self):
        print(f'big three total / weight = {(self.bench_press + self.squat + self.dead_lift) / self.weight}')
