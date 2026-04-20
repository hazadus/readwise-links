# Ссылки

- Всего ссылок: 3

## Ссылки

- [A toy DNS resolver](https://jvns.ca/blog/2022/02/01/a-dns-resolver-in-80-lines-of-go/) [📖](https://read.readwise.io/read/01jbyg6qq6kbq7j10v58my73x8) 👤 Julia Evans 💬 2551 🔖 #dns 🗓️ 2024-03-03
    > **Резюме:** This post explains how DNS resolvers work through a short Go program that performs the same task as explained in a previous comic. DNS resolvers are used by browsers to obtain DNS records. The program uses a library for parsing DNS packets and contains four sections in DNS responses: Question, Answer, Authority, and Additional. The resolve function is the main function for resolving a name to an IP address, and it works by querying a nameserver and parsing the response. The resolver prints out all DNS queries it made and the records used to determine the next query.
- [Let’s hand write DNS messages | James Routley](https://web.archive.org/web/20180919041301/https://routley.io/tech/2017/12/28/hand-writing-dns-messages.html) [📖](https://read.readwise.io/read/01jbyg6qfcc71mhfbt9e4j196z) 👤 james_routley 💬 1903 🔖 #dns, #python 🗓️ 2024-03-04
    > **Резюме:** In this post, we’ll explore the Domain Name Service (DNS) binary message format, and we’ll write one by hand. This is deeper than you need to use DNS, but I think it’s fun and educational to see how these things work under the hood.
- [The multiple meanings of "nameserver" and "DNS resolver"](https://jvns.ca/blog/2022/02/14/some-dns-terminology/) [📖](https://read.readwise.io/read/01jbyg6q3mv5dhpsx1m1znfkw3) 👤 Julia Evans 💬 988 🔖 #dns 🗓️ 2024-03-06
    > **Резюме:** The terms "nameserver" and "DNS resolver" have different meanings depending on the context of DNS. A "nameserver" can refer to either an authoritative server that stores DNS records or a recursive server that helps find those records. Understanding these meanings is important for anyone learning about DNS, as the terminology can be confusing.
