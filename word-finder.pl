#!/usr/bin/perl

print "\n" .
      "This script takes a string of numbers and prints a list \n" .
      "of valid words that can be created with those numbers.\n" .
      "\n";

print "Input: ";

chomp($user_input = <>);

if ( $user_input =~ m/^[0-9]+$/ )
{
  print $user_input . "\n";
}
else
{
  print "\nMalformed input \"$user_input\", must be digits only\n\n";
}
