import os

def test_git_repo_exists():
    assert os.path.isdir(".git"), "Git repository is missing!"

def test_hello_txt_exists():
    assert os.path.isfile("hello.txt"), "hello.txt file is missing!"

test_git_repo_exists()
test_hello_txt_exists()
