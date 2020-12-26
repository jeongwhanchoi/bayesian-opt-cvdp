# from Utils.helper import *
from experiment.Utils.helper import *
import pandas as pd
import numpy as np
import os
from fnmatch import fnmatch


if __name__ == '__main__':

    root = '../dataset/MORPH/'
    project_name = ['ant', 'camel', 'ivy', 'jedit', 'log4j', 'lucene', 'poi', 'synapse', 'velocity', 'xerces']

    pattern = "*.csv"
    project_list = []
    for i, row in enumerate(project_name):
        print(row)
        version_list = []
        for path, subdirs, files in os.walk(root + row + '/'):
            subdirs.sort()
            files.sort()
            for name in files:
                if fnmatch(name, pattern):
                    #                 print(os.path.join(path, name))
                    version_list.append(os.path.join(path, name))
        project_list.append(version_list)

    for i in range(len(project_list)):
        for j in range(len(project_list[i])):
            if j == len(project_list[i]) - 1:
                break
            print('*********************************************************')
            print('Experiment-', i)
            print(project_list[i][-1], project_list[i][j])
            _, tail = os.path.split(project_list[i][-1])
            target_name = os.path.splitext(tail)[0]
            _, tail2 = os.path.split(project_list[i][j])
            source_name = os.path.splitext(tail2)[0]
            print(target_name +'->'+ source_name)
            target_project = project_list[i][-1]
            # project_recent = project_list[i][-1]
            source_project = project_list[i][j]

            src_domain = pd.read_csv(source_project)
            tar_domain = pd.read_csv(target_project)
            src_domain['bug'] = np.where(src_domain['bug'] == 0, 0, 1)
            tar_domain['bug'] = np.where(tar_domain['bug'] == 0, 0, 1)

            Xs, Ys, Xt, Yt = np.array(src_domain.iloc[:, 3:-1]), np.array(src_domain['bug']), np.array(tar_domain.iloc[:, 3:-1]), np.array(tar_domain['bug'])
            # RunExperiment(Xs, Ys, Xt, Yt, target_name, source_name, 'Burakfilter', 'BRF', 'NoImb', 'KS', 'dist')
            # RunExperiment(Xs, Ys, Xt, Yt, target_name, source_name, 'TCA', 'BRF', 'NoImb', 'KS', 'dist')
            # RunExperiment(Xs, Ys, Xt, Yt, target_name, source_name, 'TCA', 'BRF', 'NoImb', 'KS', 'all')
            # RunExperiment(Xs, Ys, Xt, Yt, target_name, source_name, 'DSBF', 'BRF', 'NoImb', 'KS', 'all')
            RunExperiment(Xs, Ys, Xt, Yt, target_name, source_name, 'DSBF', 'BRF', 'NoImb', 'KS', 'dist')
