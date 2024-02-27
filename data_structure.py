class DataProcessor:
    def sort_tuple(self, input_tuple):
        # Returns the sorted tuple
        return tuple(sorted(input_tuple))
    
    def append_to_list(self, input_list, element):
        # Appends the element to the list and returns the sorted list
        input_list.append(element)
        return input_list
    
    def update_dictionary(self, input_dict, key, value):
        # Updates the dictionary with the key-value pair
        input_dict[key] = value
        return input_dict
    
    def remove_from_set(self, input_set, element):
        # Removes the element from the set
        input_set.discard(element)
        return input_set
from data_structures import DataProcessor

# Creating an instance of DataProcessor
data_processor = DataProcessor()

# Testing the methods
input_tuple = (3, 1, 2)
sorted_tuple = data_processor.sort_tuple(input_tuple)
print("Sorted tuple:", sorted_tuple)

input_list = [1, 2, 3]
element_to_append = 4
appended_list = data_processor.append_to_list(input_list, element_to_append)
print("Appended list:", appended_list)

input_dict = {'a': 1, 'b': 2}
key_to_update = 'c'
value_to_update = 3
updated_dict = data_processor.update_dictionary(input_dict, key_to_update, value_to_update)
print("Updated dictionary:", updated_dict)

input_set = {1, 2, 3}
element_to_remove = 2
set_after_removal = data_processor.remove_from_set(input_set, element_to_remove)
print("Set after removal:", set_after_removal)