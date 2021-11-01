#!/bin/sh

root_dir=$(dirname $(readlink -f $0))

old_dir=$(pwd)
cd $root_dir
dpkg-buildpackage -b --no-sign -rfakeroot && \
    find $root_dir/.. -maxdepth 1 -name '*.deb' -exec mv {} $root_dir \;


cd $old_dir
