
import os

# ---- Colorize//Decorator ---
def auto_colorize(func):
    def wrapper(self, *args, **kwargs):
        for line in func(self, *args, **kwargs):
            if self.color:
                yield f"{self.color}{line}\033[0m" 
            else:
                yield line
    return wrapper

#----- FileReader Class block ----    
class FileReader:
    def __init__(self, filename, color=None):
        self._filename = filename
        self.color = color

    @property
    def filename(self):
        """Read-only filename property."""
        return self._filename

    def raw_read_lines(self):
        with open(self.filename, "r") as file:
            for line in file:
                yield line.rstrip()
    
    @auto_colorize
    def read_lines(self):
        return self.raw_read_lines()

    def __str__(self):
        return f"FileReader for {self.filename}"   

    def __add__(self, other):
        """Concatenates two files using '+' operator."""
        new_filename = "merged_file.txt"
        #blue = "\033[34m"
        #orange= "\033[98m"
        yellow = "\033[33m"
        green = "\033[92m"
        reset = "\033[0m"
        with open(new_filename, "w") as new_file:
            for line in self.raw_read_lines():
                new_file.write(f"{yellow}{line}{reset}\n")
            new_file.write("\n")
            for line in other.raw_read_lines():
                new_file.write(f"{green}{line}{reset}\n")
        return FileReader(new_filename)  # Returns new merged file

    

    @staticmethod
    def file_extension(filename):
        """Returns the file extension."""
        return filename.split(".")[-1]

    
if __name__ == "__main__":
    file1 = FileReader("sample_1.txt")
    file2 = FileReader("sample_2.txt")

    merged_file_fin = file1 + file2

    for line in merged_file_fin.read_lines():
        print(line)

