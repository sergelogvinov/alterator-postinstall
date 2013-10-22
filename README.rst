==========================================================
 ``alterator-postinstall`` 
==========================================================

Этот модуль для авто установки altlinux, дополнение к модулю alterator

.. note::

Пример файла autoinstall.scm
____________________________

.. code-block:: text

    ("/sysconfig-base/language" action "write" lang ("en_US"))
    ("/sysconfig-base/kbd" action "write" layout "ctrl_shift_toggle")
    ("/datetime-installer" action "write" commit #t name "RU" zone "Europe/Moscow" utc #t)
    ("/evms/control" action "write" control open installer #t)
    ("/evms/control" action "write" control update)
    ("/evms/profiles/server" action apply commit #f clearall #t exclude ())
    ("/evms/control" action "write" control commit)
    ("/evms/control" action "write" control close)
    ("/pkg-init" action "write")
    ("/pkg-install" action "write" lists "" auto #t)
    ("/preinstall" action "write")
    ("/grub" action "write" language ("en_US") device "/dev/sda")
    ("/net-eth" action "write" reset #t)
    ("/net-eth" action "write" name "eth0" configuration "dhcp")
    ("/net-eth" action "write" commit #t)
    ("/root/change_password" language ("en_US") passwd_2 "pass" passwd_1 "pass")
    ("/postinstall/firsttime" action "write" method "url" url "http://server/post.sh")
    
Шаг **/postinstall** реализуется этим модулем. Два уровня запуска:

- laststate
    Скрипт запускается при завершении альтератора (перед перезагрузкой после установки)
- firsttime
    Скрипт запускается во время первого запуска ОС

Два метода (method) указания скрипта запуска

- url 
    Данные берутся по сети с сервера
    
- conf 
    Щел скрипт указывается прям в конфиг файле

Пример использования alterator-postinstall
__________________________________________

.. code-block:: text

    ("/postinstall/firsttime" action "write" method "url" url "http://server/post.sh")
    ("/postinstall/firsttime" action "write" method "conf" cmd "curl --silent --insecure http://server/finish")

    ("/postinstall/laststate" action "write" method "url" url "http://server/alterator_finish.sh")
    ("/postinstall/laststate" action "write" method "conf" cmd "curl --silent --insecure http://server/gotoreboot")
    
