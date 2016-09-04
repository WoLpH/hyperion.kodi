#!/bin/sh

ln -s "$PWD" ~/script.service.hyperion
cd ~/
rm -f script.service.hyperion.zip
zip -x '*/.*' -r script.service.hyperion.zip script.service.hyperion
rm ~/script.service.hyperion
