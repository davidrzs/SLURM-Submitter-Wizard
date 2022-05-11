# SLURM-Submitter-Wizard
A simple tool to simplify SLURM job submission for similar jobs with different parameters.

## Example Use-Case

You have access to a SLURM cluster and would like to run machine learning models with different hyperparameter configurations.

## Usage

Usage is super simple:

1. Download the `ssw.py` script.
2. Create a `ssw_config.yaml` file in same directory as script - see the example file on how to fill it.
3. Run the script with python `ssw.py`. If you are running over an SSH connection you can use `tmux` or `nohup` to keep the script running after disconnecting from the cluster. For example `nohup python ssw.py`.


## Contributions and Bugs

You are more than welcome to add bug fixes to this repo.


## License

The code is licensed under the permissive [MIT license](LICENSE).
