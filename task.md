Цель
Создать скрипт для взаимодействия с тестовым API, демонстрирующий навыки HTTP-коммуникации и обработки данных.
Алгоритм выполнения
1.  Выполнить POST на https://test.icorp.uz/interview.php
  JSON payload с полями: msg и url
  В ответе получить первую часть кода
2.  На указанный url придет вторая часть кода
3.  Конкатенировать обе части кода
4.  Выполнить GET-запрос на тот же endpoint с объединенным кодом в параметр code
5.  Получить исходное сообщение

Требования
Вывод: Консоль или веб, показать финальное сообщение и объединенный ключ
Загрузить ответ на GitHub/GitLab с README
Бонусные очки за реализация в одном файле
Время выполнения: 2-3 дня


Create a script that interacts with a test API, demonstrating skills in HTTP communication and data processing.

Execution Algorithm

Send a POST request to https://test.icorp.uz/interview.php

 – JSON payload must include the fields: msg and url
 – The response will contain the first part of a code

The second part of the code will be sent to the specified url

Concatenate both parts of the code

Send a GET request to the same endpoint with the combined code as the code parameter

Receive the original message

Requirements
– Output: show the final message and the combined key in the console or on a web interface
– Upload the result to GitHub or GitLab with a README file
– Bonus points for implementing everything in a single file
– Completion time: 2–3 days