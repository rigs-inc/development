## Phase 1 - Environment Setup

The first phase though its primary goal is to help you in the configuration of services & tools used in our day-to day tasks, is to start getting familiar with `bash` and `shell` terminal.

At-the bottom of this document, you will find the `To Learn` Section, which lists concepts and shell commands used in this configuration roadmap.

### Requirements

- The setup MUST be completed using the shell terminal.
- Your tech lead must provide you, with all the source files used in this setup.

### Setup software stack

Recommended software list.

- sublime text 3 (IDE for coding)
- iterm2 (shell terminal)
- spectacle (mac os ui manager)
- chrome
- slack

### Sublime Text Setup

One of our favorite feats from sublime are the Them, so our recommendation is the `Spacegray Them`

To install it, first install the [package control](https://packagecontrol.io/installation), then search for this them using the `install package` option

Add this to user settings as part of the JSON.
```
"theme": "Spacegray.sublime-theme",
"color_scheme": "Packages/Theme - Spacegray/base16-ocean.dark.tmTheme"
```

**Install Linters**

- [SublimeLinter](http://sublimelinter.readthedocs.io/en/latest/installation.html)
- [SublimeLinter-jshint](https://github.com/SublimeLinter/SublimeLinter-jshint)
- [SublimeLinter-pep8](https://github.com/SublimeLinter/SublimeLinter-pep8)
- [SublimeLinter-phplint](https://github.com/SublimeLinter/SublimeLinter-phplint)

--------

### SSH Key & Bitbucket Setup

To be able to clone remote repositories, in this case, bitbucket, you first need-to generate an ssh key and copy the public key content to clipboard.

```
ssh-keygen && eval "ssh-agent" && ssh-add -K ~/.ssh/id_rsa && cat ~/.ssh/id_rsa.pub
```

Now, the admin has to add the key to bitbucket, and then you can start clonning.

--------

### Rigs Credentials, Environment variables & aliases

**Rigs Credentials**

- Open the terminal and from the root path create the `.rigs` folder; `mkdir ~/.rigs`
- Copy the 2 files from `<source-folder>/config` folder inside the previous one created.
- If you list the contents from `~/.rigs`, it has to display; `config.sh credentials`.

**Environment Variables & Aliases Setup**

Open the terminal and create the `.bash_profile`. Assuming that you had installed sublime text, create the shell `subl` command.

- Create local bin folder `mkdir /usr/local/bin`
- Create symlink `ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl`

Now just run `subl ~/.bash_profile`, then copy the contents from `<source-folder>/bin/bash_profile`.

Once completed the previous step, run `source ~/.bash_profile`

--------

### MongoDB Setup

To install MongoDB follow this [instructions](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)

Once installation completed, load the settings file into your local engine; `mongo < <source-folder>/mongo/mongo_configuration.js`

--------

### Useful Services & Tools

- Install `GIT`
- Install `nodejs - npm`
- Install `aws-cli`
- Install `brew`

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

--------

## To learn

- ssh
- man
- ls
- ln
- cat
- mkdir
- curl
- ssh-keygen
