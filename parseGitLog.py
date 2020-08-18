# import os
# from typing import re

from datetime import datetime

from pydriller import RepositoryMining

def formatArrayToString (arrayToConvert):
    result = "["
    for x in arrayToConvert:
        result += str(x) + ":"
    result = result[:-1]
    result += "]"
    return result
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
project_name='core'
projectDirAbsPath= '/Users/lujan/Desktop/thesis_work/Damien_Dataset/cloned_repos/core'
currentProjectCsv = '/Users/lujan/Desktop/thesis_work/Damien_Dataset/Git_Logs/' + project_name + '_logs.csv'
print(currentProjectCsv)
print('analyzing project'+ project_name)
with open(currentProjectCsv, 'w', encoding="utf-8") as file:
    header= '"HASH, "MSG", "AUTHOR_NAME", "AUTHOR_EMAIL", "AUTHOR_DATE", ' \
            '"AUTHOR_TIMEZONE", "COMMITTER_NAME", "COMMITTER_EMAIL", "COMMITTER_DATE", "COMMITTER_TIMEZONE",' \
            '"BRANCHES", "IN_MAIN_BRANCH", "IS_MERGE_COMMIT", "MODIFIED_FILES", "NUM_LINES_ADDED", "NUM_LINES_REMOVED", "COMMIT_PARENTS",' \
            '"PROJECT_NAME", "DMM_UNIT_SIZE", "DMM_UNIT_COMPLEXITY", "DMM_UNIT_INTERFACING", ""\n'
    print(header)
    file.write(header)
    for commit in RepositoryMining(projectDirAbsPath).traverse_commits():
        hash = commit.hash
        msg = commit.msg
        author_name = commit.author.name
        author_email = commit.author.email
        author_date = commit.author_date.strftime("%m/%d/%Y-%H:%M:%S")
        author_timezone = str(commit.author_timezone)
        committer_name = commit.committer.name
        committer_email = commit.committer.email
        committer_date = str(commit.committer_date.strftime("%m/%d/%Y-%H:%M:%S"))
        committer_timezone = str(commit.committer_timezone)
        branches = formatArrayToString(commit.branches) # format
        in_main_branch = str(commit.in_main_branch)
        merge = str(commit.merge)
        parents = formatArrayToString(commit.parents) # format
        project_name = commit.project_name
        dmm_unit_size = str(commit.dmm_unit_size)
        dmm_unit_complexity = str(commit.dmm_unit_complexity)
        dmm_unit_interfacing = str(commit.dmm_unit_interfacing)
        #            print all the information from commit_ibject

        modified_files = []
        num_lines_added = []
        num_lines_removed = []
        for mod in commit.modifications:
            modified_file = mod.filename
            num_added = mod.added
            num_removed = mod.removed

            modified_files.append(modified_file)
            num_lines_added.append(num_added)
            num_lines_removed.append(num_removed)

        modified_files = formatArrayToString(modified_files)
        num_lines_added = formatArrayToString(num_lines_added)
        num_lines_removed = formatArrayToString(num_lines_removed)


        line = hash + ',' + msg + ',' + author_name + ',' + author_email + ',' \
               + author_date + ',' + author_timezone + ',' + committer_name + ',' \
        + committer_email + ',' + committer_date + ',' + committer_timezone + ',' \
        + branches + ',' + in_main_branch + ',' + merge + ',' + modified_files + ',' \
        + num_lines_added + ',' + num_lines_removed + ',' + parents + ',' + project_name + ',' \
        + dmm_unit_size + ',' + dmm_unit_complexity + ',' + dmm_unit_interfacing
        print(line)
        file.write(line)