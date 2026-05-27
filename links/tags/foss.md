# Ссылки

- Всего ссылок: 12

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
- [The Maintainer's Dilemma](https://spf13.com/p/the-maintainers-dilemma/) [📖](https://read.readwise.io/read/01ksam0gs41887x9es2gpw1b2q) 👤 spf13 💬 2569 🔖 #foss, #llm-devimpact 🗓️ 2026-05-23
    > **Резюме:** Maintainers face a big problem: too many contributions and not enough time to review them. AI tools can help with simple tasks but can't replace the deep knowledge and judgment humans use to maintain projects. Relying on AI or ignoring reviews risks breaking trust and quality in open source communities.
- [Before GitHub](https://lucumr.pocoo.org/2026/4/28/before-github/) [📖](https://read.readwise.io/read/01kqaz6w1gpbt46g0n1kbeny9s) 👤 Armin Ronacher 💬 2307 🔖 #foss, #github, #predictions 🗓️ 2026-04-28
    > **Заметка:** Да уж, прям тектонические сдвиги в ИТ пошли. Пора задуматься о переезде на Gitverse?..
    > **Резюме:** GitHub was not the first home of my Open Source software.  SourceForge
was.
Before GitHub, I had my own Trac installation.  I had Subversion repositories,
tickets, tarballs, and documentation on infrastructure I controlled.  Later I
moved projects to Bitbucket, back when Bitbucket still felt like a serious
alternative place for Open Source projects, especially for people who were not
all-in on Git yet.
And then, eventually, GitHub became the place, and I moved all of it there.
It is hard for me to overstate how important GitHub became in my life.  A large
part of my Open Source identity formed there.  Projects I worked on found users
there.  People found me there, and I found other people there.  Many professional
relationships and many friendships started because some repository, issue, pull
request, or comment thread made two people aware of each other.
That is why I find what is happening to GitHub today so sad and so
disappointing.  I do not look at it as just the folks at Microsoft making
product decisions I dislike.  GitHub was part of the social infrastructure of
Open Source for a very long time.  For many of us, it was not merely where the
code lived; it was where a large part of the community lived.
So when I think about GitHub’s decline, I also think about what came before it,
and what might come after it.  I have written a few times over the years about
dependencies, and in particular about the problem of micro
dependencies.  In my mind, GitHub gave
life to that phenomenon.  It was something I definitely did not completely
support, but it also made Open Source more inclusive.  GitHub changed how Open
Source feels,
and later npm and other systems changed how dependencies feel.  Put them
together and you get a world in which publishing code is almost frictionless,
consuming code is almost frictionless, and the number of projects in the world
explodes.
That has many upsides.  But it is worth remembering that Open Source did not
always work this way.
A Sma...
- [I don't want your PRs anymore](https://dpc.pw/posts/i-dont-want-your-prs-anymore/?utm_source=tldrdev) [📖](https://read.readwise.io/read/01kpz5e2tbx8wy0nw6sqbjr1zh) 👤 dpc.pw 💬 846 🔖 #foss, #llm-devimpact 🗓️ 2026-04-24
    > **Заметка:** Думаю, автор выражает взгляд многих мейнтейнеров. И очередное подтверждение: разработка никуда не делась, она просто сместилась от кода на чуть более высокий уровень. 

Via TLDR
    > **Резюме:** The author prefers to make code changes himself using AI tools because reviewing others' pull requests takes too much time and can be risky. Instead, contributors can help by reporting bugs, discussing ideas, and sharing prototypes or prompts for reference. Forking the code to customize it independently is encouraged, as it saves time and allows personal use cases.
- [AI as economic warfare](https://ghuntley.com/warfare/) [📖](https://read.readwise.io/read/01kkw6jb3k63bn8ha3th36sx4x) 👤 Geoffrey Huntley 💬 753 🔖 #llm, #foss, #predictions 🗓️ 2026-03-16
    > **Резюме:** Open-source AI models are being used as economic weapons by countries to challenge rivals. China offers free local AI models while the US spends heavily on research, creating a new kind of economic warfare. This raises important questions about trust, control, and the future of AI-dependent businesses and economies.
- [AI creates asymmetric pressure on Open Source](https://dri.es/ai-creates-asymmetric-pressure-on-open-source) [📖](https://read.readwise.io/read/01kg83yt4byj5f4m9dzff9v22m) 👤 Dries Buytaert 💬 1591 🔖 #llm, #foss, #llm-devimpact 🗓️ 2026-01-30
    > **Резюме:** AI makes it easier to contribute to Open Source but creates more work for maintainers who must check quality. Some projects, like curl, face many low-value AI-generated reports, causing stress and burnout. With care and testing, AI can help maintainers, but protecting them is the top priority.
- [Что джуну без опыта показать на собеседовании: вклад в open source или пет-проекты / Хабр](https://habr.com/ru/companies/yandex_praktikum/articles/725694/) [📖](https://read.readwise.io/read/01jbyg6nhv6bxqpgy64t0bkkd1) 👤 Артур 💬 1795 🔖 #foss, #career 🗓️ 2024-03-15
    > **Резюме:** Привет! Меня зовут Артур Домбровский, и я наставник и соавтор курса «Java-разработчик» в Яндекс Практикуме. Зарабатываю на жизнь программированием уже более 7 лет, из которых больше трёх провёл в...
- [Mental Health in Open Source](https://antfu.me/posts/mental-health-oss) [📖](https://read.readwise.io/read/01jbyg6nf8cq24k10t24atfgph) 👤 Anthony Fu 💬 3263 🔖 #foss 🗓️ 2024-03-18
    > **Резюме:** The writer reflects on their experience with open source over four years, discussing challenges like burnout, unpreparedness, and managing expectations. They emphasize the importance of taking breaks, seeking help, and setting realistic goals. The writer also shares insights on balancing work and hobbies, maintaining project quality, and managing capacity to avoid burnout.
- [Maintaining Balance for Open Source Maintainers | Open Source Guides](https://opensource.guide/maintaining-balance-for-open-source-maintainers/) [📖](https://read.readwise.io/read/01jbyg6n5f1etzd3sphp992nh1) 👤 opensource.guide 💬 1608 🔖 #foss 🗓️ 2024-03-18
    > **Резюме:** Maintaining balance is crucial for open source maintainers as their projects grow in popularity. To understand the experiences of maintainers and their strategies for finding balance, a workshop was conducted with 40 members of the Maintainer Community. The concept of personal ecology, which involves maintaining balance and efficiency, was emphasized during the workshop. Burnout is a common issue among maintainers, leading to a lack of motivation and empathy. By embracing personal ecology, maintainers can prioritize self-care, avoid burnout, and contribute effectively to the open source community. Tips for self-care include reflecting on motivations, identifying causes of stress, watching out for signs of burnout, seeking support from the community, exploring funding options, using tools to automate tasks, taking time to rest and recharge, and setting boundaries.
- [About Yak Shaving](https://antfu.me/posts/about-yak-shaving) [📖](https://read.readwise.io/read/01jbyg6n424pfvwbn6maa6p336) 👤 Anthony Fu 💬 1813 🔖 #foss 🗓️ 2024-03-18
    > **Резюме:** The document discusses the concept of Yak Shaving, which refers to getting sidetracked from a main task by pursuing a series of smaller tasks. The author shares personal experiences with Yak Shaving in their open-source projects, highlighting how it can lead to unexpected outcomes and valuable learning experiences. They provide advice on embracing Yak Shaving as a motivation source, identifying and solving problems effectively, and refining projects iteratively. The document emphasizes the importance of focusing on solving real issues, being resourceful, and continuously improving projects while staying motivated and open to new challenges.
- [How to Contribute to Open Source | Open Source Guides](https://opensource.guide/how-to-contribute/) [📖](https://read.readwise.io/read/01jbyg6n2fpt0peww55sjyd5j1) 👤 opensource.guide 💬 4126 🔖 #foss 🗓️ 2024-03-18
    > **Резюме:** Contributing to open source projects is a rewarding way to learn and build skills. You can contribute in various ways, not just by writing code. Remember to find welcoming projects and communicate effectively when contributing.
- [The Dark Side of Open Source - kettanaito.com](https://kettanaito.com/blog/the-dark-side-of-open-source) [📖](https://read.readwise.io/read/01jbyg6n17jp9dh30ez9m0f724) 👤 kettanaito.com 💬 2068 🔖 #foss 🗓️ 2024-03-18
    > **Резюме:** Contributing to open source is often seen as a positive experience, but there are challenges and realities that are often overlooked. Open source projects can become products and require branding and marketing efforts. Financial sustainability can be a concern for open source authors, as voluntary sponsorships are rare. It is important for authors to plan for the future and establish a healthy balance between open source work and personal life. Despite the challenges, open source is still a valuable learning experience and a place to make a positive impact.
