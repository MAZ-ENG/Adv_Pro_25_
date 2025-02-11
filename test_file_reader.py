
import pytest

from File_reader import FileReader

def test_file_extension():
    assert FileReader.file_extension("sample_1.txt") == "txt"
    assert FileReader.file_extension("sample_2.txt") == "txt"

def test_read_lines():
    file1 = FileReader("sample_1.txt")
    lines1 = list(file1.read_lines())

    file2 = FileReader("sample_2.txt")
    lines2 = list(file2.read_lines())

    #assert isinstance(lines1, list)
    #assert isinstance(lines2, list)
    assert isinstance(lines1 + lines2, list) 

#def test_files_merged():
#    merged_files_fin = FileReader(merged_files_fin) = ("file1" + "file2")


    