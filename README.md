# 40mb filesplit
filesplit is a Python module that is capable of splitting files of any size into multiple chunks and also merging them back. It can handle both structured and unstructured files and is available for Windows, Linux, and Mac operating systems with Python version 3.x.x1.

To use filesplit, you can install it via pip by running the command pip install filesplit1. Once installed, you can create an instance of the Split class by importing it from the filesplit.split module and providing the path to the input file and the output directory as arguments1. For example:

from filesplit.split import Split
split = Split(inputfile="path/to/inputfile", outputdir="path/to/outputdir")

With the instance created, you can use methods such as bysize or bylinecount to split the file by size or by line count, respectively1. The split files are generated in the format [original_filename]_1.ext, [original_filename]_2.ext, …, [original_filename]_n.ext, and a manifest file is also created in the output directory to keep track of the file splits1.

You can find more detailed information about how to use filesplit on its PyPI page.

Splitting a CSV file into smaller chunks using the filesplit module

This code demonstrates how to use the filesplit module to split a large CSV file into smaller chunks. The first line imports the Split class from the filesplit.split module. The second line creates an instance of the Split class, providing the path to the input file ("YOUR_FILE.csv") and the output directory ("C:/Users/user/Documents") as arguments.

The third line uses the bysize method of the Split instance to split the input file into chunks of a specified size. In this case, the size is set to 1024*1000*40, which is equivalent to 40MB. The newline=True argument ensures that each split will not produce any incomplete lines.

As a result, this code will split the "YOUR_FILE.csv" file into smaller chunks of 40MB each, and save them in the "C:/Users/user/Documents" directory.

