import sys
import os
import requests
import shutil

api_url = "https://codeforces.com/api/"
contest_url = "https://codeforces.com/contest/"
template = "main.cpp"


class APIError(Exception):
    pass


def getResultJson(url, params=None):
    req = requests.get(url + params)
    if req.status_code != 200:
        return APIError("HTTP {}".format(req.status_code))
    else:
        return req.json()


def getContestName(id):
    res = getResultJson(api_url, "contest.standings?contestId=" + str(id))
    if res["status"] != "OK":
        raise APIError("{}: {}".format(res["status"], res["comment"]))
    if not res["result"]:
        raise ValueError("No Data")
    contest_name = res["result"]["contest"]["name"]
    names = contest_name.split(" ")
    s = ""
    for name in names:
        if name == "Round" or name == "" or name == "Codeforces":
            continue
        s += name
    return s


def getProblemIndex(id):
    res = getResultJson(api_url, "contest.standings?contestId=" + str(id))
    if res["status"] != "OK":
        raise APIError("{}: {}".format(res["status"], res["comment"]))
    if not res["result"]:
        raise ValueError("No Data")
    problems = res["result"]["problems"]
    problem_index = []
    for problem in problems:
        problem_index.append(problem["index"])
    return problem_index


def createContestDir(contest_id):
    current_dir = os.getcwd()
    base_dir = os.path.dirname(__file__)
    contest_name = getContestName(contest_id)
    new_dir_path = contest_name
    if not os.path.isdir(new_dir_path):
        os.makedirs(new_dir_path)
    problem_index = getProblemIndex(contest_id)
    for index in problem_index:
        new_problem_dir_path = new_dir_path + "/" + index
        if os.path.exists(new_problem_dir_path):
            print("Problem directory already exists")
            sys.exit()
        os.makedirs(new_problem_dir_path)
        with open(os.path.join(new_problem_dir_path, "main.cpp"), 'w') as f:
            f.write(" ")
        shutil.copyfile(base_dir + "/" + "main.cpp", new_problem_dir_path + "/main.cpp")
        os.chdir(new_problem_dir_path)
        os.system('oj d ' + contest_url + str(contest_id) + "/problem/" + index)
        os.chdir(current_dir)


def test():
    os.system('oj t')


def submit(contest_id):
    current_dir = os.getcwd()
    index = os.path.basename(current_dir)
    os.system('oj s ' + contest_url + str(contest_id) + "/problem/" + index + " " + template)


def showHelp():
    print("HOW TO USE")
    print("Create contest directory : \"cft n (contest id)\"")
    print("Test your code           : \"cft t\"")
    print("Submit your code         : \"cft s\"")
    print("Note : Contest id is " + str(contest_url) + "(contest id)")


def main():
    args = sys.argv
    if len(args) == 1:
        print("Not Enough Args")
        showHelp()
        sys.exit()
    elif len(args) > 3:
        print("Too Much Args")
        showHelp()
        sys.exit()
    command = args[1]
    if command == 'n':
        contest_id = args[2]
        if len(args) != 3:
            print("Enter Correct Number of Args")
            showHelp()
            sys.exit()
        createContestDir(contest_id)
    elif command == 't':
        test()
    elif command == 's':
        contest_id = args[2]
        if len(args) != 3:
            print("Enter Correct Number of Args")
            showHelp()
            sys.exit()
        submit(contest_id)
    else:
        showHelp()
        sys.exit()
