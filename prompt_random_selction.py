import random  # For shuffling prompts
import tkinter as tk  # GUI library
from tkinter import filedialog, simpledialog  # Dialog boxes for file selection and input

def divide_prompts(input_file, output_folder):
    """Divides the prompts from the input file into two separate output files."""
    with open(input_file, 'r') as file:
        # Read the file content and split prompts by double newline
        content = file.read().strip()  
        prompts = content.split('\n\n')  

    random.shuffle(prompts)  # Shuffle the prompts randomly
    total_prompts = len(prompts)  # Get the total number of prompts
    prompts_in_file1 = total_prompts // 2  # Calculate number of prompts for each file

    prompts_file1 = prompts[:prompts_in_file1]  # Get prompts for the first file
    prompts_file2 = prompts[prompts_in_file1:]  # Get prompts for the second file

    # Define output file paths
    output_file1 = output_folder + '/output1.txt'
    output_file2 = output_folder + '/output2.txt'

    # Write prompts to the output files
    with open(output_file1, 'w') as file1:
        file1.write('\n\n'.join(prompts_file1))

    with open(output_file2, 'w') as file2:
        file2.write('\n\n'.join(prompts_file2))

    # Print messages indicating the creation of the output files
    print(f"File '{output_file1}' created with {len(prompts_file1)} prompts.")
    print(f"File '{output_file2}' created with {len(prompts_file2)} prompts.")

def create_multiple_files(prompts, output_folder, num_files):
    """Creates multiple output files containing prompts."""
    random.shuffle(prompts)  # Shuffle the prompts randomly
    total_prompts = len(prompts)  # Get the total number of prompts
    prompts_per_file = total_prompts // num_files  # Calculate prompts per file
    extra_prompts = total_prompts % num_files  # Calculate extra prompts for some files
    
    start_index = 0  # Initialize start index for prompts
    for i in range(num_files):
        end_index = start_index + prompts_per_file + (1 if i < extra_prompts else 0)  # Calculate end index
        prompts_subset = prompts[start_index:end_index]  # Get subset of prompts for the file
        output_file = f"{output_folder}/output{i + 1}.txt"  # Define output file path
        with open(output_file, 'w') as file:
            file.write('\n\n'.join(prompts_subset))  # Write prompts to the file
        print(f"File '{output_file}' created with {len(prompts_subset)} prompts.")  # Print creation message
        start_index = end_index  # Update start index for next file

def select_files():
    """Allows the user to select an input file and output folder for dividing prompts into two files."""
    input_file = filedialog.askopenfilename(title="Select Input File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    output_folder = filedialog.askdirectory(title="Select Output Folder")

    if input_file and output_folder:
        divide_prompts(input_file, output_folder)

def select_multiple_files():
    """Allows the user to select an input file and output folder for dividing prompts into multiple files."""
    input_file = filedialog.askopenfilename(title="Select Input File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not input_file or not output_folder:
        return
    
    num_files = simpledialog.askinteger("Input", "How many output files?", minvalue=2)
    if not num_files:
        return

    with open(input_file, 'r') as file:
        content = file.read().strip()
        prompts = content.split('\n\n')

    create_multiple_files(prompts, output_folder, num_files)

def select_random_prompts():
    """Allows the user to select an input file and output folder for selecting random prompts."""
    input_file = filedialog.askopenfilename(title="Select Input File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not input_file or not output_folder:
        return

    num_prompts = simpledialog.askinteger("Input", "How many prompts to select?", minvalue=1)
    if not num_prompts:
        return

    with open(input_file, 'r') as file:
        content = file.read().strip()
        prompts = content.split('\n\n')

    if num_prompts > len(prompts):
        print("The number of prompts requested exceeds the total number of prompts available.")
        return

    random_selected_prompts = random.sample(prompts, num_prompts)
    output_file = f"{output_folder}/randomly_selected_prompts.txt"
    
    with open(output_file, 'w') as file:
        file.write('\n\n'.join(random_selected_prompts))
    print(f"File '{output_file}' created with {num_prompts} randomly selected prompts.")

# Create the GUI window
root = tk.Tk()
root.title("Select Input File and Output Folder")

# Add a button to select files for 2 outputs
button = tk.Button(root, text="Select Files for 2 Outputs", command=select_files)
button.pack()

# Add a button to select multiple files
multi_button = tk.Button(root, text="Select Files for Multiple Outputs", command=select_multiple_files)
multi_button.pack()

# Add a button to select random prompts
random_button = tk.Button(root, text="Select Random Prompts", command=select_random_prompts)
random_button.pack()

# Run the GUI
root.mainloop()
