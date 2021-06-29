# Steps to Execute
# 1. touch Codeforces Question Details.csv
# 2. python3 codeforces_questions_download.py

import requests
from datetime import datetime
import csv


cf_contest_url = "https://codeforces.com/api/contest.list"
cf_problem_url = "https://codeforces.com/api/problemset.problems"
problem_domain = "https://codeforces.com/problemset/problem/{}/{}"
contest_date_limit = datetime(2017, 1, 1)
prepare_data = {}

# Assuming that CSV is in the same folder as this script
output_sheet_name = "Codeforces Question Details.csv"
csv_fieldnames = ["Contest Id", "Contest Name", "Contest Date",
                  "Problem Type", "Problem Name", "Rating", "Problem URL"]


def prepare_contest_data():
    all_contest = requests.get(url=cf_contest_url).json()
    all_contest = all_contest["result"]
    for contest in all_contest:
        contest["cont_date"] = datetime.fromtimestamp(
            contest["startTimeSeconds"])
        if(contest["cont_date"] < contest_date_limit):
            continue
        prepare_data[contest["id"]] = {
            "Contest Id": contest["id"],
            "Contest Name": contest.get("name", ""),
            "Contest Date": contest["cont_date"].strftime("%d %b, %Y"),
            "problem_list": []
        }


def prepare_problem_data():
    all_problem = requests.get(url=cf_problem_url).json()
    all_problem = all_problem["result"]["problems"]
    for problem in all_problem:
        if problem["contestId"] not in prepare_data:
            continue

        created_problem_url = problem_domain.format(
            problem["contestId"], problem.get("index", ""))
        problem_details = {
            "Problem Type": problem.get("index", ""),
            "Problem Name": problem.get("name", ""),
            "Rating": problem.get("rating", ""),
            "Problem URL": created_problem_url
        }
        prepare_data[problem["contestId"]
                     ]["problem_list"].append(problem_details)


def fill_csv_sheet():
    already_updated_contest = []
    with open(output_sheet_name, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        already_updated_contest = [int(line["Contest Id"]) for line in reader]

    with open(output_sheet_name, mode='a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_fieldnames)
        for key, val in prepare_data.items():
            if int(key) in already_updated_contest:
                continue
            temp_row_data = {
                "Contest Id": val["Contest Id"],
                "Contest Name": val["Contest Name"],
                "Contest Date": val["Contest Date"]
            }
            for problem_xyz in val["problem_list"]:
                temp_row_data.update(problem_xyz)
                writer.writerow(temp_row_data)


def execute_script():
    prepare_contest_data()
    prepare_problem_data()
    fill_csv_sheet()


execute_script()
