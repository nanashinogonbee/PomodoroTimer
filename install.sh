touch compile.py
printf "import py_compile\npy_compile.compile(\"main.py\")" > compile.py
python3 compile.py
rm compile.py
cd __pycache__
mv * ../pomodoro
cd ..
rm -rf __pycache__
chmod +x pomodoro
sudo mv pomodoro /usr/bin
printf "Done!\nType \"pomodoro\" in your Bash terminal to launch.\n"
