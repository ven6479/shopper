# test
1) Добавил записи в модели
2) Создал автоматическое заполнения поля slug для Product
2) Создал специальное поле для фотографий чтобы конвертировать файла в webp, более подробно в папке fields
3) Создал точку апи для получения всех товаров,
5) В точке добавил фильтрацию по статусу
6) Добавил поиск по артиклю и названию
7) Изменил вывод api у фотографий (путь получил, довольно костыльным способом, в бд поподал относительный путь, в api выводился путь с протоколом)
8) Добавил точку для получения конкретного товара по id (изначально хотел по slug, но подумал, что по id будет лучше)
9) Добавил тесты api
10) Добавил тесты сериализаторов

#Загруженная фотография сразу сохраняется с форматом webp в бд
