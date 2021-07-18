#!/bin/bash

JAR_NAME="springboot-pt.jar"
VM_OPTIONS=""
PROGRAM_ARGS=""
for arg in $*               #在$*中遍历参数，此时每个参数都是独立的，会遍历$#次
do
  if [[ $arg == --* ]]; then
      PROGRAM_ARGS="$PROGRAM_ARGS "$arg
  else
      VM_OPTIONS="$VM_OPTIONS "$arg
  fi

done

java $VM_OPTIONS -jar "$JAR_NAME" $PROGRAM_ARGS