#!/usr/bin/perl -w

# Written by Alejandro Reyes

use strict;

if (@ARGV < 5) {
	die "\nUsage: Sort_otu_table.pl [Matrix] [MappingFile] [SortedSubset] [Name of Category(ies) to Sort (separated by ,)] [Category numerical:1, alpha:2 separated by ,] [MinAbundance] > <outfile>\n\n";
}

my $OTUfile = shift;
open (OTU, "<$OTUfile") or die ("Couldn't open file: $OTUfile\n");

my $Mapfile = shift;
open (IN, "<$Mapfile") or die ("Couldn't open file: $Mapfile\n");

my $subsetFile = shift;
open (SUB, "<$subsetFile") or die ("Couldn't open file: $subsetFile\n");

my $cat = shift;
my @cats= split /,/, $cat;

my $type=shift;
my @types=split /,/, $type;

my $min_abundance=shift;

$min_abundance=0 unless ($min_abundance);


# Leer el subset ordenado
my %sortedSubset=();
my $count=1;
while (my $l = <SUB>) {
	chomp($l);
	my @lin = split /\s+/, $l;
	$sortedSubset{$lin[0]}=$count;
	$count++;
}


## Leer el mapping file
my $FirstLine =<IN>;
chomp ($FirstLine);
my %name_map=();
my @names = split /\t/, $FirstLine;
for (my $i=1; $i<@names; $i++){
	#print "creating >$names[$i]< in map\n";
	$name_map{$names[$i]}=$i;
}

foreach my $l (@cats){
  die ("Category >$l< does not exist, options are: ".join(";",@names)."\n") unless $name_map{$l};
}


my @toOrder=();

while (my $line = <IN>){
  chomp $line;
  my @temp = split /\t/, $line;
  push (@toOrder, [@temp]);
}
close IN;


## Sort por Cat
my @sorted=@toOrder;
for (my $i=0; $i<@cats; $i++){
  #print "Ordering by $cats[$i] que es tipo $types[$i]\n";
  my @t_m=();
  if ($types[$i]==2){
    @t_m = sort { $a->[$name_map{$cats[$i]}] cmp $b->[$name_map{$cats[$i]}]} @sorted;
  }else{
    @t_m = sort { $a->[$name_map{$cats[$i]}] <=> $b->[$name_map{$cats[$i]}]} @sorted;
  }
  @sorted=@t_m;
}

## Generar hash con orden
my %ref=();

for (my $i=0; $i<@sorted; $i++){
  #print "$sorted[$i][0]\t$sorted[$i][1]\t$i\n";
  $ref{$sorted[$i][0]}=$i+1;
}



## Leer el otu table
## Imprimirla segun el orden

#print "#OTU\n";


my @order=();
my %seen=();
my @table=();
my $first=0;

while (my $line = <OTU>){
	chomp $line;
  
	my @t=split /\t/, $line;
	next if (scalar(@t)==1);
	#La primera linea que empieza por # tiene los samples IDs;
	if ($line =~ /^\#/ or $first==0){
		$order[0]=0;
		$sortedSubset{$t[0]}=0;
		for (my $i=1; $i<@t; $i++){
			if ($ref{$t[$i]}){
				$order[$i]=$ref{$t[$i]};
				$seen{$t[$i]}=1;
				#print "In here, where exists ref of $t[$i] and now order of $i is $order[$i]\n";
			}else{
				$order[$i]=-1;
			}
		}
		$first=1;
	}
  
	for (my $i=0; $i<@t; $i++){
		#print "i es $i y order es $order[$i] y t es $t[$i]\n" unless ($order[$i]==-1);
		if (exists($sortedSubset{$t[0]})) {
			$table[$sortedSubset{$t[0]}][$order[$i]]=$t[$i] unless ($order[$i]==-1);
			#print "in here\n";
		}
		#print "llenando tabla en $sortedSubset{$t[0]} con $order[$i]\n" unless ($order[$i]==-1 or !($sortedSubset{$t[0]}));
	}
}
close OTU;

my $table_rows=scalar(@table);
my $table_cols=scalar(@{$table[0]});
#die("Esta por imprimir y table tiene tamano $table_rows x $table_cols\n");

for (my $i=0; $i<$table_rows; $i++){
	next unless ($table[$i]);
	my $current_min=0;
	if ($i==0) {
		print join "\t", @{$table[$i]};
		print "\n";
	}else{
		for (my $j=1; $j<$table_cols; $j++){
			$current_min++ if ($table[$i][$j] >= $min_abundance);
		}
		if ($current_min > 2) {
			print join "\t", @{$table[$i]};
			print "\n";
		}	
	}
}