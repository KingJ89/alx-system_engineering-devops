#!/usr/bin/env ruby
input = ARGV[0]regex = /[A-Z]/matches = input.scan(regex)puts matches.join
