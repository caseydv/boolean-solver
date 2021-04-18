from invoke import task
from quine_mccluskey.__main__ import execute
from quine_mccluskey.output import generateExpression
import time

@task
def solve(c, test_case_path):
    with open(test_case_path, "r") as f:
        function = open(test_case_path).readlines()
        size = int(function[0])

    start = time.time()
    expressionTerms = execute(function, size)
    exp = generateExpression(size, expressionTerms)
    print(exp)
    print(f"calculation took {time.time()-start} seconds")