from sys import argv

from src.git_process.GitManager import GitManager
from src.pre_process.ReadData import ReadData


def get_path():
    if len(argv) < 3:
        raise RuntimeError

    return argv[1], argv[2]


def main():
    path = get_path()
    get_data = ReadData(path[0])
    data = get_data.getProcessData()
    git_manager = GitManager(path[1], data)
    git_manager.execute()


if __name__ == '__main__':
    main()
