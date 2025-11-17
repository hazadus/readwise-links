# Ссылки

- Всего ссылок: 20

## Ссылки

- [How to Manage Your Dotfiles Like a Pro with Git and Stow](https://dev.to/crafts69guy/how-to-manage-your-dotfiles-like-a-pro-with-git-and-stow-3pg1?utm_source=perplexity) 👤 Crafts 69 Guy 💬 1416 🔖 #git, #stow 🗓️ 2025-10-30
    > **Резюме:** This guide shows how to manage dotfiles with Git and GNU Stow.  
Stow creates symlinks so you track configs in one repo and deploy them easily.  
Use .stow-local-ignore and .gitignore to skip machine-specific or unwanted files.
- [Opening all the files that have been modified in a Git branch](https://alexwlchan.net/2025/review-files-in-text-editor/?ref=rss) 👤 alexwlchan.net 💬 522 🔖 #git, #try 🗓️ 2025-09-19
    > **Резюме:** This shows how to open every file changed in a Git branch in your local editor. Use git merge-base to find the branch point and git diff --name-only to list changed files. Pipe the list to xargs and open -a "Visual Studio Code" to open them all.
- [How to Back up Your GitHub Repositories](https://improveandrepeat.com/2025/09/how-to-back-up-your-github-repositories/?utm_source=PythonFriday&utm_medium=RSS&utm_campaign=feed-syndication) 👤 info@ImproveAndRepeat.com (Johnny Graber) 💬 616 🔖 #git, #try, #github 🗓️ 2025-09-02
    > **Резюме:** GitHub is convenient, but you should back up all your repositories. Create bare (or --mirror) clones to keep a full copy of each repo. Automate regular updates with a simple fetch script run by cron.
- [Git: count files in a repository](https://adamj.eu/tech/2025/08/29/git-count-files/) 👤 adamj.eu 💬 340 🔖 #git 🗓️ 2025-08-30
    > **Резюме:** Count committed files with Git so you ignore generated or downloaded files.  
Run: git ls-files -z | tr -d -c '\0' | wc -c — null bytes prevent errors from filenames with newlines.  
Use git ls-files '<pattern>' | wc -l to count types or git ls-files ':!<pattern>' to exclude files.
- [The Problem with GitHub Commit Statuses](https://joshcannon.me/2025/08/24/github-commit-status.html) 👤 Josh Cannon 💬 616 🔖 #git, #github 🗓️ 2025-08-25
    > **Резюме:** GitHub lets you block PR merges using commit statuses, and anyone can post arbitrary statuses via the API. Required checks must come from a specific app, but spoofable or non-required statuses still appear and confuse users. Because statuses are keyed by context and commit SHA, renaming contexts or reusing a SHA can break or wrongly allow merges.
- [Code Review Can Be Better](https://tigerbeetle.com/blog/2025-08-04-code-review-can-be-better/?utm_source=substack&utm_medium=email) 👤 matklad 💬 928 🔖 #git, #github, #codereview, #joyandcuriosity 🗓️ 2025-08-24
    > **Резюме:** The author tried a new way to do code reviews by storing comments as commits in git, but it was too complicated to work well. Current web-based tools cause delays and limit local code exploration. For now, they returned to web reviews, hoping better solutions will come.
- [Commit Messages That Write Themselves](https://newsletter.appliedgo.net/archive/2025-08-17-commit-messages-that-write-themselves/) 👤 The Applied Go Weekly Newsletter 💬 1485 🔖 #go, #git 🗓️ 2025-08-17
    > **Резюме:** A small Go tool reads your staged git diff and uses an LLM to generate Conventional Commit messages.  
It uses LangChainGo so you can swap providers, asks the model for JSON output, and caps diffs to save tokens.  
This issue wraps up the Go & AI mini‑series and asks readers to take a short feedback survey.
- [Git Notes: git's coolest, most unloved feature](https://tylercipriani.com/blog/2022/11/19/git-notes-gits-coolest-most-unloved-feature/) 👤 Tyler Cipriani 💬 717 🔖 #git 🗓️ 2025-07-09
    > **Резюме:** Git notes let you add extra information to commits without changing them. They can store useful data like reviews and test results inside git itself. However, they are hard to use and not widely adopted, so many developers don’t know about them.
- [The best way to store your dotfiles: A bare Git repository](https://www.atlassian.com/git/tutorials/dotfiles) 👤 Atlassian 💬 710 🔖 #git, #try 🗓️ 2025-06-06
    > **Резюме:** This tutorial explains a simple way to store dotfiles using a Git bare repository. It involves creating an alias that allows you to manage your configuration files without interfering with other Git repositories. By following the steps provided, you can easily version and replicate your configurations across different systems.
- [Coping strategies for the serial project hoarder](https://simonwillison.net/2022/Nov/26/productivity/) 👤 Simon Willison 💬 2852 🔖 #git, #github, #inspiration 🗓️ 2025-05-29
    > **Резюме:** The key to increasing productivity on personal projects is to maintain comprehensive documentation and automated tests. Issue driven development, using GitHub issues as temporary documentation, can help manage multiple projects efficiently. Sharing your project work through documentation and release notes is crucial for project completion and accountability.
- [The Perfect Commit](https://simonwillison.net/2022/Oct/29/the-perfect-commit/) 👤 Simon Willison 💬 1979 🔖 #git, #github, #inspiration 🗓️ 2025-05-29
    > **Резюме:** The Perfect Commit is a software development approach that includes a single implementation change, tests, updated documentation, and a link to an issue thread for context. This method helps maintain a clear and manageable commit history, making it easier to review and revert changes if necessary. Simon Willison emphasizes that while not every commit needs to be perfect, aiming for this structure generally enhances productivity and clarity in code development.
- [Why GitHub Actually Won](https://blog.gitbutler.com/why-github-actually-won/) 👤 Scott Chacon 💬 4079 🔖 #git, #github 🗓️ 2025-03-23
    > **Резюме:** GitHub became dominant because it launched at the right time when open-source tools were gaining popularity. The founders had a good sense of design and community, which helped attract early adopters, especially from the Ruby community. As Git grew in use, GitHub's appealing platform made it the go-to choice for code hosting, easily outpacing competitors.
- [How to Deploy Selectively to Production](https://www.caktusgroup.com/blog/2025/03/04/how-deploy-selectively-production/?utm_campaign=Django%2BNewsletter&utm_medium=email&utm_source=Django_Newsletter_275) 👤 Tobias McNulty 💬 495 🔖 #git 🗓️ 2025-03-08
    > **Резюме:** This blog post discusses how to deploy specific features or bug fixes to production using Git flow. It recommends using hotfix branches to cherry-pick necessary commits from the testing branch while avoiding complex changes like schema migrations. This method is best suited for small fixes and code changes, rather than large features.
- [How Core Git Developers Configure Git](https://blog.gitbutler.com/how-git-core-devs-configure-git/) 👤 GitButler 💬 3188 🔖 #git 🗓️ 2025-02-25
    > **Резюме:** The author shares lesser-known Git configuration settings that core Git developers recommend for better performance. These settings include adjusting default branch names, improving diff algorithms, and enhancing push and fetch behavior. By enabling these options, users can streamline their Git experience and make it more efficient.
- [GitHub flow - GitHub Docs](https://docs.github.com/en/get-started/using-github/github-flow) 👤 GitHub Docs 💬 1069 🔖 #git, #github 🗓️ 2025-02-05
    > **Резюме:** GitHub flow is a simple way to collaborate on projects using branches. You create a branch, make changes, and then submit a pull request for feedback before merging your work. After merging, you can delete your branch to keep your project organized.
- [Git: undo a pull](https://adamj.eu/tech/2024/12/31/git-undo-pull-reflog/) 👤 adamj.eu 💬 351 🔖 #git 🗓️ 2025-01-01
    > **Резюме:** If you run a `git pull` and something breaks, you can undo it using `git reset` to revert to the previous commit. If you lost the pull output, check the reflog with `git reflog` to find the old commit reference. Use `git reset --keep` with the appropriate commit SHA to restore your branch to its previous state.
- [Git: count commits with rev-list](https://adamj.eu/tech/2024/11/20/git-count-commits-rev-list/) 👤 Adam Johnson 💬 299 🔖 #git 🗓️ 2024-11-21
    > **Резюме:** The `git rev-list` command helps you count commits in a Git repository. You can count commits on the current branch or between specific branches using simple syntax. For more detailed counts, like by author, the `git shortlog` command is useful.
- [What’s running in production? Making your Docker images identifiable](https://pythonspeed.com/articles/identifying-images/) 👤 Itamar Turner-Trauring 💬 690 🔖 #git 🗓️ 2024-02-16
    > **Резюме:** It’s difficult to debug production problems if you don’t know what image is running in production.
- [Git: generate statistics with shortlog - Adam Johnson](https://adamj.eu/tech/2024/09/03/git-quick-stats-shortlog/) 👤 adamj.eu 💬 650 🔖 #git 🗓️ 2024-09-04
    > **Резюме:** The article explains how to use the `git shortlog` command to generate statistics about commits in a Git repository, which can help create project release notes. It shows different ways to group commits, such as by author or date, and how to limit the results based on time or specific files. The author encourages users to explore these features for better insights into their project's contributions.
- [How to search for strings in Git commit additions or deletions | Stefan Judis Web Development](https://www.stefanjudis.com/today-i-learned/how-to-search-for-strings-in-git-commit-additions-or-deletions/) 👤 Stefan Judis 💬 280 🔖 #git 🗓️ 2024-11-02
    > **Резюме:** Use the `git log -S` to find a commit than added or removed a string from a code base.
