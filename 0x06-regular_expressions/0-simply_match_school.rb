#!/usr/bin env ruby
# This is a regular expressin in ruby

input = ARGV[0]

regex = /School/

match = input.match(regex)

puts match[0] if match
