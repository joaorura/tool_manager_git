import git


class GitManager:
    def __init__(self, path, repositories_list):
        self.path = path
        self.repositories_list = repositories_list['list']

    def execute(self):
        count = 0
        for i in self.repositories_list:
            count += 1
            j = 0
            for j in range(len(i) - 1, -1, -1):
                if i[j] == '/':
                    break

            directories = self.path + f'\\{i[j + 1:]}'

            print(f'{count}: {i} || {directories}')
            try:
                git.Repo.clone_from(i, directories)
            except git.GitCommandError:
                print(f"Error in clone {i}!")
                continue
