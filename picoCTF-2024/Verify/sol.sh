#!/bin/bash

for file in ./files/*
do 
    bash decrypt.sh "$file"
done