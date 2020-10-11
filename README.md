# run-remote
Sets of scripts to run experiments in a remote machine in a (hopefully) smoother way

## Running conda environment
`copy_env.sh` creates a copy of a `macOS` conda environment in a given `repository` in the path `env/environment_macos.yaml`

Example:
```
copy_env.sh my_cloned_repo
```

## Setting up conda environment
`setupt_environments.sh` creates a conda environment from `env/environment_ubuntu.yaml` and adds it to the ipython kernell lists.

There might be some errors in the build depending how the original `env/environment_macos.yaml` was saved. You would just need to see what the problematic libraries are and delete those lines from `env/environment_ubuntu.yaml`

## Telegram bot sidekick
`telegram-bot.py` creates a telegram bot that looks after a `log` file and will let you know when an experiment has ended or will reply you with the latest log prints. The neccesary information about the bot and the log file information should be stored in `credentials.py`. A template `credentials_template.py` is provided.

