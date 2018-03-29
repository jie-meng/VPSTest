if [ $# -lt 1 ]; then
    echo 'You should provide a name!'
    exit -1
fi

sudo apt-get update &&\
sudo apt-get -y install build-essential

./run_unixbench.sh $1

./run_geekbench.sh $1
