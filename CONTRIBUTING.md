Contributing
----------------------------------

1. File an issue to notify the maintainers about what you're working on.
2. Fork the repo, develop and test your code changes, add docs.
3. Make sure that your commit messages clearly describe the changes.
4. Send a pull request.

Before writing code, file an issue
----------------------------------

Use the issue tracker to start the discussion. It is possible that someone
else is already working on your idea, your approach is not quite right, or that
the functionality exists already. The ticket you file in the issue tracker will
be used to hash that all out.

Style Guides
-------------------
1. Write in UTF-8
2. Use modular architecture to group similar functions, processes, configs etc. 
3. Always use 4 spaces for indentation (don't use tabs)
4. Try to limit line length to 120 characters
5. Function and process names should always be lowercase and use snake case
6. Configs should live in the `configs` folder
7. If a new feature cannot be tested with current test datasets, you must provide one
8. Look at the existing style and adhere accordingly

Fork the Repository
-------------------

Be sure to add the relevant tests before making the pull request. Docs will be
updated automatically when we merge to `master`, but you should also build
the docs yourself and make sure they're readable.

Make the pull request
---------------------

Once you have made all your changes, tests, and updated the documentation,
make a pull request to move everything back into the main branch of the
`repository`. Be sure to reference the original issue in the pull request.
Expect some back-and-forth with regards to style and compliance of these
rules.

Adding Dependencies
---------------------

If your changes require additional dependencies, please demonstrate the change through an
updated Docker image.