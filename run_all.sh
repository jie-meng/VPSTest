if [ $# -lt 1 ]; then
    echo 'You should provide a name!'
    exit -1
fi

./run_unixbench.sh $1

./run_geekbench.sh $1
