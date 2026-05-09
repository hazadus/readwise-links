# Ссылки

- Всего ссылок: 4

## Ссылки

- [Amp, Rebuilt](https://ampcode.com/news/neo) [📖](https://read.readwise.io/read/01kqyy5gnbfzb3nwm18qpb1k13) 👤 Amp News 💬 1380 🔖 #amp 🗓️ 2026-05-06
    > **Резюме:** Today we're starting to roll out the new Amp.
Not all of it, not yet. But the first piece: a rebuilt Amp CLI. Codename: Neo.
In The Coding Agent is Dead we wrote about
where this is going: agents with longer leashes, less handholding, and many more
places to run. Not just one agent in one terminal. Agents prompted from
anywhere, running everywhere.
That's the new Amp we're building.
But the terminal still matters and will matter. There will be moments where you
want the agent right next to you.
So we rebuilt the CLI first. It is still Amp in your terminal. But it's
running on a completely new architecture: remote-controllable, compaction-first,
plugin-powered, and much faster. Built for what's coming.

Let's walk through it.
Remote Control
When you start a thread in the new Amp CLI, you can now remote control it from
ampcode.com.
You'll not only get live updates but you can also send messages, queue and
dequeue them, or cancel what the agent is currently doing:

The architecture that enables this is the reason we rewrote Amp. And remote control is just the start.
No More Manual Context Management
A core principle behind the rebuild: build for what the frontier models can do
now, in 2026, and what they will be able to do in the future. Do not build for
what once was.
Today's leading frontier models are great at handling compaction.
So Amp now manages context for you.
You don't have to watch context percentages anymore, or decide when to
handoff, or extract information from a
thread in a panic.
When the context window fills up, Amp now compacts the thread: it summarizes the
current context, starts a fresh window with that summary, and keeps going.
Compaction now runs automatically when the context window is 90% full.
It was also the first thing we added to the new architecture. During one
migration, we had to shut it off for a day and everyone complained. One
beta-user reported: "I love having auto-compaction. NOT missing handoff..."
So handoff is out. Compaction i...
- [Opus 4.7](https://ampcode.com/news/opus-4.7) [📖](https://read.readwise.io/read/01kq1z7rfpfew9gde3qd52d9ve) 👤 Amp News 💬 506 🔖 #amp 🗓️ 2026-04-25
    > **Резюме:** Opus 4.7 is a smarter coding model that follows prompts more closely and handles complex tasks better than Opus 4.6. It uses tokens more efficiently and gives clearer explanations. To get the best results, users should tell it what success looks like and provide ways for it to check its work.
- [The Coding Agent Is Dead](https://ampcode.com/news/the-coding-agent-is-dead) [📖](https://read.readwise.io/read/01khx7vvj0zfqafa3zdc15w7mc) 👤 ampcode.com 💬 546 🔖 #amp, #llm, #agents, #predictions 🗓️ 2026-02-20
    > **Резюме:** The old way of using coding agents is over because new models are smarter and need less help. Amp is stopping its editor extensions and focusing on a flexible command-line tool instead. This change means Amp is moving forward with the latest technology, inviting users to join their journey.
- [Thoughts on Amp's ad-supported business model](https://rselbach.com/amps-ad-supported-business-model/) [📖](https://read.readwise.io/read/01kfwehj16k0zaxkh2a35z3zvy) 👤 Roberto Selbach 💬 528 🔖 #amp 🗓️ 2026-01-26
    > **Резюме:** Amp offers a new ad-supported free tier that gives users $10 of daily API use in exchange for watching optional ads. This helps lower costs and makes powerful AI tools more accessible, especially for developers in less wealthy countries. Paying users can also enable this free tier to save money while still using premium models.
