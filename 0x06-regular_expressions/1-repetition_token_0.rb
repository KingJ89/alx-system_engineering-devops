#!/usr/bin/env ruby
#this script matches a certain repititive pattern.
puts ARGV[0].scan(/hbt{2, 5}n/).join
