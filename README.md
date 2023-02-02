
Task:
Задание:
Разработать метод, на вход которого подается PDF файл (сам файл предоставляется во вложении). Нужно прочитать всю возможную информацию из файла и на выходе вернуть в виде словаря.
 Используя этот файл как эталон, разработать механизм, проверяющий входящие pdf-файлы на наличие всех элементов и соответствие структуры (расположение на листе). 

Время выполнения задания 2 календарных дня.

1) Pull this repo
2) pip install -r requirements.txt
3) Set the path to pdf file at th path_holder.py 
4) Call one of methods { get_voucher_info_as_dictionary() | checking_the_compliance_of_the_structure_with_the_requirements() }
5) Method get_voucher_info_as_dictionary() read, parse and compilates python dictionary by data from pdf
6) Method checking_the_compliance_of_the_structure_with_the_requirements() compares Yours file structure with the standarded one and gives feedback
