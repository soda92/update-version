import argparse

"parse program arguments"


class Arg:
    build: bool = False
    upload: bool = False
    git_cm: bool = False
    git_tag: bool = False
    git_push: bool = False


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
        "--upload",
        "-u",
        action="store_true",
        default=False,
        help="upload package to pypi",
    )

    parser.add_argument(
        "--git-tag",
        "-g",
        action="store_true",
        default=False,
        help="create a git tag",
    )

    args_obj = parser.parse_args()
    args = Arg()
    args.build = args_obj.build
    args.upload = args_obj.upload
    args.git_tag = args_obj.git_tag
    return args
