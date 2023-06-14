def exists_word(word, instance):
    result = []
    for archive in instance._data:
        info_file = {
            'palavra': word,
            'arquivo': archive['nome_do_arquivo'],
            'ocorrencias': []
        }

        for i in range(archive['qtd_linhas']):
            if word.lower() in archive['linhas_do_arquivo'][i].lower():
                info_file['ocorrencias'].append({'linha': i + 1})

        if info_file['ocorrencias']:
            result.append(info_file)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
