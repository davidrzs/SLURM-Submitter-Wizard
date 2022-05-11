import os


config = {}

print(os.popen("whoami").read())




def number_of_running_jobs(config):
    os.popen(f'squeue -u {config["username"]}').read()





if __name__ == '__main__':
    config = {}
    uncleaned_name = os.popen("whoami").read()
    config['username'] = "".join(uncleaned_name.split())
    print(config)
