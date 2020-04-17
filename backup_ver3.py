import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\My Documents"', 'C:\\Code']

# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.

target_dir = 'D:\\Python\\backup' # Подставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
current_time = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем, введён ли комментарий
    target = today + os.sep + current_time + '.zip'
else:
    target = today + os.sep + current_time + '_' + comment.replace(' ', '_') + '.zip'

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today)
    print('Новый каталог\'{0}\' создан'.format(today))

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
