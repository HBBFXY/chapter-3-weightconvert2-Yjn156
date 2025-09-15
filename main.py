current_weight = 60
moon_ratio = 0.165
yearly_gain = 0.5
years = 10
print("未来10年地球和月球上的体重变化")
for year in range(1,years + 1):
    earth_weight = current_weight + yearly_gain * year
    moon_weight = earth_weight * moon_ratio
    print(f"第{year}年：地球上的体重{earth_weight:.2f}kg,月球上的体重{moon_weight:.2f}kg")
