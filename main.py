from docx import Document


def iter_tables(table):
    for row in table.rows:
        for cell in row.cells:
            for nested_table in cell.tables:
                yield nested_table
                yield from iter_tables(nested_table)


def main():
    doc = Document('test.docx')
    # последовательность всех таблиц документа
    all_tables = doc.tables

    #print(iter_tables(all_tables))
    list_add_table = []
    for tab in all_tables:
        for n_table in iter_tables(tab):
            list_add_table.append(n_table)
            print("found a nested table %s" % n_table)

    all_tables = all_tables + list_add_table

    print(all_tables)

    print('Всего таблиц в документе:', len(all_tables))

    # создаем пустой словарь под данные таблиц
    data_tables = {i: None for i in range(len(all_tables))}
    # проходимся по таблицам
    for i, table in enumerate(all_tables):
        print('\nДанные таблицы №', i)
        # создаем список строк для таблицы `i` (пока пустые)
        data_tables[i] = [[] for _ in range(len(table.rows))]
        # проходимся по строкам таблицы `i`
        for j, row in enumerate(table.rows):
            # проходимся по ячейкам таблицы `i` и строки `j`
            for cell in row.cells:
                # добавляем значение ячейки в соответствующий
                # список, созданного словаря под данные таблиц
                data_tables[i][j].append(cell.text)

        # смотрим извлеченные данные
        # (по строкам) для таблицы `i`
        print(data_tables[i])
        print('\n')

    print('Данные всех таблиц документа:')
    print(data_tables)


if __name__ == "__main__":
    main()
