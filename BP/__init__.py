from re import sub, findall

class Transpiler:
    def __init__(self, file: str) -> None:
        with open(file, "r") as file_content:
            self.file = file_content.read()
    def transpile(self) -> str:
        declarations, functions = "", ""
        functions_portion, main_portion = self.file.split("\n-- MAIN --\n")
        declarations = "\n".join(findall(r"FN\s.*\)", functions_portion)) + "\n" + "\n".join(findall(r"SUB\s.*\)", functions_portion))
        declarations = sub(r"FN\s(.*\))", r"DECLARE FUNCTION \1", declarations)
        declarations = sub(r"SUB\s(.*\))", r"DECLARE SUB \1", declarations)
        declarations = declarations.replace("::","_")
        functions    = sub(r"FN\s(.*\))", r"FUNCTION \1", functions_portion)
        functions    = sub(r"SUB\s(.*\))", r"SUB \1", functions)
        functions    = sub(r"END\sFN", r"END FUNCTION", functions)
        functions    = sub(r"END\sSUB", r"END SUB", functions)
        functions    = functions.replace("::","_")
        class_dec    = "".join(findall(r"CDEF\s(.*)", main_portion)).replace(", ",",").split(",")
        main_portion = main_portion.replace("".join(findall(r"CDEF\s.*", main_portion)),"")
        for class_ in class_dec:
            var, class__ = class_.split(":")
            #globals()[var] = class__
            functions    = sub(var+r"\:\:(.*)\s", var+r"_\1", functions)
            print(var)
            main_portion = sub(var+r"\:\:(.*\()(.*\))",class_+"_"+r"\1"+var+r",\2\n",main_portion).replace(f"{var}:","").replace(f"{var},","")
            main_portion = sub(var+r"\:\:(.*)\s", var+r"_\1", main_portion)
            final = f"{declarations}CLS{main_portion}\nEND\n{functions}"
        print(final)
        return final
    def write_to_file(self, file: str) -> None:
        with open(file, "w") as file_content:
            file_content.write(self.transpile())
