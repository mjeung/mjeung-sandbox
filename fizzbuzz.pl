#!/usr/bin/perl

# This should be the output
#
#1
#2
#Fizz
#4
#Buzz
#6
#7
#8
#Fizz
#Buzz
#11
#Fizz
#13
#14
#FizzBuzz

# If it's divisible by 5, say Buzz instead
# If it's divisible by 3 and 5, say FizzBuzz
# If you screw up, you must consume your drink

    for($number = 1; $number <= 1000000; $number++)
    {
       # If it's divisible by 3, say Fizz instead
       if ( $number % 3 == 0 && $number % 5 == 0 )
       {
         print "FizzBuzz\n";
       }
       elsif ( $number % 3 == 0 )
       {
         print "Fizz\n";
       }
       elsif ( $number % 5 == 0 )
       {
         print "Buzz\n";
       }
       else
       { 
         print $number . "\n";
       }
    }



