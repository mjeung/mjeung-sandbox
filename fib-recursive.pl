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
}

###############################################################################

sub fib
{
  my ($n) = @_;
  my $ret;

  if ($n == 0)
  {
    $ret = 0;
  }
  elsif ($n == 1 || $n == 2)
  {
    $ret = 1; 
  }
  else
  {
    $ret = fib($n-1) + fib($n-2);
  }

  $ret;
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
  print "result: " . fib($input);
  print "\n";
}
else
{
  printUsage();
  print "Malformed input \"$input\", must be digits only\n\n";
}
