# -*- coding: utf-8 -*-

import os
from plotlib.unixbenchplotter import UnixBenchPlotter

if __name__ == "__main__":
    unixbench_plotter = UnixBenchPlotter('UnixBench')
    unixbench_plotter.setIsMultiCore(True)

    #unixbench_plotter.addFile('/Users/jiemeng/aws/output/output_unixbench_aws.ec2.t2.micro.txt')
    unixbench_plotter.addFile('/Users/jiemeng/aws/output/output_unixbench_aws.ec2.m4.large.txt')
    unixbench_plotter.addFile('/Users/jiemeng/aws/output/output_unixbench_aws.ec2.m5.large.txt')
    unixbench_plotter.addFile('/Users/jiemeng/aws/output/output_unixbench_tc.s2.4c8g.txt')
    unixbench_plotter.plot()

    os.rename('output.png', unixbench_plotter.getName().replace(' ', '_') + '.png')
    print('Rename output.png to {}'.format(unixbench_plotter.getName() + '.png'))
    print('done!')
