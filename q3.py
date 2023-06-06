def generator_function():
  for item in [1, 2, 3, 4, 5]:
    yield item

print(generator_function())