# Jorryn Lu
ECE444 Fall 2023 Assignment 1 - Self Assessment

## Activity 1
Creating a repo in your own GitHub account and commiting files
<p>
    <img src="screenshots\Activity1-commit.png" alt="Screenshot Activity 1"/>
</p>

## Activity 2
Branching and merging
<p>
    <img src="screenshots\Activity2-branch&merge.png" alt="Screenshot Activity 2"/>
</p>

## Activity 3
Issues, pull requests and merge conflicts

My steps to solving merge conflicts:
1. On the develop branch: `git rebase main` -> encounter merge conflict
2. Modify helloworld.py to fix conflicted lines
3. `git add` modified file(s), `git commit`changes, and then `git rebase --continue`
4. `git push --force-with-lease` force push changes to remote branch so the conflicted commit is resolved

The following 5 screenshots document my process:
<p>
    Git commands of the steps<br/>
    <img src="screenshots\Activity3-1-rebase-main.png" alt="Screenshot Activity 3-1"/><br/>
    Local branch commit history<br/>
    <img src="screenshots\Activity3-2-rebase-commits.png" alt="Screenshot Activity 3-2"/><br/>
    Record of force push inside pull request<br/>
    <img src="screenshots\Activity3-3-force-push.png" alt="Screenshot Activity 3-3"/><br/>
    Successful pull request merge. The 2 different commits on the PR are before (08f063b with conflict) and after the force push  (3b61e14 resolved)<br/>
    <img src="screenshots\Activity3-4-merge.png" alt="Screenshot Activity 3-4"/><br/>
    Remote commit history on main after merge<br/>
    <img src="screenshots\Activity3-5-commits.png" alt="Screenshot Activity 3-5"/><br/>
</p>