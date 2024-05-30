import tempfile
import os
import time
import shutil

# Function to simulate processing an input file
def process_input_file(input_file):
    time.sleep(1)  
    return f"Processed {input_file}"

# Function to generate output file based on input file
def generate_output_file(input_file):
    output_file = input_file.replace(".in", ".out")
    with open(output_file, 'w') as f:
        f.write(f"Output for {input_file}")
    return output_file

# Function to compare performance
def compare_performance(input_files, ram_input_dir, disk_input_dir):
    ram_times = []
    disk_times = []
    
    for input_file in input_files:
        start_time = time.time()
        process_input_file(os.path.join(ram_input_dir, input_file))
        ram_time = time.time() - start_time
        ram_times.append(ram_time)
        
        start_time = time.time()
        process_input_file(os.path.join(disk_input_dir, input_file))
        disk_time = time.time() - start_time
        disk_times.append(disk_time)
    
    return ram_times, disk_times

# Function to write performance results to a text file
def write_performance_results(ram_input_dir, disk_input_dir, input_files, ram_times, disk_times):
    with open("task-mat-cache-parallel-testing.txt", 'w') as f:
        f.write("Regular Implementation vs Parallel Implementation\n\n")
        for i, input_file in enumerate(input_files):
            f.write(f"File: {input_file}\n")
            f.write(f"RAM Time: {ram_times[i]:.2f} seconds\n")
            f.write(f"Disk Time: {disk_times[i]:.2f} seconds\n")
            f.write("-" * 30 + "\n")

    with open("task-mat-cache-parallel-ram-testing.txt", 'w') as f:
        f.write("RAM Disk vs Disk-based Input Directory\n")
        f.write(f"RAM Input Directory: {ram_input_dir}\n")
        f.write(f"Disk Input Directory: {disk_input_dir}\n\n")
        for i, input_file in enumerate(input_files):
            f.write(f"File: {input_file}\n")
            f.write(f"RAM Time: {ram_times[i]:.2f} seconds\n")
            f.write(f"Disk Time: {disk_times[i]:.2f} seconds\n\n")


def main():
    # Create a temporary directory for RAM-based input
    ram_input_dir = tempfile.mkdtemp()
    print(f"RAM Input Directory: {ram_input_dir}")
    
    # Create a directory for disk-based input (adjust path as needed)
    disk_input_dir = "C:\\path\\to\\disk\\input"
    os.makedirs(disk_input_dir, exist_ok=True)
    print(f"Disk Input Directory: {disk_input_dir}")
    
    # Create some mock input files for testing
    input_files = ["mat96.in", "mat512.in", "mat10020.in"]
    for input_file in input_files:
        with open(os.path.join(ram_input_dir, input_file), 'w') as f:
            f.write(f"Sample content for {input_file}")
        with open(os.path.join(disk_input_dir, input_file), 'w') as f:
            f.write(f"Sample content for {input_file}")
    
    # Process input files and generate output files
    for input_file in input_files:
        processed_result = process_input_file(os.path.join(ram_input_dir, input_file))
        output_file = generate_output_file(input_file)
        print(processed_result)
        print(f"Generated {output_file}")
    
    # Compare performance between RAM and disk-based input
    ram_times, disk_times = compare_performance(input_files, ram_input_dir, disk_input_dir)
    
    # Write performance comparison results to text files
    write_performance_results(ram_input_dir, disk_input_dir, input_files, ram_times, disk_times)
    
    # Clean up: delete the temporary directory
    shutil.rmtree(ram_input_dir)
    print(f"Cleaned up RAM Input Directory: {ram_input_dir}")

if __name__ == "__main__":
    main()
