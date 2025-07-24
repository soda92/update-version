import argparse

"parse program arguments"


class Arg:
    build: bool = False
    'build package'

    upload: bool = False
    'upload package to twine (only in effect with build)'

    git_commit: bool = False
    'create a git commit'

    git_tag: bool = False
    'create a git tag'

    git_push: bool = False
    'push git changes (commit/tag)'


def get_args() -> Arg:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--build", "-b", action="store_true", default=False, help="build package"
    )
    parser.add_argument(
        "--upload",
        "-u",
        action="store_true",
        default=False,
        help="upload package to pypi",
    )

    parser.add_argument(
        "--git-commit",
        "-c",
        action="store_true",
        default=False,
        help="create a git commit",
    )

    parser.add_argument(
        "--git-tag",
        "-t",
        action="store_true",
        default=False,
        help="create a git tag",
    )

    parser.add_argument(
        "--git-push",
        "-p",
        action="store_true",
        default=False,
        help="push to git origin",
    )

    args_obj = parser.parse_args()
    args = Arg()
    args.build = args_obj.build
    args.upload = args_obj.upload
    args.git_tag = args_obj.git_tag
    args.git_commit = args_obj.git_commit
    args.git_push = args_obj.git_push
    return args
