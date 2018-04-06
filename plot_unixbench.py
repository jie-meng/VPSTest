# -*- coding: utf-8 -*-

from plotlib.unixbenchplotter import UnixBenchPlotter

if __name__ == "__main__":
    unixbench_plotter = UnixBenchPlotter('UnixBench')
    unixbench_plotter.setIsMultiCore(True)
    #unixbench_plotter.addFile('/Users/jiemeng/aws/output/output_unixbench_aws.ec2.t2.micro.txt')
    unixbench_plotter.addFile('/Users/jiemeng/aws/output/output_unixbench_aws.ec2.m4.large.txt')
    unixbench_plotter.addFile('/Users/jiemeng/aws/output/output_unixbench_aws.ec2.m5.large.txt')
    unixbench_plotter.plot()

    print('done!')
