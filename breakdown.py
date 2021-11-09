class Breakdown:

    script = []
    functions = []

    def __init__(self, script):
        Breakdown.script = script

    @staticmethod
    def searching(x):
        infunction = [False, ""]
        inclass = [False, ""]
        inconditionalstatement = False

        if infunction[0] == True:
            if "\t" in x:
                print("Still in function " + infunction[1] + "!")
            else:
                print("We are out of the function")
                infunction[0] = False
                infunction[1] = ""


        elif inclass[0] == True:
            if "\t" in x:
                print("Still in class " + inclass[1] + "!")
            else:
                print("We are out of the class")
                inclass[0] = False
                inclass[1] = ""

        elif inconditionalstatement == True:
            if "\t" in x:
                print("Still in a conditional statement")


        if "def" in x:

            funcnam1 = x.split(" ")
            funcname2 = funcnam1[1].split("(") # Getting function name

            param1 = x.split("(")
            param2 = param1[1].split(")") # Fetching parameters

            print("Function " + funcname2[0] + " requires these parameters: " + param2[0])

            if infunction[0] == True:
                print("We are in a nested function")

            infunction[0] = True
            infunction[1] = funcname2[0]

        elif "class" in x:
            print("We are in a class")
            if "(" in x:
                print("This class has parameters!")
            classnam1 = x.split(" ")
            classnam2 = classnam1[1]

        elif "if" in x:
            condition = x.split("f")
            print("Checking if " + condition[1])
            inconditionalstatement = True

        elif "elif" in x:
            condition = x.split("f")
            print("Also checking if " + condition[1])

        elif "else" in x:
            inconditionalstatement = False





    @staticmethod
    def find(path):
        with open(path, 'r') as fileObj:
            code = fileObj.read()
            script = code.split("\n")
            for line in script:
                Breakdown.searching(line)

        return 0
