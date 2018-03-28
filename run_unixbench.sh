#!/bin/sh

echo 'clear working path'
rm master.zip
rm -rf byte-unixbench-master

set -e

if ! [ -f "master.zip" ]; then
    echo 'download unixbench'
    wget https://github.com/kdlucas/byte-unixbench/archive/master.zip
fi

echo 'install unzip'
sudo apt-get install unzip

echo 'uncompress UnixBench'
unzip master.zip

echo 'go to working path'
cd byte-unixbench-master/UnixBench

echo 'Run ...'
./Run > output_unixbench.txt

cd ..
cd ..
cp byte-unixbench-master/UnixBench/output_unixbench.txt .

echo "generate output ${PWD}/output_unixbench.txt"

#clear
rm -rf byte-unixbench-master
rm master.zip

echo '\ndone!'
