# 🧪Ловим alert в Selenium

### *Этот скрипт автоматизирует выполнение задачи с сайта SunInJuly , используя библиотеку Selenium.*


## 🔍 Описание функционала 

Скриптом предусмотрено выполнение следующих шагов: 

1. Открытие страницы `http://suninjuly.github.io/alert_accept.html` 
2. Нажатие alert и подтверждение всплывающего confirm.
3. Переход на страницу `http://suninjuly.github.io/alert_redirect.html?`
4. Считывание значения переменной x.
5. Вычисление математического выражения на основе x.
6. Ввод результата в поле ввода.
7. Нажатие финальной кнопки и вывод текста из alert.
     

## 📦 Требования 

1. Для запуска скрипта убедитесь, что установлена библиотека Selenium:
```bash
pip freeze | grep -i 'selenium'
```

#### Пример вывода:

```
Selenium==4.19.0
```
Если библитека не установлена, нужно её установить 😊 

``` bash
pip install selenium
``` 

2. Убедиться, что установлен драйвер браузера ChromeDriver. 


## 🚀 Как запустить 

1. Склонируйте репозиторий: 
``` bash 
git clone https://github.com/YOURNAME/Favorite-alert.git 
 ```

2. Перейдите в папку проекта: 

```bash
cd 'LOCATION_YOUR_REPOSITORY'
``` 
3. Запустите скрипт: 
``` 
    python alert.py
```  

### 📄 Пример вывода 

После выполнения скрипта в консоль будет выведен текст из последнего всплывающего окна (обычно это строка с кодом или сообщением): 
 
`Congrats! You've passed the test! Copy this code as a proof of your  achievement: XXXXXXXXXX`
   

