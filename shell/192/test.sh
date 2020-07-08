# Read from the file words.txt and output the word frequency list to stdout.
#0:50AC
awk '{split($0,a," ");for(t in a){cnt[a[t]]+=1}} END{for(k in cnt){printf("%s %d\n",k, cnt[k]);}}' words.txt | sort -k2nr
