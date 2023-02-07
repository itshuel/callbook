<b>Телефонная книга</b>

Это простая книга посетителей, которую можно интегрировать к себе на сайт. Однако что она может скрывать?

Заходим на страницу, видим следующую картину:

![1](https://user-images.githubusercontent.com/64978486/217244403-520b7f5b-513b-4641-a429-087fd0c4e180.png)

Посмотрим, что мы можем сделать:

![1](https://user-images.githubusercontent.com/64978486/217244613-8955ebd7-f7e5-4c74-8bb1-f744d236e406.png)
![1](https://user-images.githubusercontent.com/64978486/217244801-946180c5-8537-4ac1-afd5-837da6e0ba42.png)

Тут нас встречает подсказка, мы ищем то, чего нет. Отправимся в терминал и попробуем заDIRBить этот сайт:

![1](https://user-images.githubusercontent.com/64978486/217245843-dad7a350-3557-4673-995e-f05f1a9016f2.png)

Видим директорию users, попробуем перейти на нее: 

![1](https://user-images.githubusercontent.com/64978486/217248189-fbd8a034-e864-4356-b3fb-26c875d360ba.png)

Попробуем что-либо ввести в нее:

![1](https://user-images.githubusercontent.com/64978486/217246244-7d799d15-c589-49a9-973b-3bc1ebcb299f.png)

Замечаем, что url изменился, попробуем посмотреть, какой пользователь скрыт под 1:

![1](https://user-images.githubusercontent.com/64978486/217246497-6a84a823-a4c5-465b-998f-927a0f83584a.png)

Это администратор! Видим цифру 88, смотрим, что там:

![1](https://user-images.githubusercontent.com/64978486/217246658-06636a7e-b783-4a15-a97a-479365ec5319.png)

Ничего интересного, однако глянем cookies:

![1](https://user-images.githubusercontent.com/64978486/217246940-b533247e-e9da-46c5-b99f-d1e3698d0cb3.png)

Меняем значение на true, обновляем страницу и получаем флаг:

![1](https://user-images.githubusercontent.com/64978486/217247814-7e21f0c7-9783-429a-9140-491d39cc9d68.png)

Флаг: <b>kvvu{c@l18ooK_M4d3_bY_DjAng0}</b>
