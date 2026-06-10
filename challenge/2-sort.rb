#!/usr/bin/env ruby

args = ARGV

# yalnız rəqəmləri götür (C, fun kimi stringləri çıxarır)
numbers = args.select { |a| a =~ /^-?\d+$/ }.map(&:to_i)

puts numbers.sort.reverse
