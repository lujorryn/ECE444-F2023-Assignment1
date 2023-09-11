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

## Activity 4
Unit test
<p>
    <img src="screenshots\Activity4-1-local-commit.png" alt="Screenshot Activity 4-1"/><br/>
    <img src="screenshots\Activity4-2-remote-commit.png" alt="Screenshot Activity 4-2"/><br/>
</p>

## Activity 5
Git rebase
<p>
    Complete rebase process with git logs after every step<br/>
    <img src="screenshots\Activity5-1-rebase-process.png" alt="Screenshot Activity 4-1"/><br/>
</p>

Breakdown of `git rebase -i HEAD~4` inside the editor:

<p>
    Interactive rebase screen before edit<br/>
    <img src="screenshots\Activity5-2-interactive-before.png" alt="Screenshot Activity 4-2"/><br/>
    Interactive rebase screen after edit<br/>
    <img src="screenshots\Activity5-3-interactive-after.png" alt="Screenshot Activity 4-2"/><br/>
</p>

### End result of Activity 5:
develop: c3->c4->c1->c2\
rebase: c1->c2\
main: none of the c1~c4 commits
