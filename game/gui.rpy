################################################################################
## Инициализация
################################################################################

## Оператор init offset повышает приоритет инициализации в этом файле над
## другими файлами, из-за чего инициализация здесь запускается первее.
init offset = -2

## Вызываем gui.init, чтобы сбросить стили, чувствительные к стандартным
## значениям, и задать высоту и ширину окна игры.
init python:
    gui.init(1920, 1080)

## Включить проверку на недопустимые или нестабильные свойства в экранах или
## трансформациях
define config.check_conflicting_properties = True


################################################################################
## Конфигурация переменных интерфейса
################################################################################


## Цвета #######################################################################
##
## Цвета текста в интерфейсе.

## Акцентный цвет используется в заголовках и для выделения текста.
define gui.accent_color = '#c94a4a'

## Цвет, используемый в текстовой кнопке, когда она не выбрана и не наведена.
define gui.idle_color = '#b6c5cf'

## Цвет, используемый в мелком тексте, который должен быть ярче/темнее, чтобы
## оставаться заметным.
define gui.idle_small_color = '#6c7a86'

## Цвет, используемый в кнопках и панелях, когда они наведены.
define gui.hover_color = '#ffffff'

## Цвет, используемый в текстовой кнопке, когда она выбрана, но не наведена.
## Кнопка может быть выбрана, если таково значение в текущем экране или в
## настройках.
define gui.selected_color = '#ffffff'

## Цвет, используемый в текстовой кнопке, когда она не может быть выбрана.
define gui.insensitive_color = '#8888887f'

## Цвета, используемые для незаполненных частей панелей. Они не используются
## напрямую, а только при повторной генерации файлов изображений панели.
define gui.muted_color = '#4a5056'
define gui.hover_muted_color = '#005b7a'

## Цвета, используемые в тексте диалогов и меню выбора.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Шрифты и их размеры #########################################################

## Шрифт для внутриигрового текста.
define gui.text_font = "Georgia.ttf"

## Шрифт для имён персонажей.
define gui.name_text_font = "Georgia.ttf"

## Шрифт для текста вне игры.
define gui.interface_text_font = "DejaVuSans.ttf"

## Размер нормального текста диалога.
define gui.text_size = 31
define gui.text_outlines = [ (2, "#000000cc", 1, 1) ]

## Размер текста для имён персонажей.
define gui.name_text_size = 38
define gui.name_text_outlines = [ (2, "#000000ee", 1, 1) ]
define gui.interface_text_size = 33
define gui.label_text_size = 36

## Размер текста на экране уведомлений.
define gui.notify_text_size = 24

## Размер заголовка игры.
define gui.title_text_size = 75


## Главное и игровое меню ######################################################

## Изображения, используемые в главном и игровом меню.
define gui.main_menu_background = im.Scale("images/bg_main_menu.jpg", 1920, 1080)
define gui.game_menu_background = "gui/game_menu.png"


## Диалог ######################################################################
##
## Эти переменные контролируют отображение реплик диалога на экране.

## Высота текстового окна, содержащего диалог.
define gui.textbox_height = 278

## Положение текстового окна по вертикали экрана. 0.0 — верх, 0.5 — центр и 1.0
## — низ.
define gui.textbox_yalign = 1.0


## Положение имени говорящего персонажа по отношению к текстовому окну. Это
## могут быть целые числа в пикселях слева и сверху, или дробные, например, 0.5
## для центрирования.
define gui.name_xpos = 360
define gui.name_ypos = 0

## Горизонтальное выравнивание имени персонажа. Это может быть 0.0 для
## выравнивания по левому краю, 0.5 — по центру и 1.0 — по правому краю.
define gui.name_xalign = 0.0

## Ширина, высота и границы окна, содержащего имя персонажа, или None для
## автоматического определения размера.
define gui.namebox_width = None
define gui.namebox_height = None

## Границы окна, содержащего имя персонажа в порядке слева, сверху, справа и
## снизу.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Если True, фон окна с именем будет повторятся плиткой. Если False, фон окна
## будет растягиваться.
define gui.namebox_tile = False


## Положение диалога по отношению к текстовому окну. Это могут быть целые числа
## в пикселях от левой и верхней стороны текстового окна, или дробные, например,
## 0.5 для центрирования.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## Максимальная ширина текста диалога в пикселях.
define gui.dialogue_width = 1116

## Горизонтальное выравнивание текста диалога. Это может быть 0.0 для
## выравнивания по левому краю, 0.5 — по центру и 1.0 — по правому краю.
define gui.dialogue_text_xalign = 0.0


## Кнопки ######################################################################
##
## Эти переменные, вместе с изображениями в gui/button, контролируют как будут
## отображаться кнопки.

## Ширина и высота кнопки в пикселях. Если None, Ren'Py самостоятельно
## рассчитает размер.
define gui.button_width = None
define gui.button_height = None

## Границы каждой стороны кнопки в порядке слева, сверху, справа, снизу.
define gui.button_borders = Borders(6, 6, 6, 6)

## Если True, фоновое изображение будет повторятся плиткой. Если False, фон
## будет линейно растягиваться.
define gui.button_tile = False

## Шрифт, используемый кнопкой.
define gui.button_text_font = gui.interface_text_font

## Размер текста, используемый кнопкой.
define gui.button_text_size = gui.interface_text_size

## Цвет текста в кнопке в различных состояниях.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Горизонтальное выравнивание текста в кнопке. (0.0 — слева, 0.5 — по центру,
## 1.0 — справа).
define gui.button_text_xalign = 0.0


## Эти переменные переопределяют настройки различных кнопок. Пожалуйста,
## посмотрите документацию по GUI для просмотра всех видов кнопок и для чего
## каждая из них нужна.
##
## Эти настройки используются стандартным интерфейсом:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Вы также можете добавить собственные настройки, добавляя правильно
## именованные переменные. Например, вы можете раскомментировать следующую
## строчку, чтобы установить ширину кнопок навигации.

# define gui.navigation_button_width = 250


## Кнопки выбора ###############################################################
##
## Кнопки выбора используются во внутриигровых меню.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 14, 150, 14)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Кнопки слотов сохранений ####################################################
##
## Кнопка слотов — особый вид кнопки. Она содержит миниатюру и текст,
## описывающий слот сохранения. Слот сохранения использует файлы из gui/button,
## как и другие виды кнопок.

## Кнопка слота сохранения.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Ширина и высота миниатюры, используемой слотом сохранения.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Количество колонок и рядов в таблице слотов.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Позиционирование и интервалы ################################################
##
## Эти переменные контролируют позиционирование и интервалы различных элементов
## пользовательского интерфейса.

## Положение левого края кнопок навигации относительно левого края экрана.
define gui.navigation_xpos = 60

## Вертикальная позиция индикатора пропуска.
define gui.skip_ypos = 15

## Вертикальная позиция экрана уведомлений.
define gui.notify_ypos = 68

## Интервал между выборами в меню.
define gui.choice_spacing = 33

## Кнопки в секции навигации главного и игрового меню.
define gui.navigation_spacing = 6

## Контролирует интервал между настройками.
define gui.pref_spacing = 15

## Контролирует интервал между кнопками настройки.
define gui.pref_button_spacing = 0

## Интервал между кнопками страниц сохранений.
define gui.page_spacing = 0

## Интервал между слотами сохранений.
define gui.slot_spacing = 15

## Позиция текста главного меню.
define gui.main_menu_text_xalign = 1.0


## Рамки #######################################################################
##
## Эти переменные управляют внешним видом рамок, которые могут содержать
## элементы интерфейса, когда отсутствует оверлей или окно.

## Обычные рамки.
define gui.frame_borders = Borders(6, 6, 6, 6)

## Рамка, используемая в экране подтверждения.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Рамка, используемая в экране пропуска.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Рамка, используемая в экране уведомлений.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Должен ли фон рамок повторятся плиткой?
define gui.frame_tile = False


## Панели, полосы прокрутки и ползунки #########################################
##
## Эти настройки контролируют вид и размер панелей, полос прокрутки и ползунков.
##
## Стандартный интерфейс использует только ползунки и вертикальные полосы
## прокрутки. Все остальные панели используются только авторами в собственных
## экранах.

## Высота горизонтальных панелей, полос прокрутки и ползунков. Ширина
## вертикальных панелей, полос прокрутки и ползунков.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## Если True, фон панелей будет повторятся плиткой. Если False, фон будет
## линейно растягиваться.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Горизонтальные границы.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Вертикальные границы.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## Что делать с непрокручиваемыми полосами прокрутки в игровом меню. "hide"
## прячет их, а None их показывает.
define gui.unscrollable = "hide"


## История #####################################################################
##
## Экран истории показывает диалог, который игрок уже прошёл.

## Количество блоков истории диалога, которые Ren'Py будет хранить.
define config.history_length = 250

## Высота сообщений на экране истории. None, чтобы ценой производительности
## высота просчитывалась автоматически.
define gui.history_height = 210

## Дополнительное пространство между сообщениями на экране истории.
define gui.history_spacing = 0

## Положение, ширина и выравнивание заголовка с именем говорящего персонажа.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Положение, ширина и выравнивание текста диалога.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## Режим NVL ###################################################################
##
## Экран режима NVL показывает диалог NVL-персонажей.

## Границы фона окна NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Максимальное число показываемых сообщений в режиме NVL. Когда количество
## сообщений превышает это значение, старые сообщения будут удалены.
define gui.nvl_list_length = 6

## Высота сообщений в режиме NVL. Установите на None, чтобы сообщения
## автоматически рассчитывали свою высоту.
define gui.nvl_height = 173

## Интервал между сообщениями в режиме NVL, если gui.nvl_height равно None. А
## также интервал от сообщений до меню в режиме NVL.
define gui.nvl_spacing = 15

## Положение, ширина и выравнивание заголовка с именем говорящего персонажа.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Положение, ширина и выравнивание текста диалога.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## Положение, ширина и выравнивание текста nvl_thought (текст от лица персонажа
## nvl_narrator).
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## Положение кнопок меню NVL.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Локализация #################################################################

## Эта настройка контролирует где доступен разрыв строки. Стандартное значение
## подходит для большинства языков. Список доступных значений можно найти на
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Мобильные устройства
################################################################################

init python:

    ## Увеличивает размер быстрых кнопок, чтобы сделать их доступнее для нажатия
    ## на планшетах и телефонах.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Изменяет размеры и интервалы различных элементов интерфейса, чтобы они
    ## были лучше видны на телефонах.
    @gui.variant
    def small():

        ## Размеры шрифтов.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Регулирует положение текстового окна.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Изменяет размеры и интервалы различных объектов.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Таблица слотов сохранений.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Режим NVL.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
