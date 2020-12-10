#!/usr/bin/perl -w

# Written by Alejandro Reyes

# Usage: Parse_CD-Hit.pl <file.clstr> > <output>


use strict;

unless (@ARGV == 1) {
  die "\nUsage: Parse_CD-Hit.pl <file.clstr>  > <output>\n\n";
}

my $file = shift @ARGV;


#Reads the lowest file

open (IN, "<$file") or die ("Couldn't open file: $file\n");

my %cluster = ();
my $sample="";
my $name ="";
my %id =();
my %convert=();

while (my $lines=<IN>) {
  chomp $lines;
  $name=$lines if ($lines =~/^>/);
  $name=~s/>//;
  if ($lines =~ /^\d/){
    my @elements = split (/\s+/, $lines);
    $elements[2]=~/>(.+)\.\.\./;
    my $seg=$1;
    my @parts = split /\|/, $seg;
    $sample=$parts[0];
    $convert{$name}=$seg if ($lines =~ /\*$/);
    $id{$sample}=1;
    $cluster{$name}{$sample}++;
  }
}
close IN;

my @ids=sort(keys (%id));
#Reads the Fasta Sequences
print "Sample\t";
foreach my $a (@ids){
  print "$a\t";
}
print "\n";

foreach my $key (keys (%cluster)){	
  #print "$counter\t";
  print "$convert{$key}";
  foreach my $a (@ids){
    if ($cluster{$key}{$a}){
      print "\t$cluster{$key}{$a}";
    }else{
      print "\t0";
    }
  }
  print "\n";
}
