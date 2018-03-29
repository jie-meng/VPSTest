#!/bin/sh

if [ $# -lt 1 ]; then
    echo 'You should provide a name!'
    exit -1
fi

echo 'clear working path'
rm -rf Geekbench-4.2.2-Linux

set -e

if ! [ -f "Geekbench-4.2.2-Linux.tar.gz" ]; then
    echo 'download Geekbench-4.2.2-Linux.tar.gz'
    wget http://cdn.geekbench.com/Geekbench-4.2.2-Linux.tar.gz
fi

echo 'uncompress Geekbench-4.2.2-Linux.tar.gz'
tar xf Geekbench-4.2.2-Linux.tar.gz

echo 'go to working path'
cd Geekbench-4.2.2-Linux/

echo 'run geekbench4 and save ouput to geekbench_output ...'
./geekbench4 > geekbench_output

echo 'Make geekbench4 ouput ...'
wget -O output_geekbench.html $(grep -m 1 'https://browser\.geekbench\.com/v4/cpu/' geekbench_output)

cd ..

cp Geekbench-4.2.2-Linux/output_geekbench.html ./output_geekbench_$1.html

echo "generate output ${PWD}/output_geekbench_$1.html"

#clear
rm -rf Geekbench-4.2.2-Linux

echo '\ndone!'
