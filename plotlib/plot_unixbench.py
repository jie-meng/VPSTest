# -*- coding: utf-8 -*-

from plotlib.unixbenchplotter import UnixBenchPlotter

if __name__ == "__main__":
    unixbenchPlotter = UnixBenchPlotter('UnixBench')
    unixbenchPlotter.addFile('/Users/jiemeng/aws/output/output_unixbench_aws.ec2.t2.micro.txt')
    unixbenchPlotter.addFile('/Users/jiemeng/aws/output/output_unixbench_aws.ec2.m4.large.txt')
    unixbenchPlotter.addFile('/Users/jiemeng/aws/output/output_unixbench_aws.ec2.m5.large.txt')
    unixbenchPlotter.plot()

    print('done!')