# :construction: README em construção ! :construction:

# Project TING (Trybe is not Google)

#### This...

* Solved using Python

<details>
<summary>Description of created solutions:</summary>
<br>
  
| Function | Description | Location |
| ----------- | ----------- | ----------- |
| `Queue`   | ... | `ting_file_management/queue.py` |
| `txt_importer`   | ... | `ting_file_management/file_management.py` |
| `process`   | ... | `ting_file_management/file_process.py` |
| `remove`   | ... | `ting_file_management/file_process.py` |
| `file_metadata`   | ... | `ting_file_management/file_process.py` |
| `exists_word`   | ... | `ting_word_searches/word_search.py` |
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
