import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://neal.fun/spend/'

        super().__init__(web_driver, url)


    btn_headers_logo = WebElement(xpath='//a[@class="header-site-link nuxt-link-active"]')#лого в хэдере
    txt_headers_title = WebElement(xpath='//div[@class="title"]')#текст титл хэдера
    txt_headers_money = WebElement(xpath='//div[@class="money-bar"]')#сумма в хэдере

    btn_footer_logo = WebElement(xpath='//a[@class="nuxt-link-active"]')  #лого в футере
    inp_footer_email = WebElement(xpath='//input[@class="newsletter-input"]') #строка емаила в футере
    str_footer_thx = WebElement(xpath='//div[@class="newsletter-text"]') #надпись после нажатия на кнопку сабскрайб
    btn_footer_subscribe = WebElement(xpath='//button[@class="newsletter-subscribe"]')  # кнопка сабскарйб в футере

    str_footer_also = WebElement(xpath="//div[@class='related-text']")  # надпись после нажатия на кнопку сабскрайб
    link_footer_first = WebElement(xpath='(//a[@data-v-cf9a47ea])[1]') #первая линка в футере
    link_footer_second = WebElement(xpath='(//a[@data-v-cf9a47ea])[2]') #вторая линка в футере
    link_footer_third = WebElement(xpath='(//a[@data-v-cf9a47ea])[3]')  # третья линка в футере
    link_footer_fourth = WebElement(xpath='(//a[@data-v-cf9a47ea])[4]')  # четвертая линка в футере

    button_body_mac_sell = WebElement(xpath='(//*[@id="__layout"]//button)[1]')  # кнопка продажи бигмака
    button_body_mac_buy = WebElement(xpath='(//*[@id="__layout"]//button)[2]') #кнопка покупки бигмака
    button_body_flops_sell= WebElement(xpath='(//*[@id="__layout"]//button)[3]')  # кнопка продажи тапок
    button_body_flops_buy = WebElement(xpath='(//*[@id="__layout"]//button)[4]')  # кнопка покубки тапок
    button_body_cola_sell = WebElement(xpath='(//*[@id="__layout"]//button)[5]')  # кнопка продажи колы
    button_body_cola_buy = WebElement(xpath='(//*[@id="__layout"]//button)[6]')  # кнопка покубки колы
    button_body_ticket_sell = WebElement(xpath='(//*[@id="__layout"]//button)[7]')  # кнопка продажи биллета
    button_body_ticket_buy = WebElement(xpath='(//*[@id="__layout"]//button)[8]')  # кнопка покубки биллета
    button_body_book_sell = WebElement(xpath='(//*[@id="__layout"]//button)[9]')  # кнопка продажи книги
    button_body_book_buy = WebElement(xpath='(//*[@id="__layout"]//button)[10]')  # кнопка покупки книги
    button_body_lobster_sell = WebElement(xpath='(//*[@id="__layout"]//button)[11]')  # кнопка продажи лобстера
    button_body_lobster_buy = WebElement(xpath='(//*[@id="__layout"]//button)[12]')  # кнопка покупки лобстера
    button_body_game_sell = WebElement(xpath='(//*[@id="__layout"]//button)[13]')  # кнопка продажи игры
    button_body_game_buy = WebElement(xpath='(//*[@id="__layout"]//button)[14]')  # кнопка покубки игры
    button_body_echo_sell = WebElement(xpath='(//*[@id="__layout"]//button)[15]')  # кнопка продажи колонки
    button_body_echo_buy = WebElement(xpath='(//*[@id="__layout"]//button)[16]')  # кнопка покубки колонки
    button_body_netflix_sell = WebElement(xpath='(//*[@id="__layout"]//button)[17]')  # кнопка продажи подписки нетфликс
    button_body_netflix = WebElement(xpath='(//*[@id="__layout"]//button)[18]')  # кнопка покупки подписки нетфликс
    button_body_jordans_sell = WebElement(xpath='(//*[@id="__layout"]//button)[19]')  # кнопка продажи джорданов
    button_body_jordans_buy = WebElement(xpath='(//*[@id="__layout"]//button)[20]')  # кнопка покупки джорданов
    button_body_airpods_sell = WebElement(xpath='(//*[@id="__layout"]//button)[21]')  # кнопка продажи аирподсов
    button_body_airpods = WebElement(xpath='(//*[@id="__layout"]//button)[22]')  # кнопка покупки аирподсов
    button_body_console_sell = WebElement(xpath='(//*[@id="__layout"]//button)[23]')  # кнопка продажи консоли
    button_body_console_buy = WebElement(xpath='(//*[@id="__layout"]//button)[24]')  # кнопка покупки консоли
    button_body_drone_sell = WebElement(xpath='(//*[@id="__layout"]//button)[25]')  # кнопка продажи дрона
    button_body_drone_buy = WebElement(xpath='(//*[@id="__layout"]//button)[26]')  # кнопка покупки дрона
    button_body_smartphone_sell = WebElement(xpath='(//*[@id="__layout"]//button)[27]')  # кнопка продажи смартфона
    button_body_smartphone_buy = WebElement(xpath='(//*[@id="__layout"]//button)[28]')  # кнопка покупки смартфона
    button_body_bike_sell = WebElement(xpath='(//*[@id="__layout"]//button)[29]')  # кнопка продажи велосипеда
    button_body_bike_buy = WebElement(xpath='(//*[@id="__layout"]//button)[30]')  # кнопка покупки велосипеда
    button_body_kitten_sell = WebElement(xpath='(//*[@id="__layout"]//button)[31]')  # кнопка продажи котенка
    button_body_kitten_buy = WebElement(xpath='(//*[@id="__layout"]//button)[32]')  # кнопка покупки котенка
    button_body_puppy_sell = WebElement(xpath='(//*[@id="__layout"]//button)[33]')  # кнопка продажи щенка
    button_body_puppy_buy = WebElement(xpath='(//*[@id="__layout"]//button)[34]')  # кнопка покупки щенка
    button_body_rickshaw_sell = WebElement(xpath='(//*[@id="__layout"]//button)[35]')  # кнопка продажи тележки
    button_body_rickshaw_buy = WebElement(xpath='(//*[@id="__layout"]//button)[36]')  # кнопка покупки тележки
    button_body_horse_sell = WebElement(xpath='(//*[@id="__layout"]//button)[37]')  # кнопка продажи коня
    button_body_horse_buy = WebElement(xpath='(//*[@id="__layout"]//button)[38]')  # кнопка покупки коня
    button_body_acre_sell = WebElement(xpath='(//*[@id="__layout"]//button)[39]')  # кнопка продажи акра территории
    button_body_acre_buy = WebElement(xpath='(//*[@id="__layout"]//button)[40]')  # кнопка покупки территории
    button_body_handbag_sell = WebElement(xpath='(//*[@id="__layout"]//button)[41]')  # кнопка продажи сумочки
    button_body_handbag_buy = WebElement(xpath='(//*[@id="__layout"]//button)[42]')  # кнопка покупки сумочки
    button_body_hottub_sell = WebElement(xpath='(//*[@id="__layout"]//button)[43]')  # кнопка продажи джакузи
    button_body_hottub_buy = WebElement(xpath='(//*[@id="__layout"]//button)[44]')  # кнопка покупки джакузи
    button_body_wine_sell = WebElement(xpath='(//*[@id="__layout"]//button)[45]')  # кнопка продажи вина
    button_body_wine_buy = WebElement(xpath='(//*[@id="__layout"]//button)[46]')  # кнопка покупки вина
    button_body_ring_sell = WebElement(xpath='(//*[@id="__layout"]//button)[47]')  # кнопка продажи кольца
    button_body_ring_buy = WebElement(xpath='(//*[@id="__layout"]//button)[48]')  # кнопка покупки кольца
    button_body_jet_ski_sell = WebElement(xpath='(//*[@id="__layout"]//button)[49]')  # кнопка продажи гидроцикла
    button_body_jet_ski_buy = WebElement(xpath='(//*[@id="__layout"]//button)[50]')  # кнопка покупки гидроцикла
    button_body_rolex_sell = WebElement(xpath='(//*[@id="__layout"]//button)[51]')  # кнопка продажи ролексов
    button_body_rolex_buy = WebElement(xpath='(//*[@id="__layout"]//button)[52]')  # кнопка покупки ролексов
    button_body_ford_sell = WebElement(xpath='(//*[@id="__layout"]//button)[53]')  # кнопка продажи форда
    button_body_ford_buy = WebElement(xpath='(//*[@id="__layout"]//button)[54]')  # кнопка покупки форда
    button_body_tesla_sell = WebElement(xpath='(//*[@id="__layout"]//button)[55]')  # кнопка продажи теслы
    button_body_tesla_buy = WebElement(xpath='(//*[@id="__layout"]//button)[56]')  # кнопка покупки теслы
    button_body_truck_sell = WebElement(xpath='(//*[@id="__layout"]//button)[57]')  # кнопка продажи трака
    button_body_truck_buy = WebElement(xpath='(//*[@id="__layout"]//button)[58]')  # кнопка покупки трака
    button_body_ferrari_sell = WebElement(xpath='(//*[@id="__layout"]//button)[59]')  # кнопка продажи ферари
    button_body_ferrari_buy = WebElement(xpath='(//*[@id="__layout"]//button)[60]')  # кнопка покупки ферари
    button_body_home_sell = WebElement(xpath='(//*[@id="__layout"]//button)[61]')  # кнопка продажи дома
    button_body_home_buy = WebElement(xpath='(//*[@id="__layout"]//button)[62]')  # кнопка покупки дома
    button_body_gold_sell = WebElement(xpath='(//*[@id="__layout"]//button)[63]')  # кнопка продажи золота
    button_body_gold_buy = WebElement(xpath='(//*[@id="__layout"]//button)[64]')  # кнопка покупки золота
    button_body_mc_franchise_sell = WebElement(xpath='(//*[@id="__layout"]//button)[65]')  # кнопка продажи франшизы
    button_body_mc_franchise_buy = WebElement(xpath='(//*[@id="__layout"]//button)[66]')  # кнопка покупки франшизы
    button_body_superbowl_sell = WebElement(xpath='(//*[@id="__layout"]//button)[67]')  # кнопка продажи супербоула
    button_body_superbowl_buy = WebElement(xpath='(//*[@id="__layout"]//button)[68]')  # кнопка покупки супербоула
    button_body_yacht_sell = WebElement(xpath='(//*[@id="__layout"]//button)[69]')  # кнопка продажи яхты
    button_body_yacht_buy = WebElement(xpath='(//*[@id="__layout"]//button)[70]')  # кнопка покупки яхты
    button_body_abrams_sell = WebElement(xpath='(//*[@id="__layout"]//button)[71]')  # кнопка продажи танка
    button_body_abrams_buy = WebElement(xpath='(//*[@id="__layout"]//button)[72]')  # кнопка покупки танка
    button_body_f1_sell = WebElement(xpath='(//*[@id="__layout"]//button)[73]')  # кнопка продажи формулы1
    button_body_f1_buy = WebElement(xpath='(//*[@id="__layout"]//button)[74]')  # кнопка покупки формулы1
    button_body_apache_sell = WebElement(xpath='(//*[@id="__layout"]//button)[75]')  # кнопка продажи вертолета
    button_body_apache_buy = WebElement(xpath='(//*[@id="__layout"]//button)[76]')  # кнопка покупки вертолета
    button_body_mansion_sell = WebElement(xpath='(//*[@id="__layout"]//button)[77]')  # кнопка продажи поместья
    button_body_mansion_buy = WebElement(xpath='(//*[@id="__layout"]//button)[78]')  # кнопка покупки поместья
    button_body_movie_sell = WebElement(xpath='(//*[@id="__layout"]//button)[79]')  # кнопка продажи фильма
    button_body_movie_buy = WebElement(xpath='(//*[@id="__layout"]//button)[80]')  # кнопка покупки фильма
    button_body_boeing_sell = WebElement(xpath='(//*[@id="__layout"]//button)[81]')  # кнопка продажи боинга
    button_body_boeing_buy = WebElement(xpath='(//*[@id="__layout"]//button)[82]')  # кнопка покупки боинга
    button_body_monalisa_sell = WebElement(xpath='(//*[@id="__layout"]//button)[83]')  # кнопка продажи монализы
    button_body_monalisa_buy = WebElement(xpath='(//*[@id="__layout"]//button)[84]')  # кнопка покупки монализы
    button_body_skyscraper_sell = WebElement(xpath='(//*[@id="__layout"]//button)[85]')  # кнопка продажи высотки
    button_body_skyscraper_buy = WebElement(xpath='(//*[@id="__layout"]//button)[86]')  # кнопка покупки высотки
    button_body_cruise_sell = WebElement(xpath='(//*[@id="__layout"]//button)[87]')  # кнопка продажи лайнера
    button_body_cruise_buy = WebElement(xpath='(//*[@id="__layout"]//button)[88]')  # кнопка покупки лайнера
    button_body_nba_sell = WebElement(xpath='(//*[@id="__layout"]//button)[89]')  # кнопка продажи команды нба
    button_body_nba_buy = WebElement(xpath='(//*[@id="__layout"]//button)[90]')  # кнопка покупки команды нба


    inp_body_mac_count = WebElement(xpath='(//*[@pattern="\d*"])[1]')  # строка ввода кол-ва бургеров
    inp_body_flops_count = WebElement(xpath='(//*[@pattern="\d*"])[2]')  # строка ввода кол-ва тапок
    inp_body_cola_count = WebElement(xpath='(//*[@pattern="\d*"])[3]')  # строка ввода кол-ва колы
    inp_body_ticket_count = WebElement(xpath='(//*[@pattern="\d*"])[4]')  # строка ввода кол-ва билетов
    inp_body_book_count = WebElement(xpath='(//*[@pattern="\d*"])[5]')  # строка ввода кол-ва книг
    inp_body_lobster_count = WebElement(xpath='(//*[@pattern="\d*"])[6]')  # строка ввода кол-ва лобстера
    inp_body_game_count = WebElement(xpath='(//*[@pattern="\d*"])[7]')  # строка ввода кол-ва игры
    inp_body_echo_count = WebElement(xpath='(//*[@pattern="\d*"])[8]')  # строка ввода кол-ва колонки
    inp_body_netflix_count = WebElement(xpath='(//*[@pattern="\d*"])[9]')  # строка ввода кол-ва подписки нетфликс
    inp_body_jordans_count = WebElement(xpath='(//*[@pattern="\d*"])[10]')  # строка ввода кол-ва джорданов
    inp_body_airpods_count = WebElement(xpath='(//*[@pattern="\d*"])[11]')  # строка ввода кол-ва аирподсов
    inp_body_console_count = WebElement(xpath='(//*[@pattern="\d*"])[12]')  # строка ввода кол-ва консоли
    inp_body_drone_count = WebElement(xpath='(//*[@pattern="\d*"])[13]')  # строка ввода кол-ва дрона
    inp_body_smartphone_count = WebElement(xpath='(//*[@pattern="\d*"])[14]')  # строка ввода кол-ва смартфона
    inp_body_bike_count = WebElement(xpath='(//*[@pattern="\d*"])[15]')  # строка ввода кол-ва велосипеда
    inp_body_kitten_count = WebElement(xpath='(//*[@pattern="\d*"])[16]')  # строка ввода кол-ва кошки
    inp_body_puppy_count = WebElement(xpath='(//*[@pattern="\d*"])[17]')  # строка ввода кол-ва щенка
    inp_body_rickshaw_count = WebElement(xpath='(//*[@pattern="\d*"])[18]')  # строка ввода кол-ва тележки
    inp_body_horse_count = WebElement(xpath='(//*[@pattern="\d*"])[19]')  # строка ввода кол-ва коня
    inp_body_acre_count = WebElement(xpath='(//*[@pattern="\d*"])[20]')  # строка ввода кол-ва акра территории
    inp_body_handbag_count = WebElement(xpath='(//*[@pattern="\d*"])[21]')  # строка ввода кол-ва сумочки
    inp_body_tub_count = WebElement(xpath='(//*[@pattern="\d*"])[22]')  # строка ввода кол-ва джакузи
    inp_body_wine_count = WebElement(xpath='(//*[@pattern="\d*"])[23]')  # строка ввода кол-ва вина
    inp_body_ring_count = WebElement(xpath='(//*[@pattern="\d*"])[24]')  # строка ввода кол-ва кольца
    inp_body_ski_count = WebElement(xpath='(//*[@pattern="\d*"])[25]')  # строка ввода кол-ва гидроцикла
    inp_body_rolex_count = WebElement(xpath='(//*[@pattern="\d*"])[26]')  # строка ввода кол-ва ролексов
    inp_body_ford_count = WebElement(xpath='(//*[@pattern="\d*"])[27]')  # строка ввода кол-ва форда
    inp_body_tesla_count = WebElement(xpath='(//*[@pattern="\d*"])[28]')  # строка ввода кол-ва теслы
    inp_body_truck_count = WebElement(xpath='(//*[@pattern="\d*"])[29]')  # строка ввода кол-ва трака
    inp_body_ferrari_count = WebElement(xpath='(//*[@pattern="\d*"])[30]')  # строка ввода кол-ва ферари
    inp_body_home_count = WebElement(xpath='(//*[@pattern="\d*"])[31]')  # строка ввода кол-ва дома
    inp_body_gold_count = WebElement(xpath='(//*[@pattern="\d*"])[32]')  # строка ввода кол-ва золота
    inp_body_franchise_count = WebElement(xpath='(//*[@pattern="\d*"])[33]')  # строка ввода кол-ва франшизы
    inp_body_superbowl_count = WebElement(xpath='(//*[@pattern="\d*"])[34]')  # строка ввода кол-ва супербоула
    inp_body_yacht_count = WebElement(xpath='(//*[@pattern="\d*"])[35]')  # строка ввода кол-ва яхты
    inp_body_abrams_count = WebElement(xpath='(//*[@pattern="\d*"])[36]')  # строка ввода кол-ва танка
    inp_body_formula_count = WebElement(xpath='(//*[@pattern="\d*"])[37]')  # строка ввода кол-ва формулы1
    inp_body_apache_count = WebElement(xpath='(//*[@pattern="\d*"])[38]')  # строка ввода кол-ва вертолета
    inp_body_mansion_count = WebElement(xpath='(//*[@pattern="\d*"])[39]')  # строка ввода кол-ва поместья
    inp_body_movie_count = WebElement(xpath='(//*[@pattern="\d*"])[40]')  # строка ввода кол-ва фильмов
    inp_body_boeing_count = WebElement(xpath='(//*[@pattern="\d*"])[41]')  # строка ввода кол-ва боинга
    inp_body_monalisa_count = WebElement(xpath='(//*[@pattern="\d*"])[42]')  # строка ввода кол-ва картины
    inp_body_skyscraper_count = WebElement(xpath='(//*[@pattern="\d*"])[43]')  # строка ввода кол-ва высотки
    inp_body_ship_count = WebElement(xpath='(//*[@pattern="\d*"])[44]')  # строка ввода кол-ва лайнера
    inp_body_nba_count = WebElement(xpath='(//*[@pattern="\d*"])[45]')  # строка ввода кол-ва команды нба

    name_body_mac = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[1]')
    name_body_flops = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[2]')
    name_body_cola = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[3]')
    name_body_ticket = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[4]')
    name_body_book = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[5]')
    name_body_lobster = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[6]')
    name_body_game = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[7]')
    name_body_echo = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[8]')
    name_body_netflix = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[9]')
    name_body_jordans = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[10]')
    name_body_airpods = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[11]')
    name_body_console = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[12]')
    name_body_drone = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[13]')
    name_body_smartphone = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[14]')
    name_body_bike = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[15]')
    name_body_kitten = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[16]')
    name_body_puppy = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[17]')
    name_body_rickshaw = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[18]')
    name_body_horse = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[19]')
    name_body_acre = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[20]')
    name_body_handbag = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[21]')
    name_body_tub = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[22]')
    name_body_wine = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[23]')
    name_body_ring = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[24]')
    name_body_ski = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[25]')
    name_body_rolex = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[26]')
    name_body_ford = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[27]')
    name_body_tesla = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[28]')
    name_body_truck = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[29]')
    name_body_ferrari = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[30]')
    name_body_home = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[31]')
    name_body_gold = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[32]')
    name_body_ranchise = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[33]')
    name_body_superbowl = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[34]')
    name_body_yacht = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[35]')
    name_body_abrams = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[36]')
    name_body_formula_1 = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[37]')
    name_body_helicopter = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[38]')
    name_body_mansion = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[39]')
    name_body_movie = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[40]')
    name_body_boeing = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[41]')
    name_body_mona_lisa = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[42]')
    name_body_skyscraper = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[43]')
    name_body_cruise = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[44]')
    name_body_nba = WebElement(xpath='(//*[contains(concat(' ', normalize-space(@class), ' '), "item-name")])[45]')


    cost_body_mac = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[1]")
    cost_body_flops = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[2]")
    cost_body_cola = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[3]")
    cost_body_ticket = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[4]")
    cost_body_book = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[5]")
    cost_body_lobster = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[6]")
    cost_body_game = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[7]")
    cost_body_echo = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[8]")
    cost_body_netflix = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[9]")
    cost_body_jordans = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[10]")
    cost_body_airpods = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[11]")
    cost_body_console = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[12]")
    cost_body_drone = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[13]")
    cost_body_smartphone = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[14]")
    cost_body_bike = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[15]")
    cost_body_kitten = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[16]")
    cost_body_puppy = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[17]")
    cost_body_rickshaw = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[18]")
    cost_body_horse = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[19]")
    cost_body_acre = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[20]")
    cost_body_handbag = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[21]")
    cost_body_tub = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[22]")
    cost_body_wine = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[23]")
    cost_body_ring = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[24]")
    cost_body_ski = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[25]")
    cost_body_rolex = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[26]")
    cost_body_ford = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[27]")
    cost_body_tesla = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[28]")
    cost_body_truck = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[29]")
    cost_body_ferrari = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[30]")
    cost_body_home = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[31]")
    cost_body_gold = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[32]")
    cost_body_franchise = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[33]")
    cost_body_superbowl = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[34]")
    cost_body_yacht = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[35]")
    cost_body_abrams = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[36]")
    cost_body_formula_1 = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[37]")
    cost_body_apache = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[38]")
    cost_body_mansion = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[39]")
    cost_body_movie = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[40]")
    cost_body_boeing = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[41]")
    cost_body_mona_lisa = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[42]")
    cost_body_skyscraper = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost')])[43]")
    cost_body_cruise = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '),'item-cost'])[44]")
    cost_body_nba = WebElement(xpath="(//*[contains(concat(' ', normalize-space(@class), ' '), 'item-cost'])[45]")







