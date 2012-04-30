#!/usr/bin/perl
use strict;
use warnings;

use Switch;
use Text::Aspell;

my $speller = Text::Aspell->new;
die unless $speller;
$speller->set_option('lang','en_US');
$speller->set_option('sug-mode','fast');

sub printIntro
{
  print "\n" .
        "This script takes a string of numbers and prints a list \n" .
        "of valid words that can be created with those numbers.\n" .
        "\n";
}

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
  my ($ref_remainingDigits, $ref_wordSoFar) = @_;
  my @remainingDigits = @{$ref_remainingDigits};
  my @wordSoFar = @{$ref_wordSoFar};

  if (scalar(@remainingDigits) == 0)
  {
     my $result = join ("",@wordSoFar);
     if ( $speller->check($result) )
     {
       print "word: $result\n";
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
      findPossibleWords(\@remainingDigits, \@localWord);
    }
  }
}

printIntro();
print "Input: ";

chomp(my $userInput = <>);

if ( $userInput =~ m/^[0-9]+$/ )
{
  my @charArray = split('',$userInput);
  my @progress = ();
  findPossibleWords(\@charArray,\@progress);
}
else
{
  print "\nMalformed input \"$userInput\", must be digits only\n\n";
}
