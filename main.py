from ting_file_management.queue import Queue
from ting_file_management.file_process import process
from ting_file_management.file_process import remove
from ting_file_management.file_process import file_metadata
from ting_word_searches.word_search import exists_word

if __name__ == "__main__":
    queue = Queue()
    process('statics/arquivo_teste.txt', queue)
    process('statics/nome_pedro.txt', queue)

    remove(queue)  # Arquivo statics/arquivo_teste.txt removido com sucesso

    file_metadata(queue, 0)
    file_metadata(queue, 1)  # Posição inválida

    print(exists_word('menino', queue))
