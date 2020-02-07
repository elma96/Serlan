#!/bin/sh
# Zeigt Inhalt der Config-Dateien
# Shell oder LUci-Backend
# Version 1.4

## Funktion:
listparam() {
    ls -1 /etc/config/
    echo -e "    Benutze <Name> als Parameter \n    oder Parameter <all>"
}


if [ "$1" = "" ]; then
    echo -e "\n    Folgende Config-Dateien gefunden:"
    listparam
    exit 0
fi

if [ "$1" = "all" ]; then
    for i in $(ls -1 /etc/config/); do
        echo -e "\n______\n### $i ###";
        cat /etc/config/$i
    done
    exit 0
fi

if [ ! -f /etc/config/$1 ]; then
    echo -e "\n    FEHLER! Datei nicht gefunden!"
    listparam
    exit 1
else
    echo -e "\n______\n### $1 ###";
    cat /etc/config/$1
fi

exit 0