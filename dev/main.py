import argparse

from utils.utils import fetch_env_variables


def main():
    env_variables = fetch_env_variables()
    ACCOUNT_ID = env_variables["ACCOUNT_ID"]
    BOOMI_USER = env_variables["BOOMI_USER"]
    ACCOUNT_ID = env_variables["ACCOUNT_ID"]


def get_command_line_args():
    """
    Get command line arguments
    """

    parser = argparse.ArgumentParser(
        description="Generate Dependency Report for all components in a given Boomi Folder."
    )

    parser.add_argument(
        "-f",
        "--folder_name",
        metavar="folder_name",
        type=str,
        help="Boomi Folder Name",
        required=True,
    )

    parser.add_argument(
        "-fid",
        "--folder_id",
        metavar="folder_id",
        type=str,
        help=(
            "Boomi Folder ID, only required if querying a folder name that exists multiple times in the Boomi environment."
        ),
    )

    args = parser.parse_args()

    args_dict = {}
    args_dict["folder_name"] = args.account

    profile_id_lst = []
    if args.profile_dump is not None:
        print("profile_dump is not None")
        profile_id_lst = [
            profile_id.strip() for profile_id in args.profile_dump.split(",")
        ]
        print(profile_id_lst)
    args_dict["profile_dump"] = profile_id_lst

    md_profile_id_lst = []
    if args.mapping_document is not None:
        md_profile_id_lst = [
            profile_id.strip() for profile_id in args.mapping_document.split(",")
        ]
        args_dict["integration"] = args.integration
    args_dict["mapping_document"] = md_profile_id_lst

    args_dict["environment_report"] = get_env_id_lst_from_cmd(args.extension_report)

    args_dict["assessment_report"] = get_env_id_lst_from_cmd(args.assessment_report)

    args_dict["build_acct"] = (
        args_dict["assessment_report"] != [] or args_dict["environment_report"] != []
    )

    return args_dict


if __name__ == "__main__":

    main()
