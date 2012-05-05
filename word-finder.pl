#!/usr/bin/perl

###############################################################################
#
# Given a string of digits, this script finds all valid words that the digits
# could be translated into using a regular telephone keypad:
#
#
#   1    2    3
#       abc  def 
#
#   4    5    6
#  ghi  jkl  mno 
#
#   7    8    9
#  pqrs tuv  wxyz   
#
#
# For example, "7672676" translates to "popcorn".
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
  print "usage: ./word-finder.pl <digits>\n";
  print "\n";
  print "try:\n";
  print "  ./word-finder.pl 7672676\n";
  print "  ./word-finder.pl 266626333\n";
  print "  ./word-finder.pl 3782254746368\n";
  print "\n";
}

###############################################################################

sub translateNumber 
{
  my ($inputNumber) = @_;

  my @outputArray;
  switch ($inputNumber) 
  {
    case(2) { @outputArray = ("a","b","c"); }
    case(3) { @outputArray = ("d","e","f"); }
    case(4) { @outputArray = ("g","h","i"); }
    case(5) { @outputArray = ("j","k","l"); }
    case(6) { @outputArray = ("m","n","o"); }
    case(7) { @outputArray = ("p","q","r","s"); }
    case(8) { @outputArray = ("t","u","v"); }
    case(9) { @outputArray = ("w","x","y","z"); }
    else    { @outputArray = (); }
  }

  return (@outputArray);
}

###############################################################################

sub printPossibleWords
{
  my ($ref_remainingDigits, $ref_wordSoFar) = @_;
  my @remainingDigits = @{$ref_remainingDigits};
  my @wordSoFar = @{$ref_wordSoFar};

  if (scalar(@remainingDigits) == 0)
  {
     my $result = join ("",@wordSoFar);
     if ( $speller->check($result) )
     {
       print "  $result\n";
     }
  }
  else
  {
    my $nextDigit = $remainingDigits[0];
    shift(@remainingDigits);
    my @translationResult = translateNumber($nextDigit);
    foreach my $item (@translationResult)
    {
      my @localWord = @wordSoFar;
      push(@localWord,$item);
      printPossibleWords(\@remainingDigits, \@localWord);
    }
  }
}

###############################################################################

### MAIN

die unless $speller;
$speller->set_option('lang','en_US');
$speller->set_option('sug-mode','fast');

if ($#ARGV != 0)
{
  printUsage();
  print "\n";
  exit;
}

my $digits = $ARGV[0];

if ( $digits =~ m/^[0-9]+$/ )
{
  my @charArray = split('',$digits);
  my @progress = ();

  print "\nFinding possible words for $digits:\n";
  printPossibleWords(\@charArray,\@progress);
  print "\n";
}
else
{
  printUsage();
  print "Malformed input \"$digits\", must be digits only\n\n";
}
