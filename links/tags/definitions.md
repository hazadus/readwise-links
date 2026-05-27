# Ссылки

- Всего ссылок: 4

## Ссылки

- [Building Pi With Pi](https://lucumr.pocoo.org/2026/5/24/pi-oss/) [📖](https://read.readwise.io/read/01ksde9fsf2v08c6qm3ce7zy2n) 👤 Armin Ronacher 💬 1877 🔖 #foss, #definitions, #llm-devimpact 🗓️ 2026-05-24
    > **Резюме:** Pi is now part of Earendil, but in the important sense it is
still Mario’s project.  He has been living with its
issue tracker longer than I have, and he has been exposed to the weirdness of
the new form of agent traffic in Open Source projects for longer too.  This post
is mostly a reflection of my own experience after spending more time in the
tracker, using Pi to work on Pi, and watching what I have learned about it so
far.
Slop Issues
Unsurprisingly, we are using Pi to build Pi.  That sounds like a cute dogfooding
thing but it really helps understand what we do.  An interesting effect of
building with agents is that it changes the role of the issue tracker a tiny
bit.  The issue descriptions are not just messages from a user to a maintainer
because we also use them as inputs for prompts in Pi sessions.  It is something
I might hand to my clanker1 and say: “understand this, reproduce it, inspect
the code, and propose a fix.”
That means the shape of the issue matters in a new way.  A bad issue was always
annoying, but at least a lot of issues were vague.  Now we are also dealing with
a class of issues that are 5% human and 95% clanker-generated and largely
inaccurate shit.  A bad issue that contains a plausible but wrong diagnosis
creates extra work.
The most frustrating failure mode right now is that people submit issues that
are not in their own voice.  They contain an observed problem somewhere, but it
has been thrown into a clanker and the clanker reworded it and made a huge mess
of it.  Typically, it was prompted so badly that the conclusions produced are
more often than not inaccurate but always full of confidence.  The result is
complete guesswork on root causes, fake-minimal repros, suggested implementation
strategies, analogies to adjacent but often the wrong code, and long lists of
error classes that might or might not matter.
That is worse than no diagnosis.
I don’t want to point to specific issues because I really do not want to bad
mouth anyone, bu...
- [The Pulse: ‘Tokenmaxxing’ as a weird new trend](https://blog.pragmaticengineer.com/the-pulse-tokenmaxxing-as-a-weird-new-trend/) [📖](https://read.readwise.io/read/01kpxsckj3veyzbhy69y9dhzyc) 👤 Gergely Orosz 💬 1993 🔖 #llm, #definitions, #llm-devimpact 🗓️ 2026-04-23
    > **Заметка:** Думается, когда волна хайпа спадёт, все придут к спокойному использованию LLM-инструментов – а не показному завышению объёмов их использования. 
    > **Резюме:** Some tech companies like Meta and Microsoft created leaderboards to track AI token usage, which led to wasteful and excessive AI use called "tokenmaxxing." This practice caused high costs and low-quality work, prompting backlash and changes like Meta removing its leaderboard. Shopify's careful approach with monitoring and limits shows a better way to encourage AI use without encouraging waste.
- [Andrej Karpathy talks about "Claws"](https://simonwillison.net/2026/Feb/21/claws/#atom-everything) [📖](https://read.readwise.io/read/01kj0cy87553fgk4bewgp5x7zb) 👤 Simon Willison 💬 261 🔖 #llm, #definitions 🗓️ 2026-02-21
    > **Резюме:** Andrej Karpathy talks about "Claws," a new layer of AI agents that improve how tasks are managed and tools are used. He finds smaller Claws like NanoClaw interesting because they are simple and flexible. "Claw" is becoming a name for AI agent systems that run on personal devices and handle tasks through messaging.
- [Deep Blue](https://simonwillison.net/2026/Feb/15/deep-blue/#atom-everything) [📖](https://read.readwise.io/read/01khn0a805a87jayezjjx9rtgy) 👤 Simon Willison 💬 961 🔖 #llm, #definitions, #llm-devimpact 🗓️ 2026-02-17
    > **Резюме:** Many software developers feel lost because AI can now do their jobs easily. This feeling is called "Deep Blue," named after the chess computer that beat Garry Kasparov. Although AI is powerful, people can still find new ways to use their skills and grow.
