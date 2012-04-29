#!/usr/bin/perl
use strict;
use warnings;

use Switch;

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
    case(7) { @outputArray = ("p","q","r"); }
    case(8) { @outputArray = ("t","u","v"); }
    case(9) { @outputArray = ("w","x","y"); }
    else    { @outputArray = (); }
  }

  return (@outputArray);
}

sub findPossibleWords
{
  my (@remainingDigits, @wordSoFar) = @_;

  print "Entering function with r: @remainingDigits, w: @wordSoFar";

  if (scalar(@remainingDigits) == -1)
  {
     print "word: @wordSoFar\n";
  }
  else
  {
    my $nextDigit = $remainingDigits[0];
    print scalar(@remainingDigits);
    shift(@remainingDigits);
    print scalar(@remainingDigits);
    my @translationResult = translateNumber($nextDigit);
    foreach my $item (@translationResult)
    {
      my @localWord = @wordSoFar;
      push(@localWord,$item);
      print "localWord: @localWord\n";
      findPossibleWords(@remainingDigits,@localWord);
    }
  }
}

print "\n" .
      "This script takes a string of numbers and prints a list \n" .
      "of valid words that can be created with those numbers.\n" .
      "\n";

print "Input: ";

chomp(my $userInput = <>);

if ( $userInput =~ m/^[0-9]+$/ )
{
  my @charArray = split('',$userInput);

  print "@charArray\n";

  my @progress = ();

  findPossibleWords(@charArray,@progress);
}
else
{
  print "\nMalformed input \"$userInput\", must be digits only\n\n";
}
