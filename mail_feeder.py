import subprocess

def process_junk_mail(start, end, procmailrc_path):
    # Loop through the range of file numbers
    for i in range(start, end + 1):
        # Construct the file name dynamically
        input_file_path = f'/junkMail/junkMail_{i}'
        
        # Define the command to run procmail with the current file
        command = f'procmail {procmailrc_path} < {input_file_path}'
        
        # Execute the command
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check the outcome and print relevant information
        if result.returncode == 0:
            print(f"Processed {input_file_path} successfully.")
        else:
            print(f"Error processing {input_file_path}: {result.stderr.decode()}")

process_junk_mail(0, 74, '.procmailrc')
