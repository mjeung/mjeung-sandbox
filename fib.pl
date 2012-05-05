#!/usr/bin/perl

###############################################################################
#
# Given index N, find the Nth Fibonnacci number 
#
#  F(n) = F(n-1) + F(n-2)
#
###############################################################################

use strict;
use warnings;
use Switch;
use Text::Aspell;

### Global Spell Checker
my $speller = Text::Aspell->new;

###############################################################################

sub printUsage
{
  print "usage: ./fib.pl <number>\n";
  print "\n";
}

###############################################################################

sub printUsage
{
  print "usage: ./fib.pl <number>\n";
  print "\n";
}

###############################################################################
###############################################################################
###############################################################################

if ($#ARGV != 0)
{
  printUsage();
  print "\n";
  exit;
}

my $input = $ARGV[0];

if ( $input =~ m/^[0-9]+$/ )
{
  print fib($input);
  print "\n";
}
else
{
  printUsage();
  print "Malformed input \"$input\", must be digits only\n\n";
}
