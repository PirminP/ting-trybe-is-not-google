import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for arquive in instance._data:
        if path_file == arquive['nome_do_arquivo']:
            return None

    data_file = txt_importer(path_file)
    dict_file = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data_file),
        'linhas_do_arquivo': data_file
    }
    instance.enqueue(dict_file)
    sys.stdout.write(str(dict_file))


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write('Não há elementos\n')
    else:
        delete_file = instance.dequeue()
        sys.stdout.write(
            f'Arquivo {delete_file["nome_do_arquivo"]} removido com sucesso\n'
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
