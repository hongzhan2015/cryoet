#!/bin/bash
readarray all_lines < $1
one=1
echo '<fsc title="" xaxis="Resolution (A-1)" yaxis="Correlation Coefficient">' > $2
echo '  <coordinate>' >> $2
echo '    <x>0.0</x>' >> $2
echo '    <y>1.0</y>' >> $2
echo '  </coordinate>' >> $2
## now loop through the above array
for i in "${all_lines[@]}"
do
   resolution=`echo $i | awk '{print $2}'`
   spatial_freq=`calc -p 1/$resolution | cut -d'~' -f2`
   fsc=`echo $i | awk '{print $4}'`
echo '  <coordinate>' >> $2
echo "    <x>$spatial_freq</x>" >> $2
echo "    <y>$fsc</y>" >> $2
echo "  </coordinate>" >> $2
done
echo '</fsc>' >> $2
