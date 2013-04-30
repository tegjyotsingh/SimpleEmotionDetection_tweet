#bash script to run the Get twitter script after every one hour till the time specified as argument
# specify the numbe of probes as the parameter
# one probe is made after every 10m, change the parameter if needed
for i in `seq 1 $1`;
do
echo $i
sleep 10m
var="python tweets_collector.py"
eval $var
done
