# huntington_hill

This is a Python 3 implementation of the _Method of Equal Proportions_, also known as the
[Huntington–Hill method](https://en.wikipedia.org/wiki/Huntington–Hill_method). This is the current
method of congressional apportionment used by the United States. Apportionment is the process by which
the US calculates how many congressional representatives each state has, using their population to
arrive at a number.

It would seem as if this should be a very simple process, in which either there should be one representative
for each multiple of some fixed value, or that the number of representatives should be based on a pie slice
of the total number based on the fraction of the population contained in that state.

However, apportionment has a considerable history (as described in the
[Wikipedia Article on the Topic](https://en.wikipedia.org/wiki/United_States_congressional_apportionment)),
and the current system, arrived at after many methods were tried over more than two centuries,
is not nearly so simple, and is kind of confusing to describe.

The purpose of this implementation is to try to make it simpler to understand what this
method is, and how it works, by turning it into relatively simple, readable Python code.
