from django.urls import path
from book import views

urlpatterns = [
    path('', views.domov, name='domov'),
    path('obsah', views.obsah, name='obsah'),
    path('internet-zaklad-novodobeho-zivota', views.one, name='one'),
    path('digitalizacia-ludstva', views.two, name='two'),
    path('kyberneticka-bezpecnost', views.two_one, name='two_one'),
    path('kyberneticke-utoky', views.two_two, name='two_two'),
    path('hrozby-internetu', views.three, name='three'),
    path('bezpecne-pouzivanie-internetu', views.three_one, name='three_one'),
    path('tvorba-hesla', views.three_one_one, name='three_one_one'),
    path('ukladanie-hesla', views.three_one_two, name='three_one_two'),
    path('verejne-siete-wifi', views.three_one_three, name='three_one_three'),
    path('socialne-siete', views.three_two, name='three_two'),
    path('tipy-k-bezpecnemu-pouzivaniu-socialnych-sieti', views.three_two_one, name='three_two_one'),
    path('pocitacove-virusy-a-spam', views.three_three, name='three_three'),
    path('najbeznejsie-typy-pocitacovych-virusov', views.three_three_one, name='three_three_one'),
    path('mylne-predstavy-o-pocitacovych-virusoch', views.three_three_two, name='three_three_two'),
    path('ako-nedostat-pocitacovy-virus', views.three_three_three, name='three_three_three'),
    path('ako-identifikovat-a-zneskodnit-pocitacovy-virus', views.three_three_four, name='three_three_four'),
    path('spam', views.three_four, name='three_four'),
    path('phishing', views.three_four_one, name='three_four_one'),
    path('ako-sa-branit-proti-spamu-a-phishingu', views.three_four_two, name='three_four_two'),
    path('socialne-inzinierstvo', views.three_four_three, name='three_four_three'),
    path('netiketa', views.four, name='four'),
    path('kybersikana', views.four_one, name='four_one'),
    path('ako-sa-kybersikane-vyvarovat-a-branit', views.four_one_one, name='four_one_one'),
    path('dvojjazycny-vykladovy-slovnik-pouzitych-pojmov', views.five, name='five'),
    path('zoznam-pouzitych-zdrojov', views.zoznam_pouzitych_zdrojov, name='zoznam_pouzitych_zdrojov'),
    path('test1', views.test1, name='test1'),
    path('test2', views.test2, name='test2'),
    path('test3', views.test3, name='test3'),
]
