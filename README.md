# json-merge

**json-merge creates a single JSON array by reading JSON arrays
from different files.**

## Functions:
  1. Supports non-english words as well.
  2. Creates file only upto the maximum size specified by the user.
  3. Merging works for any array name.

This program reads *base file name for input*, *base file name for output*,
*maximum size of the output file to be created* from the user.

starts from **input_basefilename1.json** and reads all the files in that
particular folder in a sequential order and creates a output JSON
file in that folder itself. If **output_basefilename1.json** already exist
in that folder then it increases the suffix count and checks again.

When the file reaches maximum size [in bytes] specified size by the user, it terminates
automatically and informs user about the intermediate file created. which has
the size of *maximum_size* specified by the user.

If the specified file size is greater than the generated file, then it creates
a complete JSON file in that folder and displays a success message


Tested on : Linux

## Time and Space analysis

**Works with all kind of JSON arrays and Languages**
```
Time Complexity: O(n * m)

Space Complexity: O(m) [Creates a  global array to hold values ]
```


#### Requirements:

  ```
  Python 3
  ```
#### To Run:
  ```
  python3 jsonmerge.py
  ```

  ### data1.json
  
 ![data1](data1.PNG?raw=true "data1.json input file")
  
  ### data2.json
  
 ![data2](data2.PNG?raw=true "data2.json input file")
 
 ### data3.json
 
 ![data3](data3.PNG?raw=true "data3.json input file")
 
 ### Terminal
 
 ![terminal](terminal_run.png?raw=true "Terminal Screenshot")
 
 ### merge1.json
 
 ![merge1](merge1.PNG?raw=true "merge1.json output file")
 

