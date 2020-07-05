# Read from the file file.txt and output the tenth line to stdout.
#21:55AC
awk '{if(NR==10)print $0}' file.txt
