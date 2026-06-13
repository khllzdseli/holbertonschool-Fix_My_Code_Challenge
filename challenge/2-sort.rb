#!/usr/bin/env ruby
# Sorts passed arguments that are numerical and prints them

result = []
ARGV.each do |arg|
    # Check if the argument is a valid integer (including negative numbers)
    if arg =~ /^-?[0-9]+$/
        result << arg.to_i
    end
end

# Sort the integers and print each on a new line
puts result.sort
