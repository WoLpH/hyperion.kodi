#!/bin/sh

ln -s "$PWD" ~/script.service.hyperion
cd ~/
rm -vf script.service.hyperion.zip
zip -x '*/.*' -x '*/*.pyc' -x '*/*.pyo' -x '*/__pycache__/*' -r script.service.hyperion.zip script.service.hyperion
rm ~/script.service.hyperion
