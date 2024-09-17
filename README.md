
# PhDs.io

[PhDs.io] is a platform dedicated to helping finance research students and academics navigate the literature.

It is developed by Dr. [__Mingze Gao__](https://mingze-gao.com) from the __Department of Applied Finance__ at __Macquarie Business School__.

## Maintainers

This site is collectively maintained by:

1. [Mingze Gao](https://mingze-gao.com) (Macquarie University)
2. Haocheng Xu (University of Iowa)
3. [Jun He](https://www.nhh.no/en/employees/faculty/jun-he/) (NHH Norwegian School of Economics)

___If you would like to join this effort, please kindly let me know.___

## Technology

[PhDs.io] is built with [KerkoApp], a web application that uses [Kerko] to provide a user-friendly search and browsing interface for sharing a bibliography managed with the [Zotero] reference manager.

KerkoApp is built in [Python] with the [Flask] framework. It is just a thin container around Kerko and, as such, inherits most of its features directly from Kerko. However, it adds support for [TOML] configuration files, allowing a good separation of configuration from code.

## Contact

If you identify any issue, please contact [mingze.gao@mq.edu.au](mailto:mingze.gao@mq.edu.au).

[PhDs.io]: https://phds.io
[Kerko]: https://github.com/whiskyechobravo/kerko
[KerkoApp]: https://github.com/whiskyechobravo/kerkoapp
[Flask]: https://pypi.org/project/Flask/
[Python]: https://www.python.org/
[TOML]: https://toml.io/
[Zotero]: https://www.zotero.org/
