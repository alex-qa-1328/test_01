def single_root_words(root_word, *other_words):     # Создаем функцию, которая на вход принимает 1 фикс параметр
                                                    # неограниченное кол-во слов во втором параметре
    same_words=[]          # создаем пустой список с совпадающими словами
    for w in other_words:   # создаем цикл, который перебирает все слова из 2 параметра
        if root_word.lower() in w.lower() or w.lower() in root_word.lower(): # приводим все слова к нижнему регистру при сравнении
            same_words.append(w)    # если есть совпадению по первому слову, то добавляем в список
    return same_words       # возвращаем полный список с совпадающими словами

print(single_root_words('стол', 'Столешка', 'диван', 'стол-книжка', 'тумба'))

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)