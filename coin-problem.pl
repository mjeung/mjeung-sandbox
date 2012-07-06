#!/usr/bin/perl

use strict;
use warnings;

my $globalTarget;
my %hashNumberOfCoinsForValue = ();
my %hashBestCoinCombinationForValue = ();

###############################################################################

sub printUsage
{
  print "usage: ./coin-problem.pl <number>\n";
}

###############################################################################

sub minChange
{
  my ($m, $ref_SoFar) = @_;
  my @soFar = @{$ref_SoFar};
  my $ret;

  $ret = 99999;
  if ($m == 0)
  {
    $ret = 0;
  }
#  elsif (exists $hashNumberOfCoinsForValue{$m})
#  elsif (exists $hashNumberOfCoinsForValue{$m} and exists $hashBestCoinCombinationForValue{$m})
#  {
#    $ret = $hashNumberOfCoinsForValue{$m};
#    my @BestCoinCombination = @{$hashBestCoinCombinationForValue{$m}};
#    print "Best For $m: @BestCoinCombination\n";
#    push(@soFar,@BestCoinCombination);
#  }
  else
  {
    foreach my $coin (1, 3, 5)
    {
      if ($m >= $coin)
      {
        push(@soFar,$coin);
        my $return = (1 + minChange($m - $coin, \@soFar));

        my $hashKey = $globalTarget - ($m - $coin);
        if (exists $hashBestCoinCombinationForValue{$hashKey})
        {
          my @BestCoinCombination = @{$hashBestCoinCombinationForValue{$hashKey}};
          if ( scalar(@BestCoinCombination) > scalar(@soFar) )
          {
            #print "Storing for $hashKey: @soFar\n";
            my @copyOfSoFar = @soFar;
            $hashBestCoinCombinationForValue{$hashKey} = \@copyOfSoFar;
            #displayHash();   
          }
          else
          {
            my @copyOfSoFar = @soFar;
           # print "Was going to store for $hashKey: @copyOfSoFar\n";
          }
        }
        else
        {
          #print "Storing for $hashKey: @soFar\n";
          my @copyOfSoFar = @soFar;
          $hashBestCoinCombinationForValue{$hashKey} = \@copyOfSoFar;
        }

        if ($ret > $return)
        {
          $ret = $return;
          $hashNumberOfCoinsForValue{$m} = $ret;
        }
        pop(@soFar);
      }
    }
  }

  $ret;
}

sub displayHash
{
  print "----------- \n";
  foreach my $key ( keys %hashBestCoinCombinationForValue) 
  {  
     print "$key: ";
     my @array = @{$hashBestCoinCombinationForValue{$key}};
     foreach (@array)
     {
       print "$_ "
     }
     print "\n"
  }
  print "----------- \n";
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
my @empty;

if ( $input =~ m/^[0-9]+$/ )
{
  $globalTarget = $input; 
  print "result: " . minChange($input, \@empty) . "\n";
  displayHash();   
  print "\n";
}
else
{
  printUsage();
  print "Malformed input \"$input\", must be digits only\n\n";
}
