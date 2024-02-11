# from konspekt_package.foo import foo                            # абсолютний шлях (краще використовувати)
# from konspekt_package.baz.operation import mul, sum             # абсолютний шлях (краще використовувати)
# from konspekt_package.bar.info import log                       # абсолютний шлях (краще використовувати)
from .foo import foo                                          # відносний шлях
from .baz.operation import mul, sum                           # відносний шлях
from .bar.info import log, foo as info_foo   # використання 'as' для уникнення дублювання імен функції
from .foo import get_name_from_ordered_dict as get_value  # використання 'as' для спрощення назви функції

# __all__ = ['foo', 'mul', 'sum']  # при використанні import modul import * використовується конструкція
                                    # списку публічних об'єктів модуля, тобто приписуються функції які мають
                                    # імпортуватись (рекомендовано не використовувати)
