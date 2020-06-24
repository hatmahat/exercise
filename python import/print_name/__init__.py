class Name:
    """
    Arguments
    -----------
    name    :
    age     :
    height  :
    weight  :
    """     

    def __init__(self, name, age, height, weight):
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age
    
    def print_name(self):
        print(self._name)

    def print_age(self):
        print(self._age)