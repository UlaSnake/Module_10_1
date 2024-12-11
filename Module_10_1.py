import threading  # Импортируем модуль threading для работы с потоками
from time import sleep, time  # Импортируем функции sleep и time из модуля time

def write_words(word_count, file_name):
    """
    Функция для записи word_count слов в файл file_name.
    Каждое слово записывается с задержкой 0.1 секунды.

    :param word_count: Количество слов для записи в файл.
    :param file_name: Имя файла, в который будут записываться слова.
    """
    with open(file_name, 'w', encoding='utf-8') as f:  # Открываем файл для записи с кодировкой UTF-8
        for i in range(1, word_count + 1):  # Цикл от 1 до word_count (включительно)
            f.write(f"Какое-то слово № {i}\n")  # Записываем строку в файл с номером слова
            sleep(0.1)  # Пауза на 0.1 секунды между записями
    print(f"Завершилась запись в файл {file_name}")  # Сообщаем о завершении записи в файл

# Взятие текущего времени перед выполнением функций
start_time = time()  # Сохраняем текущее время в переменной start_time

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')  # Записываем 10 слов в example1.txt
write_words(30, 'example2.txt')  # Записываем 30 слов в example2.txt
write_words(200, 'example3.txt')  # Записываем 200 слов в example3.txt
write_words(100, 'example4.txt')  # Записываем 100 слов в example4.txt

# Взятие текущего времени после выполнения функций
end_time = time()  # Сохраняем текущее время после выполнения функций
print(f"Время выполнения функций: {end_time - start_time:.6f} секунд")  # Выводим время выполнения функций

# Взятие текущего времени для потоков
start_time_threads = time()  # Сохраняем текущее время перед запуском потоков

# Создание потоков
threads = []  # Инициализируем список для хранения потоков
threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))  # Создаем поток для записи 10 слов в example5.txt
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))  # Создаем поток для записи 30 слов в example6.txt
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))  # Создаем поток для записи 200 слов в example7.txt
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))  # Создаем поток для записи 100 слов в example8.txt

# Запуск потоков
for thread in threads:  # Проходим по каждому потоку в списке threads
    thread.start()  # Запускаем поток

# Ожидание завершения всех потоков
for thread in threads:  # Проходим по каждому потоку в списке threads
    thread.join()  # Ждем завершения потока перед продолжением выполнения программы

# Взятие текущего времени после завершения потоков
end_time_threads = time()  # Сохраняем текущее время после завершения всех потоков
print(f"Время выполнения потоков: {end_time_threads - start_time_threads:.6f} секунд")  # Выводим время выполнения потоков