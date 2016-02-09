# babypandas
A facade on top of Pandas to present a more beginner friendly and opinionated class API

**Examples**

Can be found in babypandas_api.ipynb

**Motivations**

Pandas is a "Flexible and powerful data analysis / manipulation library for Python" that introduces a dataframe to Python. 

Its power and flexibility, however, give it a long learning curve. How can we reduce this learning curve?

* Pandas has a huge class API, about 400 public methods for DataFrame and Series, while in practice people only use about 25% of these
* Pandas has many ways to reach the same goals, this flexibility is useful and allows experienced users to work quickly, but puts an unnecessary burden on beginning users
* Pandas also does not make much effort in preventing users from selecting clearly wrong approaches that reinvent other Pandas methods
* A thorough look at online code samples seems to suggest that most Pandas users actually are beginning users and have not read much of the documentation
* Pandas has a great set of guidelines scattered throughout its documentation, but it's too bad no one reads them, these can be enforced in the library itself
* Pandas docstrings don't have code examples

These suggestions are inspired by the Zen of Python and strangely enough, the Pandas documentation itself.
