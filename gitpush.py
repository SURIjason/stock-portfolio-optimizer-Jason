import subprocess

# Step 1: Stage your updated files
subprocess.run(["git", "add", "."])  # Adds all changed files

# Step 2: Commit the changes with a message
subprocess.run(["git", "commit", "-m", "Update: latest changes to app and optimizer logic"])

# Step 3: Push to the remote repository (assuming branch is 'main')
subprocess.run(["git", "push", "origin", "main"])