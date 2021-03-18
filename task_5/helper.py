class Helper:

    @staticmethod
    def my_lenght(structure):
        if type(structure) == list or type(structure) == dict or type(structure) == str:
            print(len(structure))
        else:
            raise ValueError("You don't entered a String or a Structure")

