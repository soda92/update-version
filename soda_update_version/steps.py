import subprocess
from .update_version import update_version  # noqa: F401
"steps to perform"


def build():
    subprocess.run(["uv", "build"], check=True)


def upload(version: str):
    subprocess.run(
        [
            "twine",
            "upload",
            "--repository",
            "pypi",
            f"./dist/*-{version}.*",
            f"./dist/*-{version}-*",
        ],
        check=True,
    )


def git_tag(version: str):
    subprocess.run(["git", "tag", version], check=True)
    subprocess.run(["git", "push", "--tags"])
