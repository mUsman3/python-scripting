import subprocess
import os

def run_git_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to that directory
    os.chdir(script_dir)

    # Stage all changes
    print("Running git add .")
    run_git_command(['git', 'add', '.'])

    # Commit the changes
    commit_message = input("Enter commit message: ")
    print(f"Running git commit -m {commit_message}")
    run_git_command(['git', 'commit', '-m', commit_message])

    # Push to the main branch
    print("Running git push origin main")
    run_git_command(['git', 'push', 'origin', 'main'])

if __name__ == "__main__":
    main()
