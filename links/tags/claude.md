# Ссылки

- Всего ссылок: 11

## Ссылки

- [Get Notified When Claude Code Finishes With Hooks](https://alexop.dev/posts/claude-code-notification-hooks/) 👤 Alexander Opalic 💬 736 🔖 #try, #claude 🗓️ 2025-11-24
    > **Резюме:** Claude Code can run hooks that trigger desktop notifications when it needs your attention. Set a simple .claude/settings.json and a notification script to handle permission_prompt and idle_prompt events. This stops you from constantly checking the terminal and brings you back only when needed.
- [How I Use Every Claude Code Feature](https://blog.sshh.io/p/how-i-use-every-claude-code-feature) 👤 Shrivu Shankar 💬 3126 🔖 #llm, #claude 🗓️ 2025-11-02
    > **Резюме:** The author describes how they use Claude Code across docs, CLI tools, subagents, SDKs, and GitHub Actions. They emphasize a short, focused CLAUDE.md, prefer scripting/Task-based workflows over rigid subagents, and use the SDK for batch or prototype agents. GitHub Actions and careful permissions/timeouts help automate PRs and scale usage.
- [claude_code_docs_map.md](https://simonwillison.net/2025/Oct/24/claude-code-docs-map/#atom-everything) 👤 Simon Willison 💬 205 🔖 #claude 🗓️ 2025-10-25
    > **Резюме:** Simon Willison explains that Claude Code uses a Markdown index (claude_code_docs_map.md) to find documentation when asked about its features. He shows the system prompt directs Claude Code to fetch that URL for answers about itself. He wishes other LLMs would use the same pattern because many struggle to answer questions about their own tools.
- [Don't let Claude Code delete your session logs](https://simonwillison.net/2025/Oct/22/claude-code-logs/#atom-everything) 👤 Simon Willison 💬 99 🔖 #claude 🗓️ 2025-10-22
    > **Резюме:** Claude Code saves your session logs on your computer but deletes them after 30 days by default. You can stop this by changing the cleanupPeriodDays setting in the settings file. This lets you keep your logs for a very long time.
- [Claude Code for web—a new asynchronous coding agent from Anthropic](https://simonwillison.net/2025/Oct/20/claude-code-for-web/#atom-everything) 👤 Simon Willison 💬 1076 🔖 #llm, #claude 🗓️ 2025-10-20
    > **Резюме:** Anthropic released Claude Code for web, an easy-to-use hosted coding agent that runs tasks in managed containers and can edit GitHub repos and open PRs. It supports configurable sandboxing and network isolation to reduce permission prompts and limit data exfiltration. The author found it convenient and effective, though they worry about broad "trusted" allow-lists.
- [Claude Skills are awesome, maybe a bigger deal than MCP](https://simonwillison.net/2025/Oct/16/claude-skills/#atom-everything) 👤 Simon Willison 💬 1480 🔖 #llm, #claude 🗓️ 2025-10-18
    > **Резюме:** Anthropic released Claude Skills, simple Markdown folders that teach the model special tasks and can include scripts and resources. Skills let Claude run code in a sandboxed environment, making it much more capable and efficient than large token-heavy MCP context files. They are easy to share and could quickly create powerful, reusable "agents" for many workflows.
- [Claude Code sub-agents](https://simonwillison.net/2025/Oct/11/sub-agents/#atom-everything) 👤 Simon Willison 💬 295 🔖 #llm, #claude 🗓️ 2025-10-12
    > **Резюме:** Claude Code can run sub-agents to work on smaller tasks in parallel and report back. This helps it handle complex jobs more efficiently, like documenting code templates. The author tested this and got a detailed markdown file created automatically.
- [simonw/claude-skills](https://simonwillison.net/2025/Oct/10/claude-skills/#atom-everything) 👤 Simon Willison 💬 388 🔖 #llm, #claude 🗓️ 2025-10-11
    > **Резюме:** Simon Willison found a hidden /mnt/skills folder in Claude that contains tools for handling Office and PDF files. He zipped the folder, published it on GitHub, and showed the prompts and Python scripts inside. The repo reveals detailed, prewritten code Anthropic uses to create and edit docx, pdf, pptx, and xlsx files.
- [Superpowers: How I'm using coding agents in October 2025](https://blog.fsck.com/2025/10/09/superpowers/) 👤 fsck.com 💬 2112 🔖 #llm, #claude 🗓️ 2025-10-11
    > **Резюме:** The author built "Superpowers," a system of sharable SKILL.md files that teach Claude coding agents how to search, plan, and act using subagents. Claude practices RED/GREEN TDD, pressure-tests skills with realistic scenarios, and mines past conversations for new lessons. Install Claude Code 2.0.13+ and follow the Superpowers SKILL.md files to try it, file bugs, or contribute skills.
- [Superpowers: How I'm using coding agents in October 2025](https://simonwillison.net/2025/Oct/10/superpowers/#atom-everything) 👤 Simon Willison 💬 408 🔖 #llm, #claude 🗓️ 2025-10-11
    > **Резюме:** Simon Willison describes how Jesse Vincent uses Claude Code coding agents and released a plugin called Superpowers. The plugin bundles many practical skills, like root-cause tracing with Graphviz workflows. Willison recommends exploring Jesse’s repository to learn effective agent workflows.
- [MacBook Lid Angle Sensor: Python Implementation Analysis](https://claude.ai/public/artifacts/6c92203e-9768-4ffa-ae0a-9c4307b94c5e) 👤 Claude 💬 1123 🔖 #claude 🗓️ 2025-09-07
    > **Резюме:** Reading MacBook lid angle data in Python is possible but requires complex workarounds. A hybrid pyobjc+ctypes implementation can work but is slow, fragile, and needs manual memory and permission handling. For production, use a small native Objective-C component with Python bindings instead of a pure Python solution.
