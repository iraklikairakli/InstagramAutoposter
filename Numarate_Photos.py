a=1

for i in *.jpg; do
 mv -- "$i" "$a.jpg"
 a=`expr $a + 1`
done