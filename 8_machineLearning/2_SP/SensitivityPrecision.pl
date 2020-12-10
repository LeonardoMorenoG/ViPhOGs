#!/usr/bin/perl -w

# Written by Alejandro Reyes

use strict;

if (@ARGV != 2) {
        die "\nUsage: SensitivityPrecision.pl Matrix1 Matrix2 > Outfile \n\n";
}

# read files
my $file =shift;
open (IN, "<$file") or die ("Couldn't open file: $file\n");

my $file2 =shift;
open (IN2, "<$file2") or die ("Couldn't open file: $file2\n");


my %matrix1=();
my %matrix2=();
my %common_names=();

# read names of samples on first line of first matrix
my $trash1=<IN>;
chomp $trash1;
my @names1 = split /\t/, $trash1;
shift @names1;
my $size1=0;
my $minM1=100;

#read and store matrix in a 2d array.
while (my $line=<IN>){
  next unless ($line =~ /\w+/);
  chomp $line;
  my @entry=split /\t/, $line;
  my $t = shift @entry;
  $common_names{$t}=1;
  die ("Not same number of columns as names in row $size1\n") unless (scalar(@entry)==scalar(@names1));

  for (my $i=0; $i<@entry; $i++){						### Is making matrix based on Names.
    $matrix1{$names1[$i]}{$t}=$entry[$i];				### Leaves the input data as is!! Should be discrete.
    $minM1=$entry[$i] if ($entry[$i]>0 && $entry[$i]<$minM1);
  }
  $size1++;
}
close IN;

# read names of second matrix
my $trash2=<IN2>;
chomp $trash2;
my @names2 = split /\t/, $trash2;
shift @names2;
my $size2 = 0;
my $minM2=100;

# reads and store matrix2 in 2d array
while (my $line=<IN2>){
  next unless ($line =~ /\w+/);
  chomp $line;
  my @entry=split /\t/, $line;
  my $t = shift @entry;
  die ("Not same number of columns as names in matrix 2 at row $size2\n") unless (scalar(@entry)==scalar(@names2));
  die ("Name $t does not exist in Matrix1\n") unless $common_names{$t};
  
  for (my $i=0; $i<@entry; $i++){						### Is making matrix based on Names2
    $matrix2{$names2[$i]}{$t}=$entry[$i];                              		### Leaves the data as is, should be binary or categories.
    #$matrix2{$names2[$i]}{$t}=0 if ($entry[$i] == 0);
    $minM2=$entry[$i] if ($entry[$i]>0 && $entry[$i]<$minM2);
  }
  $size2++;		
}
close IN2;

die ("Both matrices were not the same size: $size1, $size2 \n") unless ($size1==$size2);

# Is going to print the Information Value.
# Starts by printing the names of matrix 1.
print "Matrix";
for (my $k=0; $k<@names1; $k++){
  print "\t$names1[$k]";
}
print "\n";

# fills in the rest of the matrix.
for (my $i=0; $i<@names2; $i++) {
  print "$names2[$i]";
  for (my $j=0; $j<@names1; $j++){
    my $p= &SP (\%{$matrix1{$names1[$j]}}, \%{$matrix2{$names2[$i]}}, $size1, $minM1, $minM2); #calculates MI for each pair of samples.
    printf ("\t%.3f", $p);
  }
  print "\n";
}
  

sub SP {
  my $arr1=$_[0];
  my $arr2=$_[1];
  my $size=$_[2];
  my $minM1=$_[3]/10;
  my $minM2=$_[4]/10;
  
  my $totalx=0;
  my $totaly=0;
  my $countxy=0;
	
  foreach my $ke (keys %common_names){
	$totalx++ if (${$arr1}{$ke} > 0);
	$totaly++ if (${$arr2}{$ke} > 0);
	$countxy++ if (${$arr1}{$ke} > 0 && ${$arr2}{$ke} > 0);
  }
  my $SP=0;
  if ($countxy==0) {
	$SP=11;		#Completely arbitrary, has to be a large number since the significant should be 0. This is based on the largest real value I observed.
  }else{
	$SP=-log($countxy/$totalx)/log(2) - log($countxy/$totaly)/log(2);	
  }
  return $SP;
}
