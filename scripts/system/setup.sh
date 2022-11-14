#!/usr/bin/env bash

FAIL="\033[1;31m[ FAIL ]\033[0m"
SUCCESS="\033[1;32m[ PASS ]\033[0m"
PROC="\033[1;36m[ PROC ]\033[0m"

sudo dnf update -y

function install_deps () {
    for i in $(seq 1 3); do
        if [ -f sysdeps.txt ]; then
            xargs sudo dnf install -y <sysdeps.txt
        else
            # only the base
            sudo dnf install -y \
                python3.10
                python3-pip
                libX11-devel
                libXft-devel
                libXinerama-devel
                libXrandr-devel
                libXScrnSaver-devel
                xmonad
                xmonad-contrib
                ghc-xmonad*
                lightdm
        fi

        if [ $? -eq 0 ]; then
            echo -e "$SUCCESS Proceeding to next process ..."
            break
        else
            echo -e "$FAIL Retrying. Attempts left: $i, ..."
        fi
    done
}

function setup_services () {
    declare -a Services=("index", "meow")
    echo "" > missing.lists # clear previous list, if there exists one

    for service in "${Services[@]}"; do
        if [ ! -f system/services/$service ] && [ ! -f system/tasks/$service ]; then
            echo -e "$FAIL $service not found, skipping ..."
            echo $service >> missing.lists
        fi
    done

    cat missing.lists | while read line; do
        case $line in
            index)
                wget #link;;
        esac
    done
}
