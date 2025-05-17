import subprocess
from .args import get_args
from .steps import build, upload, git_tag, update_version


def main():
    version = update_version()
    args = get_args()
    if args.build:
        build()
    if args.upload:
        upload(version)


    # git_stat = subprocess.getoutput("git status")
    # if not "working tree clean" in git_stat:
    #     print("please commit your changes first")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"bump version to {version}"])

    subprocess.run(["git", "push"])

    if args.git_tag:
        git_tag(version)


if __name__ == "__main__":
    main()
