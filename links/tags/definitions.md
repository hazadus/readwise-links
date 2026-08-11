# Ссылки

- Всего ссылок: 7

## Ссылки

- [Don't be a meat proxy](https://gruhn.me/blog/2026-08-03/) [📖](https://read.readwise.io/read/01kzn9k19m433y2e3wcn77td07) 👤 gruhn.me 💬 248 🔖 #definitions, #llm-devimpact 🗓️ 2026-08-10
    > **Резюме:** Don't just copy AI answers to others without understanding them first. Read, check, and explain the AI output in your own words to add real value. Otherwise, you become a "meat proxy" who does no real work.
- [The Intent Debt](https://addyosmani.com/blog/intent-debt/) [📖](https://read.readwise.io/read/01ktdd7n1t4nztd0twq75mkr93) 👤 Addy Osmani 💬 1785 🔖 #intentdebt, #definitions, #cognitivedebt, #llm-devimpact 🗓️ 2026-06-06
    > **Резюме:** Intent debt is the missing explanation of why software was built a certain way, and it lives in unwritten goals and decisions. Unlike technical and cognitive debt, AI agents cannot fix intent debt because they don’t know the true reasons behind choices. To reduce intent debt, teams must write down their goals and decisions clearly so both humans and AI can understand the system’s purpose.
- [Clanker: A Word For The Machine](https://lucumr.pocoo.org/2026/5/26/clankers/) [📖](https://read.readwise.io/read/01ksj7vq42nw5sbtgn8rz3ky2v) 👤 Armin Ronacher 💬 1969 🔖 #llm, #definitions, #llm-reality 🗓️ 2026-05-26
    > **Резюме:** In my last post I used the word “clanker” as an
alternative to “agent” quite consistently and probably excessively.  That choice
ended up attracting a lot more attention than I expected in the Hacker News
comment section of that post and a number of folks had a very strong reaction:
to them it sounded like a slur, in one case even something adjacent to the
n-word.
That reaction surprised me somewhat, but it also made me realize that I should
write down what I mean by the word for future reference.
For me “clanker” is useful because it creates distance from the machine and that
is a quality which is important to me.  The machine is not a person, not a
co-worker, not a friend, not a little spirit in the terminal. It is just a
machine, a tool, and nothing more.
Why Not Agent?
I dislike the word “agent” for these LLM based tool loops with a UI attached.
In everyday use an agent is someone who acts on behalf of someone else and it
has agency and more importantly: responsibility.  An agent decides, represents,
negotiates, acts, and can be blamed.  In the current AI discourse we
increasingly do a lot of anthropomorphizing and the term “agent” is now
frequently being used to put blame on an abstract machine.  But the machine
cannot be responsible, whoever is wielding it is.  If it drops your
database
it was not at fault, you were.
Agent makes the machine sound like a person with delegated authority and I do
not think that is healthy.
What we actually have is a language model attached to a harness, a prompt, some
tools, a bit of context, and a boring tool loop.  Sometimes the loop is very
capable and it surprises us by editing code for a really long time and produce
genuinely amazing and even valuable outputs.  But the agency is not in the model
or harness but in the human and in the organization that deployed it.  If my
coding tool opens a pull request, I opened that pull request, not the machine.
If my machine spams someone’s issue tracker, I spammed someone’s issue tra...
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
