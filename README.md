# Web Testing Demo Project

- [Introduction](#Introduction)
- [Downloading](#Downloading)
- [Requirements](#Requirements)
- [Running](#Running)

## Introduction <a name="Introduction"></a>
Demo project contains test implementations that verify some basic functions of <a href="https://en.wikipedia.org/wiki/Main_Page" target="_blank">wikipedia</a> page.

## Downloading <a name="Downloading"></a>
Clone this repository with your favorite Git client.

Access through *ssh* is recommended in all cases.

Example:
```bash
$> cd into/your/development/folder
$> git clone git@github.com:maiducduy/PLAYWRIGHT_DEMO.git
$> cd PLAYWRIGHT_DEMO
```

2. Create a branch from the master as a playground to test and experiment with the code.

## Requirements <a name="Requirements"></a>

- **Python:** python 3 must be installed (python 3.8.5 is recommended). The installer could be downloaded from <a href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a>

- **Python libraries:** list of additional libraries is described in *requirements.txt* file. All of them could be installed by 

    ```bash
    $> cd path/to/PLAYWRIGHT_DEMO
    $> pip -r requirements.txt
    ```

## Running <a name="Running"></a>
Run through **Terminal** : We have several ways to execute our test implementation.

- **Run all test files:** 

   ```bash
   $> cd path/to/PLAYWRIGHT_DEMO
   $> pytest --path ./Tests --html=./Results/results.html
   ```
   
 - **Run specified test:** 

   ```bash
   $> cd path/to/PLAYWRIGHT_DEMO
   $> pytest --path ./Tests/<test_file>.py::<TestClass>::<TestFunction> --html=./Results/results.html
   ```  
 
### Note:
For more information, please refer to <a href="https://docs.pytest.org/en/7.1.x/" target="_blank">Pytest documentary</a>
