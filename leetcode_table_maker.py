import os, pickle

class Table_maker:
    def __init__(self):
        self.path_from = "solutions"
        self.problems = sorted(os.listdir(self.path_from), key=lambda x : int(x))
        with open('problems_info', 'rb') as f:
            self.problems_info = pickle.load(f)

    def make_table(self, category):
        table = []
        table.append("| # | Title | Solutions | Analyses | Difficulty | Note |")
        table.append("| :---: | :---: | :---: | :---: | :---: | :---: |")
        for problem in self.problems:
            index = int(problem)
            if self.problems_info[index]['Category'] != category:
                continue
            row = []
            Analysis = []
            Solution = []
            for file in os.listdir(self.path_from + "\\" + problem):
                if file[-2:] == ".c":
                    Solution.append(f'[C](solutions/{problem}/{file})')
                elif file[-4:] == ".cpp":
                    Solution.append(f'[C++](solutions/{problem}/{file})')
                elif file[-3:] == ".py":
                    Solution.append(f'[Python](solutions/{problem}/{file})')
                elif file[-5:] == ".java":
                    Solution.append(f'[Java](solutions/{problem}/{file})')
                elif file[-3:] == ".md":
                    Analysis.append(f'[md](solutions/{problem}/{file})')

            Title = self.problems_info[index]['Title']
            link = self.problems_info[index]['href']
            Difficulty = self.problems_info[index]['Difficulty']
            Note = self.problems_info[index]['Note'] + " |"

            row.append("| " + problem)
            row.append(f'[{Title}]({link})')
            row.append(', '.join(sorted(Solution)))
            row.append(', '.join(sorted(Analysis)))
            row.append(Difficulty)
            row.append(Note)

            table.append(' | '.join(row))
        return table

if __name__ == "__main__":
    maker = Table_maker()
    Algorithms_table = maker.make_table("Algorithms")
    Database_table = maker.make_table("Database")
    Shell_table = maker.make_table("Shell")
    Concurrency_table = maker.make_table("Concurrency")

    print("## Algorithms")
    print(*Algorithms_table, sep='\n')
    print()

    print("## Database")
    print(*Database_table, sep='\n')
    print()

    print("## Shell")
    print(*Shell_table, sep='\n')
    print()

    print("## Concurrency")
    print(*Concurrency_table, sep='\n')
    print()