# Отчет о тестировании формы регистрации

## Краткое описание

Проведено тестирование формы регистрации. Выявлены две основные проблемы: ошибка при загрузке изображения в CI-среде и проблема с рекламой, перекрывающей элементы формы.

## Обнаруженные проблемы

1. Ошибка загрузки изображения в CI-среде
2. Реклама перекрывает элементы формы

## Детали проблем

### 1. Ошибка загрузки изображения

- Проблема возникает только в CI-среде
- Ошибка:
```
AssertionError: Picture /home/runner/work/SimbirSoft-SDET-TEST/SimbirSoft-SDET-TEST/images/Battlestar_Galactica.jpg was not uploaded correctly
  assert False

where False = is_picture_uploaded('/home/runner/work/SimbirSoft-SDET-TEST/SimbirSoft-SDET-TEST/images/Battlestar_Galactica.jpg')
where is_picture_uploaded = <pages.registration_page.RegistrationPage object at 0x7fe6f43cf410>.is_picture_uploaded
```
- Тест проходит локально, но не в CI
### 2. Реклама перекрывает элементы формы

- Ошибка:
```
selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element <div class=" css-2b097c-container" id="state">...</div> is not clickable at point (874, 928). Other element would receive the click: <iframe frameborder="0" src="https://deb650ba0b6ab58fc73d6b827ed15b42.safeframe.googlesyndication.com/safeframe/1-0-40/html/container.html" id="google_ads_iframe_/21849154601,22343295815/Ad.Plus-Anchor_0" title="3rd party ad content" name="" scrolling="no" marginwidth="0" marginheight="0" width="728" height="90" data-is-safeframe="true" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" allow="attribution-reporting" aria-label="Advertisement" tabindex="0" data-google-container-id="1" style="border: 0px; vertical-align: bottom;" data-load-complete="true"></iframe>
```
- Элемент формы недоступен для клика из-за рекламного баннера
- Проблема влияет на взаимодействие с элементом #state

## Рекомендации

1. Для решения проблемы с загрузкой изображения:
- Проверить права доступа к файлам в CI-среде
- Убедиться, что путь к файлу корректен в CI-окружении
- Добавить дополнительное логирование для отслеживания процесса загрузки

2. Для решения проблемы с рекламой:
- Реализовать механизм ожидания загрузки рекламы перед взаимодействием с элементами
- Использовать JavaScript для удаления или скрытия рекламного баннера перед тестированием
- Рассмотреть возможность отключения рекламы в тестовом окружении

## Заключение

Обнаруженные проблемы препятствуют успешному прохождению тестов и требуют дальнейшего исследования.