import os

import dateUtil
import downloadhtml
import sendMail
from  gitdiff import *


def downWikiIfEmpty(DIR_NAME):
    if not os.path.exists(DIR_NAME):
        os.mkdir(DIR_NAME)
    if os.path.isdir(DIR_NAME):
        L = os.listdir(DIR_NAME)
        if len(L) <= 1:
            downloadhtml.downloadWiki()


def run():
    DIR_NAME = "wiki"
    date = dateUtil.today()
    downWikiIfEmpty(DIR_NAME)
    repo = readRepo(DIR_NAME)
    if repo is None:
        repo = createRepo(DIR_NAME)
        commit(repo)
        createBranch(repo, date)
        checkoutBranch(repo, date)
    else:
        today = dateUtil.today()
        yesterday = dateUtil.yesterday()
        # today = '2017-06-15'
        # yesterday = '2017-06-14'
        createBranch(repo, today)
        checkoutBranch(repo, today)
        downloadhtml.downloadWiki()
        commit(repo)
        change = diff(repo, yesterday)
        if change is not None:
            sendMail.mail(change, "Monitor_WeChatWiki_" + dateUtil.today())


if __name__ == "__main__":
    run()
