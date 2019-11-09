# json-merge

**json-merge creates a single JSON array by reading JSON arrays
from different files.**

This program reads *base file name for input*, *base file name for output*,
*maximum size of the output file to be created* from the user.

starts from **input_basefilename1.json** and reads all the files in that
particular folder in a sequential order and creates a output JSON
file in that folder itself. If **output_basefilename1.json** already exist
in that foler then it increases the suffix count and check again.

When the file reaches maximum size specified size by the user, it terminates
automatically and informs user about the intermediate file created. which has
the size of *maximum_size* specified by the user.

If the specified file size is greater than the generated file, then it creates
a complete JSON file in that folder and displays a success message
Tested on : Linux

**Works with all kind of JSON arrays and Languages**
```
Time Complexity: O(n * m)

Space Complexity: O(m) [Creates a  global array to hold values ]
```

Requirements:
  ```
  Python 3
  ```
 To Run:
  ```
  python3 json-merge.py
  ```

  

