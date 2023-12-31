# Project TING (Trybe is not Google)

#### This project consists of an application that simulates a document indexing algorithm similar to Google's, capable of identifying occurrences in TXT files.

* Solved by using Python

<details>
<summary>Description of created solutions:</summary>
<br>
  
| Function | Description | Location |
| ----------- | ----------- | ----------- |
| `Queue`   | Class created for storing files by queues | `ting_file_management/queue.py` |
| `txt_importer`   | Function capable of reading TXT files and returning them in list format | `ting_file_management/file_management.py` |
| `process`   | Function to import information from TXT file and add it to instance of `Queue` Class | `ting_file_management/file_process.py` |
| `remove`   | Function to remove first processed file present in instance | `ting_file_management/file_process.py` |
| `file_metadata`   | Function to find data in instance via given index | `ting_file_management/file_process.py` |
| `exists_word`   | Function to check for existence of a word in all processed files, returning a simplified report | `ting_word_searches/word_search.py` |
| `search_by_word`   | - | `ting_word_searches/word_search.py` |

</details>

<details>
<summary>Description of created test:</summary>
<br>
  
| Test | Description | Location |
| ----------- | ----------- | ----------- |
| `test_basic_priority_queueing`   | - | `tests/priority_queue/test_priority_queue.py` |

</details>


## Structure of project
  ```
  Legenda:
  🔸Arquivos que não podem ser alterados
  🔹Arquivos a serem alterados para realizar os requisitos.
  .
  ├──🔸dev-requirements.txt
  ├──🔸pyproject.toml
  ├──🔸README.md
  ├──🔸requirements.txt
  ├──🔸setup.cfg
  ├──🔸setup.py
  ├──statics
  │   ├──🔸arquivo_teste.csv
  │   ├──🔸arquivo_teste.txt
  │   ├──🔸nome_pedro.txt
  │   ├──🔸novo_paradigma_globalizado-min.txt
  │   └──🔸novo_paradigma_globalizado.txt
  ├──tests
  │   ├──🔸__init__.py
  │   ├──🔸test_file_management.py
  │   ├──🔸test_file_process.py
  │   ├──🔸test_queue.py
  │   └──🔸test_word_search.py
  ├──ting_file_management
  │   ├──🔹file_management.py
  │   ├──🔹file_process.py
  │   ├──🔸__init__.py
  │   └──🔹queue.py
  ├──ting_word_searches
  │   ├──🔸__init__.py
  │   └──🔹word_search.py
  └──🔸trybe.yml
```

### Instructions
* Clone the project and use the following commands:
  
```
To install dependencies and start applications:
<-- in root of the project -->
python3 -m venv .venv // create virtual environment
source .venv/bin/activate // activate virtual environment
python3 -m pip install -r dev-requirements.txt // install dependencies

```
### Running Application
* The `main.py` file contains examples for running application described below, command: `python3 -m main`

1. Create an instance of `Queue` Class and add information from TXT files in `statics` directory:
  ```
  queue = Queue()
  process('statics/arquivo_teste.txt', queue)
  process('statics/nome_pedro.txt', queue)
  ```
2. Remove the information in created instance with `remove` function:
  ```
  remove(queue)  # Arquivo statics/arquivo_teste.txt removido com sucesso
  ```
3. Locate the information in `index/position` with`file_metadata` function:
  ```
  file_metadata(queue, 0)  # Return first and only element in queue (nome_pedro.txt)
  file_metadata(queue, 1)  # Invalid position
  ```
4. Create search reports for words in instance using `exists_word` functions:
   `print(exists_word('menino', queue))`
   
   Return:
    ```
    [{
    "palavra": "menino",
    "arquivo": "statics/nome_pedro.txt",
    "ocorrencias": [
      {
        "linha": 1
      },
      {
        "linha": 2
      }
    ]
    }]
    ```
