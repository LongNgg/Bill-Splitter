# The following line creates a dictionary from the input. Do not modify it, please
import operator
test_dict = {"a": 43, "b": 1233, "c": 8}
min_value = min(test_dict.items(), key=operator.itemgetter(1))
max_value = max(test_dict.items(), key=operator.itemgetter(1))
print('min:', min_value[0])
print('max:', max_value[0])
# Work with the 'test_dict'