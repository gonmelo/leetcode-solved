import os
import sys
import re

def kebab_case(s):
    s = s.lower()
    s = re.sub(r"[^\w\s]", "", s)  # remove punctuation
    s = re.sub(r"\s+", "-", s)     # replace spaces with dashes
    return s

def create_problem(problem_id: int, title: str):
    slug = kebab_case(title)
    file_name= f"{problem_id}-{slug}.py"
    solution_path = os.path.join("problems", file_name)
    if not os.path.exists(solution_path):
        with open(solution_path, "w") as f:
            f.write(f'''"""
{problem_id}. {title}
Link: https://leetcode.com/problems/{slug}/
Difficulty: TODO

Approach:
- TODO: describe the algorithm
- Time Complexity: TODO
- Space Complexity: TODO
"""
''')
        print(f"Created: {solution_path}") 
    else:
        print(f"File already exists: {solution_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_problem.py <problem_id> <problem_title>")
        sys.exit(1)
    
    problem_id = sys.argv[1]
    title = " ".join(sys.argv[2:])
    create_problem(problem_id, title)