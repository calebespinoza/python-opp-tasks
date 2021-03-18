class Helper:

    @staticmethod
    def my_lenght(structure):
        if type(structure) == list or type(structure) == dict or type(structure) == str:
            i = 0
            for key in structure:
                i = i + 1
            print(i)
        else:
            raise ValueError("You don't entered a String or a Structure")

