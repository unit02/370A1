#!/usr/bin/env zsh
# generated from catkin/cmake/templates/setup.zsh.in

CATKIN_SHELL=zsh
<<<<<<< HEAD

# source setup.sh from same directory as this file
_CATKIN_SETUP_DIR=$(builtin cd -q "`dirname "$0"`" > /dev/null && pwd)
emulate -R zsh -c 'source "$_CATKIN_SETUP_DIR/setup.sh"'
=======
_CATKIN_SETUP_DIR=$(builtin cd -q "`dirname "$0"`" > /dev/null && pwd)
emulate sh # emulate POSIX
. "$_CATKIN_SETUP_DIR/setup.sh"
emulate zsh # back to zsh mode
>>>>>>> f13782164eafc7b386204ed4d234628a19530598
