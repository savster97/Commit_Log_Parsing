# import os
# from typing import re


from pydriller import RepositoryMining
#
# DATASET_DIR= 'C:\\Users\\Rafia Bushra\\Desktop\\TUT_Job\\temp'
# #repoName = 'commons-jexl.csv'
#
#
# filenames = os.listdir(DATASET_DIR)  # get all files' and folders' names in the current directory
#
# result = []
# for filename in filenames:  # loop through all the files and folders
#     if os.path.isdir(
#             os.path.join(os.path.abspath(DATASET_DIR), filename)):  # check whether the current object is a folder or not
#         result.append(filename)
#         print(filename)
#
# result.sort()

# for index, project_dir in enumerate(result):
project_name='gecko-dev'
projectDirAbsPath= '/Users/lujan/Desktop/thesis_work/Damien_Dataset/cloned_repos/gecko-dev'
currentProjectCsv = '/Users/lujan/Desktop/thesis_work/Damien_Dataset/Git_Log_Changes/' + project_name + '_logs.csv'
print(currentProjectCsv)
print('analyzing project'+ project_name)
with open(currentProjectCsv, 'w', encoding="utf-8") as file:
    header= '"PROJECT_ID", "FILE", "COMMIT_HASH", "DATE", "COMMITTER_ID", "LINES_ADDED", "LINES_REMOVED", "NOTE"\n'
    print(header)
    file.write(header)
    for commit in RepositoryMining(projectDirAbsPath).traverse_commits():

        for mod in commit.modifications:
            line='"{}","{}","{}","{}","{}","{}","{}","{}"\n'.format(project_name.replace('.csv', ''),
                                                                    mod.filename,
                                                                    commit.hash.replace('\n',' '),
                                                                    commit.committer_date,
                                                                    commit.author.name.replace('\n', ' '),
                                                                    mod.added,
                                                                    mod.removed,
                                                                    commit.msg.replace('\n', ' ')
                                                                            .replace('"', '')
                                                                            .replace(',', ' '))
            print(line)
            file.write(line)