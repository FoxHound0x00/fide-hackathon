## Project description & structure.
    
# 1. `main.py` file:
# This spawns our compiled c++ bot and communicates with it.
# It acts as a bridge between kaggle's game runner and our c++ bot.

# 2. `my_chess_bot.cpp` file:
# This is the source code file of our cpp chess bot.
# While submitting we need not include this in the zip file as the compiled file is the only one required by our `main.py` file.

# 3. Compilation instructions:
# This can be useful for Windows users as kaggle runs on linux and we need to compile for linux.

# 4. Zipping instructions:
# This can be useful for submission.

# Note:
# We have "writefile" commands at the top of code of Sections 1 and 2.
# This command writes the content of that cell to a file with the given name. (This command if used must be the first line in the cell)
# Eg: %%writefile main.py writes to main.py file.
# After the cell finishes running, the file will appear in the Output tab in the right side nav bar of the notebook.
# We can download it if we want.

# However, we will write to a subfolder in the current working directory named "src" for the following reason.
# At the end, we will archive all the generated files for submission.
# And if all those files are in a separate folder other than the working directory,
# then, when the archiving command writes the compressed file to the working directory,
# it won't complain that the contents changed while writing the archive.

# Running a cpp subprogram:
# https://github.com/Lux-AI-Challenge/Lux-Design-S1/blob/master/kits/cpp/simple/main.py

# Section 2: my_chess_bot.cpp file

# CPP code prints a randomly chosen move out of available moves.
# In an infinite loop, it does the following: read input, think and set a move, print the move.
# While reading input, it expects:
#     an integer: 0 for white and 1 for black,
#     a string representing board FEN
#     a string with space separated available 

# Section 3: Compilation instructions.
# We will compile the file from within the notebook.
# The compiled file will be visible along with our main.py and my_chess_bot.cpp files written by above cells.

# The following command prints the version of g++ available
!g++ --version

# Compiling our cpp file:
!g++ src/my_chess_bot.cpp -o src/my_chess_bot.out

# Section 4: We will use tar command here to zip all required files.
# Then the tar file will appear in the Output in the right side nav bar.
# We can download the zip file and submit it.
# In the name of the zip file, we will put current datetime stamp. It looks like submission_datetimestamp.tar.gz
# We will also exclude .h, .hpp, and .cpp files from being included in the zip file
!tar --exclude='*.h' --exclude='*.hpp' --exclude='*.cpp' -czf "submission_$(date +'%Y_%m_%d_%H_%M_%S').tar.gz" -C /kaggle/working/src .

# The zip command is taken from this disussion:
# https://www.kaggle.com/competitions/fide-google-efficiency-chess-ai-challenge/discussion/547145#3050379
