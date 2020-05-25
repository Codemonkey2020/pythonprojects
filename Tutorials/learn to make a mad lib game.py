
lucky_numbers = [4, 5, 6, 1, 3, 9]
bikes = ["hero honda", "pulsar", "apache", "ktm", "duke", "ktm", "TVS50"]
bikes.extend(lucky_numbers)
print(bikes)

lucky_numbers.append(7)
print(lucky_numbers)

bikes.insert(1, "BMW")
print(bikes)

bikes.remove("pulsar")
print(bikes)

bikes.pop()
print(bikes)

print(bikes.index("ktm"))
print(bikes.count("ktm"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

bikes.clear()
print(bikes)

magical_numbers = lucky_numbers.copy()
print(magical_numbers)



