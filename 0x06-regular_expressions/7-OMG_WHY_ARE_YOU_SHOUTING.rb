#!/usr/bin/env ruby
#Accept the argument from command line,Define the regular expression to match only capital letters,Find all occurrences of capital letters in the input string,Join the matched capital letters and output them.


input = ARGV[0]regex = /[A-Z]/matches = input.scan(regex)puts matches.join
