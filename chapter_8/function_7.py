def city_temp(**param):
    for k, v in param.items():
        print(k, ":", v)


city_temp(bj="32c", xm='23c')
city_temp(**{'sh': '31c', 'tj': '99c'})
