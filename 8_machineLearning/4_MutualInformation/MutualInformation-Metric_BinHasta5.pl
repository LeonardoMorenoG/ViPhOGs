#!/usr/bin/perl -w

# Written by Alejandro Reyes

use strict;

if (@ARGV != 1) {
	die "\nUsage: MutualInformation-Metric_NucFreq.pl Matrix1 > Outfile \n\n";
}


my $file =shift;
open (IN, "<$file") or die ("Couldn't open file: $file\n");

my %matrix1=();

my $trash1=<IN>;
chomp $trash1;
my @names = split /\s+/, $trash1;
shift @names;
my $size=0;

while (my $line=<IN>){
  next unless ($line =~ /\w+/);
  chomp $line;
  my @entry=split /\t/, $line;
  my $t = shift @entry;
  die ("Not same number of columns as names in row $size\n") unless (length(@entry)==length(@names));

  for (my $i=0; $i<@entry; $i++){						### arrayed based on Names
    if ($entry[$i]>5){ $matrix1{$names[$i]}[$size]=5;}
	else{
	$matrix1{$names[$i]}[$size]=$entry[$i];
    }
  }
  $size++;
}
close IN;

print "Matrix";
for (my $k=0; $k<@names; $k++){
  print "\t$names[$k]";
}print "\n";

for (my $i=0; $i<@names; $i++) {
  print "$names[$i]";
  for (my $j=0; $j<@names; $j++){
    #print "Analyzing MI on $names[$i] and $names[$j]\n";
    my $p= &MI (\@{$matrix1{$names[$j]}}, \@{$matrix1{$names[$i]}}, $size);
    printf ("\t%.4f", $p);
  }
  print "\n";
}



sub MI {
  my @arr1=@{$_[0]};
  my @arr2=@{$_[1]};
  my $size=$_[2];
  
  my %countx=();
  my %county=();
  my %countxy=();
  
  for (my $i=0; $i<@arr1; $i++){
    $countx{$arr1[$i]}++;
    $county{$arr2[$i]}++;
    $countxy{"$arr1[$i],$arr2[$i]"}++;
  }
  
  my $MI=0;
  my $entropyX=0;
  my $entropyY=0;
  my $entropyXY=0;
  
  foreach my $p (keys %countx){
    $entropyX += ($countx{$p}/$size)*(log($countx{$p}/$size)/log(2));
  }
  foreach my $p (keys %county){
    $entropyY += ($county{$p}/$size)*(log($county{$p}/$size)/log(2));
  }
  
  foreach my $k (keys %countxy){
    $entropyXY+= ($countxy{$k}/$size)*(log($countxy{$k}/$size)/log(2));
    my @array = split /\,/, $k;
    $MI += ($countxy{$k}/$size) * (log(($countxy{$k}*$size)/($countx{$array[0]}*$county{$array[1]}))/log(2));
  }
  #print "\tEntropyX: $entropyX\tEntropyY: $entropyY\tEntropyXY: $entropyXY\tMI: $MI\n";
  my $distance=((-$entropyX-$entropyY-(2*$MI))/-$entropyXY);
  return $distance;
}
		
	
	
