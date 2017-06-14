import logging

import git
from git import InvalidGitRepositoryError

logging.basicConfig(level=logging.INFO)


def readRepo(DIR_NAME):
    try:
        return git.Repo(DIR_NAME)
    except InvalidGitRepositoryError:
        return None


def createRepo(DIR_NAME):
    repo = git.Repo.init(DIR_NAME)
    return repo


def createBranch(repo, newBranchName):
    git = repo.git
    git.branch(newBranchName)


def checkoutBranch(repo, newBranchName):
    git = repo.git
    git.checkout(newBranchName)


def commit(repo):
    git = repo.git
    git.add(".")
    git.commit('-m', 'first commit')


def diff(repo, diffWithBranch):
    files = repo.git.diff(diffWithBranch)
    includeChange = 0
    for f in files.split('\n'):
        print f
        if includeChange == 0 and f.startswith('-') and not f.startswith('---') and f.find(
                'mw.config.set({"wgBackendResponseTime":') == -1:
            includeChange = 1
        if includeChange == 0 and f.startswith('+') and not f.startswith('+++') and f.find(
                'mw.config.set({"wgBackendResponseTime":') == -1:
            includeChange = 1

    if includeChange == 1:
        return files
    return None
