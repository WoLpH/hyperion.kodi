#!/bin/sh

rm ~/workspace/script.service.hyperion
ln -s "$PWD" ~/workspace/script.service.hyperion
cd ~/workspace/
rm -f script.service.hyperion.zip
zip -x '*/.*' -r script.service.hyperion.zip script.service.hyperion

