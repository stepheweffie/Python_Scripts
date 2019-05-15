commit = input("Go ahead and write a commit message: ")
commit = str(commit)

if len(commit) > 51:
    print("too long, wrapping for you")
    commit_line = commit[:49]
    commit_wrap = commit[50:]
    print(commit_line + '\n' +commit_wrap)
else:
    print("good length, less than 51")


