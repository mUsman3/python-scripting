import subprocess
import os
import random
import string

def run_git_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def create_dummy_file():
    # Generate a random filename
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '.txt'
    
    # Generate random content for the file
    content = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=100))
    
    # Write the content to the file
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"Created dummy file: {filename}")
    return filename

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to that directory
    os.chdir(script_dir)

    # Create a dummy file
    dummy_file = create_dummy_file()

    # Stage all changes
    print("Running git add .")
    run_git_command(['git', 'add', '.'])

    # Commit the changes
    commit_message = f"Add dummy file {dummy_file}"
    print(f"Running git commit -m \"{commit_message}\"")
    run_git_command(['git', 'commit', '-m', commit_message])

    # Push to the main branch
    print("Running git push origin main")
    run_git_command(['git', 'push', 'origin', 'main'])

if __name__ == "__main__":
    main()
