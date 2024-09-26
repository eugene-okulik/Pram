temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25,
                29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

warm_temperature = 28
warm_days = list(filter(lambda x: x > warm_temperature, temperatures))
print(warm_days)
print(f"Максимальная температура: {max(warm_days)}")
print(f"Минимальная температура: {min(warm_days)}")
print(f"Средняя температура: {round(sum(warm_days)/len(warm_days),2)}")
