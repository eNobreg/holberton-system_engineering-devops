#!/usr/bin/env ruby
#Just a comment
puts ARGV[0].scan(/(?:from:|to:|flags:)(.+?(?=\]))/).join(',')
# ("?:from:|to:|flags:")(.+?(?=\]))
