#!/usr/bin/env bash
#https://www.jianshu.com/p/d31cabc1f591
cat words.txt | sed 's/ /\n/g' | sed '/^$/d' | sort | uniq -c | awk '{print $2, $1}' | sort -nrk2
