# pylint: disable=bare-except
"""
Functions that have to run a shell
"""
import subprocess

from app.config import GIT_PATH


def repo_info():
    "function"
    try:
        tag = (
            subprocess.check_output(
                ["git", "--git-dir=" + GIT_PATH, "describe", "--abbrev=0", "--tags"]
            )
            .strip()
            .decode("utf-8")
        )
        version = (
            subprocess.check_output(["git", "--git-dir=" + GIT_PATH, "describe", "--tags"])
            .strip()
            .decode("utf-8")
        )
        return tag, version
    except:
        return "err", "err"
