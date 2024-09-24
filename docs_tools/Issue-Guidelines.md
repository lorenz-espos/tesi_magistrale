# Issues:

These are general guidelines for opening productive issues. If you don't follow them, we can't help you.

## _Mandatory_ requirements:
- Please be as detailed as possible.
     - "It doesn't work" is not a helpful issue.
     - Provide information about your environment:
         - What OS are you running (must be [officially supported](https://github.com/n1nj4sec/pupy/wiki/Supported-Operating-Systems))
         - How did you install Pupy? I.e. Docker compose (standard way to install), virtualenv, or the pre-built Docker image?
         - What specific commit are you using? Did you pull the latest version of Pupy from the master branch before running it?
- Please provide logs or detailed errors produced by the issue.
     - You can provide screenshots, code snippets, logs created by the `script <logfile>` command, asciinema recordings, etc.
     - For detailed information about how to correctly log output from these programs, see the logging section.
- Edit your original post rather than creating multiple new ones in succession.
- Use proper markdown formatting for code snippets with backticks.
     - See the [GitHub guide to Markdown](https://guides.github.com/features/mastering-markdown/).
- For long code segments or logs, please create a [gist](https://gist.github.com) and paste the link to it in the issue.
- Ensure that you are using a [supported operating system](https://github.com/n1nj4sec/pupy/wiki/Supported-Operating-Systems).
- Before reporting an issue, please update your OS, pull the latest commit and verify that it is still an issue afterwards.


## Optional guidelines:
- If possible, please use proper English grammar and spelling.
     - If we cannot understand you, we cannot fix your problem.
- If possible and convenient, please reproduce your issue in a freshly installed, fully updated VM. This VM must be a supported operating system.

## Logging:

- [Asciinema](https://asciinema.org/):
     - To install: `sudo pip3 install asciinema`
     - To record: `asciinema rec -i 2 <output-file>.cast`
     - Run whichever commands are required to reproduce the issue.
     - Type `exit` to stop the recording.
     - To upload: `asciinema upload <output-file>.cast`
     - Paste the resulting link into your issue.

- Script:
     - `script <output-log-file>`
     - Run whichever commands are required to reproduce the issue.
     - Type `exit`
     - Copy the contents of the output file and create a gist.
     - Paste that gist into your issue.

- Strace:
     - Run `strace -ff -o <output-file> <program to run and arguments for it>`

## Closing issues:
- Please _close the issue_ if it has been fixed or your question has been answered.
