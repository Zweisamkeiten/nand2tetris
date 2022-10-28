#!/bin/zsh
for i in *.diff.hack;
  do diff ${${i%.*}%.*}.hack $i;
done
