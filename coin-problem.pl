#!/usr/bin/perl

use strict;
use warnings;

###############################################################################

sub printUsage
{
  print "usage: ./coin-problem.pl <number>\n";
}

###############################################################################

sub minChange
{
  my ($m) = @_;
  my $ret;

  $ret = 99999;
  if ($m == 0)
  {
    $ret = 0;
  }
  else
  {
    my $tmp_answer = 99999;
    foreach my $coin (1, 3, 4, 5)
    {
      if ($m >= $coin)
      {
        my $return = (1 + minChange($m - $coin));
        if ($tmp_answer > $return)
        {
          $tmp_answer = $return;
        }
      }
    }

    $ret = $tmp_answer;
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
  print "result: " . minChange($input);
  print "\n";
}
else
{
  printUsage();
  print "Malformed input \"$input\", must be digits only\n\n";
}
